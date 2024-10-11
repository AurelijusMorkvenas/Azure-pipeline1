import os
from azure.storage.queue import QueueClient
import json
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file (optional, if using .env)
load_dotenv()

# Retrieve the connection string from environment variables
connection_string = os.getenv("AZURE_QUEUE_CONNECTION_STRING")
queue_name = os.getenv("AZURE_QUEUE_NAME")
queue_client = QueueClient.from_connection_string(connection_string, queue_name)

# Function to generate sample data
def generate_sample_data():
    devices = [f"Device_{i}" for i in range(1, 11)]
    locations = ["Stockholm", "Gothenburg", "Malmo", "Uppsala"]
    statuses = ["OK", "Warning", "Critical"]

    data = {
        "location": random.choice(locations),
        "timestamp": (datetime.now() - timedelta(seconds=random.randint(1, 10000))).strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(-10.0, 40.0), 2),
        "humidity": round(random.uniform(10.0, 90.0), 2),
        "pressure": round(random.uniform(950.0, 1050.0), 2),
        "status": random.choice(statuses)
    }
    return json.dumps(data)

# Send message to Azure Queue
def send_message_to_queue():
    message = generate_sample_data()
    queue_client.send_message(message)
    print(f"Message sent: {message}")

# Send multiple messages
if __name__ == "__main__":
    for _ in range(1):
        send_message_to_queue()
