import httpx, re
from datetime import timedelta
from mikrotik_prom_exporter.collector.base_collector import BaseCollector


class ResourceCollector(BaseCollector):
    
    @staticmethod
    def collect(router_identity, router_api):
        labels = ["architecture_name", "bad_blocks", "board_name",
                  "build_time", "cpu", "cpu_count", "cpu_frequency",
                  "cpu_load", "factory_software", "free_hdd_space",
                  "free_memory", "platform", "total_hdd_space",
                  "total_memory", "uptime", "version",
                  "write_sect_since_reboot", "write_sect_total"]
        records = []
        try:
            data = router_api.resource()
        except httpx.HTTPError as exc:
            print(f"HTTP Exception for {exc.request.url} - {exc}")
        
        # normalize the records
        normalized = {BaseCollector._normalise_keys(key): value
                   for (key, value) in data.items()
                   if BaseCollector._normalise_keys(key) in labels}
        
        # Add router identifiers
        for key, value in router_identity.items():
            normalized[key] = value
        
        normalized['uptime'] = timespan(normalized['uptime'])
        
        records.append(normalized)
        
        if records:
            uptime_metrics = BaseCollector.add_collector(
                'gauge', 'system_uptime', 
                'Time interval since boot-up', records, 
                'uptime', ['version', 'board_name', 
                           'cpu', 'architecture_name',
                           'platform'])
            yield uptime_metrics
            
            free_memory_metrics = BaseCollector.add_collector(
                'gauge', 'system_free_memory',
                'Unused amount of RAM', records,
                'free_memory', ['version', 'board_name', 
                                'cpu', 'architecture_name',
                                'platform'])
            yield free_memory_metrics
            
            total_memory_metrics = BaseCollector.add_collector(
                'gauge', 'system_total_memory',
                'Amount of installed RAM', records,
                'total_memory', ['version', 'board_name', 
                                 'cpu', 'architecture_name',
                                 'platform'])
            yield total_memory_metrics
            
            free_hdd_metrics = BaseCollector.add_collector(
                'gauge', 'system_free_hdd_space',
                'Free space on hard drive or NAND', records,
                'free_hdd_space', ['version', 'board_name', 
                                   'cpu', 'architecture_name',
                                   'platform'])
            yield free_hdd_metrics
            
            total_hdd_metrics = BaseCollector.add_collector(
                'gauge', 'system_total_hdd_space',
                'Size of the hard drive or NAND', records,
                'total_hdd_space', ['version', 'board_name', 
                                    'cpu', 'architecture_name',
                                    'platform'])
            yield total_hdd_metrics
            
            cpu_load_metrics = BaseCollector.add_collector(
                'gauge', 'system_cpu_load',
                'Percentage of used CPU resources', records,
                'cpu_load', ['version', 'board_name', 
                             'cpu', 'architecture_name',
                             'platform'])
            yield cpu_load_metrics
            
            cpu_count_metrics = BaseCollector.add_collector(
                'gauge', 'system_cpu_count',
                'Number of CPUs present on the system', records,
                'cpu_count', ['version', 'board_name', 
                              'cpu', 'architecture_name',
                              'platform'])
            yield cpu_count_metrics
            
            cpu_frequency_metrics = BaseCollector.add_collector(
                'gauge', 'system_cpu_frequency',
                'Current CPU frequency', records,
                'cpu_frequency', ['version', 'board_name', 
                                  'cpu', 'architecture_name',
                                  'platform'])
            yield cpu_frequency_metrics
            
            bad_blocks_metrics = BaseCollector.add_collector(
                'gauge', 'system_bad_blocks',
                'Percent of bad blocks on the system', records,
                'bad_blocks', ['version', 'board_name', 
                               'cpu', 'architecture_name',
                               'platform'])
            yield bad_blocks_metrics
    
@staticmethod
def timespan(time):
    duration_rgx = re.compile(r'((?P<weeks>\d+)w)?((?P<days>\d+)d)?((?P<hours>\d+)h)?((?P<minutes>\d+)m)?((?P<seconds>\d+)s)?((?P<milliseconds>\d+)ms)?')
    return timedelta(**{key: int(value) for key, value in duration_rgx.match(time).groupdict().items() if value}).total_seconds()
