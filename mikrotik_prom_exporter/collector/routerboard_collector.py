import httpx
from mikrotik_prom_exporter.collector.base_collector import BaseCollector


class RouterboardCollector(BaseCollector):
    
    @staticmethod
    def collect(router_identity, router_api):
        labels = ["current_firmware", "factory_firmware", "firmware_type",
                  "model", "routerboard", "serial_number", "upgrade_firmware"]
        records = []
        try:
            data = router_api.routerboard()
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
        
        # normalize the records
        normalized = {BaseCollector._normalise_keys(key): value
                   for (key, value) in data.items()
                   if BaseCollector._normalise_keys(key) in labels}
        
        # Add router identifiers
        for key, value in router_identity.items():
            normalized[key] = value
        
        records.append(normalized)
        if records:
            cur_firmware_metrics = BaseCollector.add_collector(
                'gauge', 'system_current_firmware',
                'System Current Firmware', records,
                'current_firmware', ['firmware_type', 'model',
                                     'routerboard', 'serial_number'])
            yield cur_firmware_metrics
            
            fac_firmware_metrics = BaseCollector.add_collector(
                'gauge', 'system_factory_firmware',
                'System Factory Firmware', records,
                'factory_firmware', ['firmware_type', 'model',
                                     'routerboard', 'serial_number'])
            yield fac_firmware_metrics
            
            upg_firmware_metrics = BaseCollector.add_collector(
                'gauge', 'system_upgrade_firmware',
                'System Upgrade Firmware', records,
                'upgrade_firmware', ['firmware_type', 'model',
                                     'routerboard', 'serial_number'])
            yield upg_firmware_metrics
