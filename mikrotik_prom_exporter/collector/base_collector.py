from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, InfoMetricFamily
from mikrotik_prom_exporter.config import ConfigKeys

class BaseCollector:
    """
    Base Collector class
    """
    
    @staticmethod
    def add_collector(type: str, name: str, documentation: str, records, metric_key=None, labels=None):
        labels = labels or []
        records = records or []
        
        BaseCollector._add_id_labels(labels)
        
        match type:
            case "info":
                collector = InfoMetricFamily(f"mktpe_{name}", documentation=documentation)
                for record in records:
                    values = {label: record.get(label) 
                            if record.get(label) else '' for label in labels}
                    collector.add_metric(labels, values)
                return collector
            case "counter":
                collector = CounterMetricFamily(f"mktpe_{name}", documentation=documentation, labels=labels)
                for record in records:
                    label_values = [record.get(label) if record.get(label) else '' for label in labels]
                    collector.add_metric(label_values, record.get(metric_key, 0))
                return collector
            case "gauge":
                collector = GaugeMetricFamily(f"mktpe_{name}", documentation=documentation, labels=labels)
                for record in records:
                    label_values = [record.get(label) if record.get(label) else '' for label in labels]
                    print(label_values)
                    collector.add_metric(label_values, record.get(metric_key, 0))
                return collector
            case _:
                print("Invalid collector type specified!")
                return None
            
        
    
    # Helpers
    @staticmethod
    def _add_id_labels(labels):
        labels.append(ConfigKeys.ROUTERBOARD_ADDRESS)
    
    @staticmethod
    def _normalise_keys(key):
        chars = ".-"
        for chr in chars:
            if chr in key:
                key = key.replace(chr, "_")     
        return key