from prometheus_client.core import REGISTRY
from prometheus_client import make_wsgi_app
from datetime import datetime
from mikrotik_prom_exporter.collector.collection_manager import CollectionManager

REGISTRY.register(CollectionManager())
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f'{current_time} Running HTTP metrics server')
app = make_wsgi_app()