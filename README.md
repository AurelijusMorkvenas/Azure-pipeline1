# Azure Data Pipeline Project

This repository contains the code and resources for a complete Azure data pipeline project. The project involves generating sensor data at the edge, uploading it to Azure Queue Storage, processing the data using an Azure Logic App, storing it in an Azure SQL database, and visualizing the data using Grafana and PowerBI.

## Architecture Overview

### Components
1. **Data Producer**: Simulates sensor data generation and sends it to Azure Queue Storage.
2. **Azure Queue Storage**: Acts as the intermediary for data ingestion.
3. **Azure Logic App**: Automates the process of transferring data from Azure Queue Storage to Azure SQL Database.
4. **Azure SQL Database**: Stores the processed sensor data.
5. **Data Consumers**:
   - **Grafana**: Visualizes the sensor data using a dashboard hosted on a virtual machine (VM).
   - **PowerBI**: Provides business intelligence insights and reports based on the stored sensor data.
   - **Menu-Driven UI**: A cloud-side Python application allowing interaction with the data through a terminal-based interface.

---

## Prerequisites

1. **Azure Account**: Set up your Azure environment including Virtual Machine, SQL Server, SQL Database, Storage Account, and Logic App.
2. **Python 3.12**: Ensure Python 3.12 is installed on your local machine and VM.
3. **Required Python Libraries**: Install the required libraries such as `pyodbc`, `azure-storage-queue`, and `python-dotenv`.
4. **Azure SQL Database**: You should have created an Azure SQL Database instance for data storage.

---

## Steps to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/AurelijusMorkvenas/Azure-pipeline1.git

### 2. Set Up the Virtual Machine (VM)
Ensure the virtual machine is running, and that you have set up the necessary dependencies:

- Activate the Python virtual environment:

    ```bash
    source ~/myenv/bin/activate
    ```

- Install necessary Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

- Run the menu-driven UI on the VM:

    ```bash
    python /home/azureuser/menu_ui.py
    ```

### 3. Run the Data Producer
This step generates and sends the sensor data to Azure Queue Storage:

```bash
python data_producer.py

4. Azure Logic App
The Logic App automatically triggers and moves the data from Azure Queue Storage to Azure SQL Database.

5. Grafana
To visualize data in Grafana:

Access Grafana on your virtual machine by navigating to http://<vm-ip>:3000.
Login with your credentials.
Visualize the sensor data using the dashboards set up for this project.
6. PowerBI
Connect PowerBI to the Azure SQL Database.
Create reports and dashboards to visualize the sensor data stored in the SQL Database.

Data Flow Diagram
The following steps outline the data flow in this project:

Edge Data Generation: The data_producer.py script generates random sensor data.
Azure Queue Storage: Sensor data is uploaded to an Azure Queue.
Azure Logic App: Logic App ingests the data from the queue and inserts it into the Azure SQL Database.
SQL Database: Data is stored and available for consumption.
Grafana & PowerBI: Visualize and analyze the sensor data in real-time.

Screenshots
Screenshots of each major step are located in the screenshots/ folder. These include:

Data producer in action
Grafana dashboard
PowerBI reports
Menu-driven UI interacting with the database
Cost Analysis
For this project, a cost comparison was performed between:

Azure SQL Database (serverless).
Azure VM with PostgreSQL installed.
Please refer to the attached screenshots for detailed cost analysis.

Conclusion
This project demonstrates a complete end-to-end Azure-based data pipeline, from data generation at the edge to data consumption using visualization tools such as Grafana and PowerBI. The entire system is automated and runs on Azure's serverless infrastructure.