import foam
from config import FOAM_CONFIG

foam.init(
    service_name="merchant-integration-api",
    api_key=FOAM_CONFIG['api_key'],
    is_production=FOAM_CONFIG['is_production'],
    sample_rate=FOAM_CONFIG.get('sample_rate', 1.0),
)