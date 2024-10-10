Azure Data Pipeline Project
Project Overview
This project demonstrates a full data pipeline implementation using Azure services, from edge data generation to data consumption through multiple platforms. The pipeline integrates real-time data ingestion, processing, storage, and visualization.

Key Components
Virtual Machine (VM1): Hosts various services and tools, including Grafana for data visualization.
Azure SQL Server: mydatapipelineserver hosts the SQL database used for data storage.
Azure SQL Database: mydatapipelinedb is the main database where processed data is stored.
Azure Storage Account: mydatapipelinequeue handles message queues for serverless data transfer.
Logic App: QueueToSQLLogicApp ingests data from the Azure Storage Queue into the SQL Database.
Grafana: Deployed on the VM for real-time monitoring of data.
PowerBI: Used locally for data visualization using data from the Azure SQL Database.
Python Menu-driven UI: A cloud-side Python script (menu_ui.py) that interacts with the SQL database, providing a text-based user interface for querying and displaying data.
Data Flow Diagram
This pipeline covers the full data flow from data generation to consumption:

Edge Data Generation: Using data_producer.py, real-time data is generated on the edge.
Data Ingestion to the Cloud: The edge-generated data is uploaded to Azure via a serverless queue in the mydatapipelinequeue storage account.
Queue to Database: The QueueToSQLLogicApp ingests the data from the Azure queue and inserts it into the mydatapipelinedb Azure SQL Database.
Data Storage: The processed data is stored in the serverless Azure SQL Database (mydatapipelinedb).
Data Consumption:
Grafana: Visualizes real-time data directly from the SQL Database (hosted on VM1).
PowerBI: Locally connects to the SQL Database and provides a rich dashboard with visualization.
Python Program: A menu-driven UI (menu_ui.py) running on VM1, allowing for interactive querying and displaying of data from the database.
Repository Structure
plaintext
Kopiera kod
.
├── data_producer.py       # Generates edge data and uploads to Azure Storage Queue
├── menu_ui.py             # Cloud-side Python program with a text-based menu for querying the database
├── azure_deployment.json  # Contains ARM template for deploying Azure resources
├── screenshots/           # Folder with screenshots showing the working data flow and services
├── README.md              # This README file
Detailed Explanation of Files
data_producer.py

Purpose: Simulates edge data generation and uploads the data to the Azure queue (mydatapipelinequeue).
Where it Runs: This script is intended to run on an edge device or any environment that simulates real-time data production.
menu_ui.py

Purpose: A cloud-side Python script providing an interactive text-based menu-driven UI for querying data from the Azure SQL Database (mydatapipelinedb).
Where it Runs: This script runs on the VM (VM1), which interacts with the SQL Database.
azure_deployment.json

Purpose: An Azure Resource Manager (ARM) template for automating the deployment of the Azure resources used in this project (SQL Server, Storage, Logic Apps, etc.).
Where it Runs: Run in the Azure portal or via CLI to deploy the resources.
screenshots/

Contains: Screenshots of the working data flow, from data generation through the edge, ingestion into the cloud, database storage, and data visualization in Grafana, PowerBI, and the Python UI.
Setup and Execution Instructions
Clone the repository:

bash
Kopiera kod
git clone https://github.com/your-repo-url.git
cd your-repo-url
Running the Data Producer:

Ensure you have Python and the necessary Azure SDKs installed.
Run the data_producer.py script to simulate edge data production:
bash
Kopiera kod
python data_producer.py
Running the Python UI on VM1:

Connect to your VM (VM1) where the script will be executed.
Run the menu_ui.py to interact with the Azure SQL Database:
bash
Kopiera kod
python menu_ui.py
Viewing Data in Grafana:

Access Grafana on VM1 using port 3000 (if not configured, ensure inbound port rules are set):
arduino
Kopiera kod
http://<VM1-IP>:3000
Viewing Data in PowerBI:

Open PowerBI locally and connect it to the Azure SQL Database (mydatapipelinedb).
Load the data and visualize it using custom dashboards.
Screenshots
Feature	Screenshot Preview
Data Generation (Producer)	
Azure Queue (Storage)	
Logic App	
SQL Database (Azure)	
Grafana Dashboard	
PowerBI Dashboard	
Python UI	
Cost Analysis
A full cost analysis of the project was conducted using the Azure Pricing Calculator. The total estimated cost for running this pipeline, based on the current configuration and expected usage, is provided in the attached screenshots (screenshots/cost_analysis.png).