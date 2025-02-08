from RestRouterOS.api import RestRouterOS
from prometheus_client.registry import Collector
from collections import OrderedDict
from mikrotik_prom_exporter.collector.identity_collector import IdentityCollector
from mikrotik_prom_exporter.collector.health_collector import HealthCollector
from mikrotik_prom_exporter.collector.routerboard_collector import RouterboardCollector
from mikrotik_prom_exporter.collector.resource_collector import ResourceCollector
from mikrotik_prom_exporter.config import ConfigManager, ConfigKeys

class CollectionManager(Collector):
    """
    Manager to hanlde all collections
    """
    def __init__(self):
        self.collectors = OrderedDict()
        self.config = ConfigManager()
        print(self.config.get(ConfigKeys.SSL_VERIFY))
        self.router_identity = {
            ConfigKeys.ROUTERBOARD_ADDRESS: self.config.get(ConfigKeys.HOST_KEY)
        }
        # Create the REST RouterOS for the router
        self.router_api = RestRouterOS(self.config.get(ConfigKeys.HOST_KEY), 
                                       self.config.get(ConfigKeys.USER_KEY), 
                                       self.config.get(ConfigKeys.PASSWD_KEY),
                                       self.config.get(ConfigKeys.PORT_KEY),
                                       self.config.get(ConfigKeys.SSL_VERIFY, True),
                                       self.config.get(ConfigKeys.SSL_CA_PATH))
        
        # Register the collectors
        self.register(ConfigKeys.IDENTITY_COLLECTOR, IdentityCollector.collect)
        self.register(ConfigKeys.HEALTH_COLLECTOR, HealthCollector.collect)
        self.register(ConfigKeys.ROUTERBOARD_COLLECTOR, RouterboardCollector.collect)
        self.register(ConfigKeys.RESOURCE_COLLECTOR, ResourceCollector.collect)
        
    def register(self, collector_id, collector_function):
        self.collectors[collector_id] = collector_function
        
    def collect(self):
        for collector_id, collector_function in self.collectors.items():
            yield from collector_function(self.router_identity, self.router_api)