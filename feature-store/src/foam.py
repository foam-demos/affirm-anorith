import foam
from src.config import FOAM_API_KEY, ENVIRONMENT

foam.init(
    service_name="feature-store",
    api_key=FOAM_API_KEY,
    is_production=ENVIRONMENT == "production",
    sample_rate=0.2 if ENVIRONMENT == "production" else 1.0,
)