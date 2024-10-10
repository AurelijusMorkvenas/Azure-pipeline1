Azure Data Pipeline Project
This repository contains the code and resources for a complete Azure data pipeline project. The project involves generating sensor data at the edge, uploading it to Azure Queue Storage, processing the data using an Azure Logic App, storing it in an Azure SQL database, and visualizing the data using Grafana and PowerBI.

Architecture Overview
Components
Data Producer: Simulates sensor data generation and sends it to Azure Queue Storage.
Azure Queue Storage: Acts as the intermediary for data ingestion.
Azure Logic App: Automates the process of transferring data from Azure Queue Storage to Azure SQL Database.
Azure SQL Database: Stores the processed sensor data.
Data Consumers:
Grafana: Visualizes the sensor data using a dashboard hosted on a virtual machine (VM).
PowerBI: Provides business intelligence insights and reports based on the stored sensor data.
Menu-Driven UI: A cloud-side Python application allowing interaction with the data through a terminal-based interface.
Prerequisites
Before you begin, ensure you have the following:

Azure Account: Set up your Azure environment including Virtual Machine, SQL Server, SQL Database, Storage Account, and Logic App.
Python 3.12: Ensure Python 3.12 is installed on both your local machine and your VM.
Required Python Libraries: Install the required libraries such as pyodbc, azure-storage-queue, and python-dotenv in your environment.
Azure SQL Database: You should have created an Azure SQL Database instance for storing sensor data.
Steps to Run the Project
1. Clone the Repository
To clone the project repository, run the following command in your terminal:
git clone https://github.com/AurelijusMorkvenas/Azure-pipeline1.git

2. Set Up the Virtual Machine (VM)
After cloning the repository, you need to ensure the virtual machine is running and set up the necessary dependencies.

a. Connect to the VM
Log into your virtual machine (VM1) using SSH:
ssh azureuser@<your-vm-ip>
b. Activate the Python Virtual Environment
Activate the Python virtual environment on your VM:
source ~/myenv/bin/activate
c. Install the Required Python Libraries
Install the required Python libraries inside the virtual environment:
pip install -r requirements.txt
d. Run the Menu-Driven UI
To interact with the sensor data via a terminal-based UI, run the following command on your VM:
python /home/azureuser/menu_ui.py


3. Run the Data Producer
Run the data producer script to simulate sensor data and send it to Azure Queue Storage:
python data_producer.py
This script will continuously generate sensor data and upload it to Azure Queue Storage.

4. Azure Logic App
The Azure Logic App is configured to automatically pick up the data from Azure Queue Storage and ingest it into the Azure SQL Database. You can verify that the data is ingested properly by querying the SQL database.

5. Visualize Data in Grafana
You can visualize the sensor data in Grafana by following these steps:

a. Access Grafana
Open Grafana in your browser by navigating to the following address (make sure the VM is running):
http://<your-vm-ip>:3000
b. Log In
Log in with your credentials (the default username is admin).

c. Create a Dashboard
In Grafana, create a dashboard to visualize the data stored in your SQL database. Use appropriate visualizations such as time series graphs to display the sensor data.

6. Visualize Data in Power BI
Follow these steps to visualize the sensor data using Power BI:

a. Connect Power BI to Azure SQL Database
Open Power BI Desktop. Go to Get Data > Azure > Azure SQL Database. Enter the necessary connection details to connect Power BI to your Azure SQL Database.

b. Create Visualizations
Once connected, you can create visualizations using the stored sensor data. Use charts like line graphs, bar charts, and tables to represent the data effectively.

Cost Analysis
This project includes a cost analysis comparing two approaches to running a 10TB database:

Azure SQL Database (Serverless)
Azure Virtual Machine with PostgreSQL installed
You can find the details of this cost analysis in the screenshots folder of this repository.

Screenshots
This repository includes screenshots that demonstrate the working system, from data generation to data visualization in Grafana, Power BI, and the terminal-based menu-driven UI.