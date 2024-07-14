Dbrain-Kafka
Overview:
  This project utilizes Kafka for messaging between a web page and a backend service. It includes a Flask-based REST API for interacting with Kafka messages.
Features:
  Kafka Producer and Consumer: Handles messaging between web page and backend.
  REST API with Flask: Provides endpoints for viewing data and sending messages to Kafka.
  Optional Kafka Topic: Data can be read without a mandatory Kafka topic.
Prerequisites:
  Docker
  Python 3.x
Installation:
  Clone the repository: git clone <repository-url>
  Navigate to the project directory.
  Build Docker containers: docker-compose up --build
Usage:
  Access the web page: http://localhost:8001/
  Use REST API endpoints:
  /: View data and download JSON file.
  /api/send-data: Send data to Kafka (if topic is created in your device).
  Configuration
  Adjust Kafka and Flask settings in docker-compose.yml and res_api.py as needed.
