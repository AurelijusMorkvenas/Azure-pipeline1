
markdown
Kopiera kod
# Azure Data Pipeline Project

This project implements an end-to-end data pipeline using Azure services and cloud-side Python programs. The goal is to simulate sensor data generation at the edge, transfer this data to the cloud via Azure Queue Storage, and ingest it into an Azure SQL Database. Data consumers such as Grafana, PowerBI, and a text-based Python UI are used to visualize and analyze the data. Additionally, cost analysis using the Azure Pricing Calculator is included.

## Table of Contents

1. [Overview](#overview)
2. [System Components](#system-components)
3. [Data Flow](#data-flow)
4. [Instructions](#instructions)
5. [Cost Analysis](#cost-analysis)
6. [Screenshots](#screenshots)
7. [Project Structure](#project-structure)

---

## Overview

This project demonstrates a real-world data pipeline that moves data from an edge device to the cloud. It incorporates serverless and cloud-based technologies and services, ensuring scalability and efficient data processing.

Key technologies used:
- **Azure Queue Storage**: For queuing messages generated at the edge.
- **Azure Logic App**: To ingest data from the queue into an Azure SQL Database.
- **Azure SQL Database**: To store and manage data.
- **Grafana**: For data visualization.
- **PowerBI**: For additional data analysis.
- **Python-based CLI**: A cloud-side Python program for data interaction via a text-based menu.

---

## System Components

1. **Virtual Machine**
   - **Purpose**: Runs the cloud-side Python program and hosts Grafana for visualizing data.
   
2. **SQL Server & Azure SQL Database**
   - **Purpose**: Central repository for all sensor data ingested from the Azure Queue.

3. **Azure Queue Storage**
   - **Purpose**: Buffers sensor data before it's ingested into the SQL database.

4. **Azure Logic App**
   - **Purpose**: Automates ingestion of queued data into the Azure SQL Database.

5. **Python-based Menu UI**
   - **Script**: `menu_ui.py`
   - **Purpose**: A cloud-side Python program that provides a text-based interface for querying sensor data in the SQL database.

---

## Data Flow

1. **Sensor Data Generation (Edge)**
   - Script: `data_producer.py`
   - Description: Simulates sensor data and uploads it to Azure Queue Storage.

2. **Azure Queue Storage**: Stores the sensor data.

3. **Azure Logic App**: Retrieves data from the queue and ingests it into the Azure SQL Database.

4. **Azure SQL Database**: Stores the ingested data for querying and analysis.

5. **Data Consumers**:
   - **Grafana**: Used to visualize sensor data.
   - **PowerBI**: Connects to the Azure SQL Database for further data analysis and dashboard creation.
   - **Python-based Menu UI**: Allows users to interact with the SQL database through the command line.

---

## Instructions

### Prerequisites

1. **Azure Subscription**: Ensure you have an active Azure subscription.
2. **Virtual Machine**: The VM should have Python 3.x installed with `pyodbc`, `azure-storage-queue`, and `python-dotenv` libraries. Instructions for setting up these dependencies are provided.
3. **Grafana**: Installed and configured on the VM.
4. **PowerBI**: Installed on your local machine, connected to the Azure SQL Database.

### Steps to Run the Project

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/AurelijusMorkvenas/Azure-pipeline1.git
Set Up the Virtual Machine (VM1):

Ensure the VM is running and all dependencies are installed.
Run menu_ui.py on the VM to interact with the Azure SQL Database.
Run Data Producer:

bash
Kopiera kod
python data_producer.py
This script simulates sensor data and pushes it to the Azure Queue Storage.

Azure Logic App: The Logic App will automatically trigger and ingest the queued data into the Azure SQL Database.

Use Grafana:

Access Grafana via your VM’s public IP (port 3000).
Visualize the sensor data using pre-configured dashboards.

Use PowerBI:

Connect PowerBI to the Azure SQL Database and analyze data using custom dashboards.

Cost Analysis

A detailed cost analysis comparing:

Azure SQL Database (Serverless)
Azure VM with PostgreSQL Installed
The cost comparison assumes a 10TB database and was performed using the Azure Pricing Calculator. See the attached screenshot for details.

Screenshots
1. Data Producer
Screenshot of the data_producer.py running.

2. Azure Logic App
A screenshot showing the successful data ingestion via the Logic App.

3. Grafana Dashboard
Visualizations of sensor data on Grafana.

4. PowerBI Dashboard
Data analysis and visualizations using PowerBI.

5. Text-based Menu UI
Screenshot showing the interaction with the cloud-side Python program.

6. Cost Analysis
Azure Pricing Calculator estimates for SQL Database and VM-based solutions.

Project Structure
bash
Kopiera kod
.
├── data_producer.py                # Simulates sensor data generation (Edge)
├── menu_ui.py                      # Python-based menu for querying the Azure SQL Database
├── .env                            # Environment variables for secure credentials
├── README.md                       # This file
├── Azure Logic App (QueueToSQLLogicApp)
│   └── Logic App screenshot
├── Grafana Dashboards               # Configured dashboards in Grafana
└── PowerBI Dashboards               # Configured PowerBI dashboards
Each file's purpose and location:
data_producer.py: Runs locally or on an edge device to generate sensor data and push to the Azure Queue.
menu_ui.py: Cloud-side Python program running on the VM for data interaction via command line.
.env: Holds sensitive credentials for Azure services.
License
This project is licensed under the MIT License.