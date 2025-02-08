import os
import configparser


class ConfigKeys:
    HOST_KEY = 'hostname'
    PORT_KEY = 'port'
    USER_KEY = 'username'
    PASSWD_KEY = 'password'
    SSL_CA_PATH = 'ssl_capath'
    SSL_VERIFY = 'ssl_verify'
    
    # Config keys for collectors
    ROUTERBOARD_ADDRESS = 'routerboard_address'
    IDENTITY_COLLECTOR = 'IdentityCollector'
    HEALTH_COLLECTOR = 'HealthCollector'
    RESOURCE_COLLECTOR = 'ResourceCollector'
    ROUTERBOARD_COLLECTOR = 'RouterboardCollector'
    
class ConfigManager:
    # init config file
    def __init__(self):
        self.config_file = os.getenv('MKTPE_CONFIG', './mktpe.conf')
        self.config = configparser.ConfigParser(inline_comment_prefixes='#')
        self.config.read(self.config_file)
        
    def get(self, config_key, config_section = 'MKTPE', boolean=False):
        if boolean:
            return self.config.getboolean(config_section, config_key, fallback=True)

        return self.config.get(config_section, config_key, fallback=None)