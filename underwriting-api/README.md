# Underwriting API

Real-time consumer credit decisioning service for Affirm loan products. Built with Python/Flask, this service evaluates loan applications using ML models from the feature store, applies risk policies, and returns instant credit decisions with transparent pricing.

**Tech Stack:** Python 3.11, Flask, MySQL, Redis, Celery, AWS Lambda

**Local Development:** `docker-compose up` to start dependencies, then `flask run --port 5000`