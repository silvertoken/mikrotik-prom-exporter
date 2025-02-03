import httpx
from mikrotik_prom_exporter.collector.base_collector import BaseCollector


class IdentityCollector(BaseCollector):
    
    @staticmethod
    def collect(router_identity, router_api):
        labels = ['name']
        records = []
        try:
            data = router_api.identity()
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
        
        # Add router identifiers
        for key, value in router_identity.items():
            data[key] = value
        
        records.append(data)
        metrics = BaseCollector.add_collector('info', 'system_identity', 'System Identity', records, labels=labels)
        yield metrics
        
        