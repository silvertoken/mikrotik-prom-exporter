import httpx
from mikrotik_prom_exporter.collector.base_collector import BaseCollector


class HealthCollector(BaseCollector):
    
    @staticmethod
    def collect(router_identity, router_api):

        try:
            data = router_api.health()
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
        
        
        for record in data:
            if 'name' in record:
                # Add router identifiers
                for key, value in router_identity.items():
                    record[key] = value
                
                # Note: The API in RouterOS v7.X+ returns a response like this:
                # [{'name': 'temperature', 'value': '33', 'type': 'C'}, ...] 
                match record['name']:
                    case 'voltage':
                        voltage_metrics = BaseCollector.add_collector(
                            'gauge', 'system_routerboard_voltage',
                            'Supplied routerboard voltage', [record, ],
                            'value')
                        yield voltage_metrics
                    case 'temperature':
                        temperature_metrics = BaseCollector.add_collector(
                            'gauge', 'system_routerboard_temperature',
                            'Routerboard current temperature', [record, ],
                            'value')
                        yield temperature_metrics
                    case _:
                        print(f"Record - {record['name']} not supported")
