# Azure Data Pipeline Project

This project implements an end-to-end data pipeline using Azure services and cloud-side Python programs. The goal is to simulate sensor data generation at the edge, transfer this data to the cloud via Azure Queue Storage, and ingest it into an Azure SQL Database. Data consumers such as Grafana, PowerBI, and a text-based Python UI are used to visualize and analyze the data. Additionally, cost analysis using the Azure Pricing Calculator is included.



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

1. **Virtual Machine (VM1)**
   - **Purpose**: Runs the cloud-side Python program and hosts Grafana for visualizing data.
   
2. **SQL Server & Azure SQL Database**
   - **Server**: `myservername`
   - **Database**: `mydbname`
   - **Purpose**: Central repository for all sensor data ingested from the Azure Queue.

3. **Azure Queue Storage**
   - **Storage Account**: `myqueuename`
   - **Purpose**: Buffers sensor data before it's ingested into the SQL database.

4. **Azure Logic App**
   - **Name**: `QueueToSQLLogicApp`
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



### Prerequisites

1. **Azure Subscription**: Ensure you have an active Azure subscription.
2. **Virtual Machine**: The VM should have Python 3.x installed with `pyodbc`, `azure-storage-queue`, and `python-dotenv` libraries. Instructions for setting up these dependencies are provided.
3. **Grafana**: Installed and configured on the VM.
4. **PowerBI**: Installed on your local machine, connected to the Azure SQL Database.


### Screenshots included























































