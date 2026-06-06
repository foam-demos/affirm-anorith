# VCN Gateway

Virtual Card Network gateway service that connects Affirm loans to Visa's payment network. Handles authorization, capture, settlement, and chargebacks for virtual and physical Affirm cards.

**Tech Stack:** Kotlin, Spring Boot, PostgreSQL, Kafka, gRPC

**Local Development:** `./gradlew bootRun` after setting up Postgres and Kafka via `docker-compose up -d`