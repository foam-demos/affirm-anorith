# Feature Store

ML feature platform that provides real-time and batch feature computation for Affirm's credit risk models. Serves features via gRPC with sub-50ms p99 latency for underwriting decisions and supports batch ETL for model training.

**Tech Stack:** Python 3.11, gRPC, Redis, Apache Spark, MySQL, AWS S3

**Local Development:** `docker-compose up` for dependencies, then `python -m src.server` to start gRPC server on port 50051