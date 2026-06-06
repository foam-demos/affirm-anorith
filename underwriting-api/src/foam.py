import foam
from config import FOAM_API_KEY, IS_PRODUCTION

foam.init(
    service_name="underwriting-api",
    api_key=FOAM_API_KEY,
    is_production=IS_PRODUCTION,
    sample_rate=1.0 if not IS_PRODUCTION else 0.1,
)