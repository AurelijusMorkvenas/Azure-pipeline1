# Azure Data Pipeline Project

This repository contains the code and resources for a complete Azure Data Pipeline project. The project simulates sensor data generation, sends it to Azure Queue Storage, processes the data using an Azure Logic App, stores the data in an Azure SQL Database, and visualizes the data using Grafana and PowerBI.

---

## Architecture Overview

- **Data Producer**: Simulates sensor data generation and sends it to Azure Queue Storage.
- **Azure Queue Storage**: Used as the intermediary for data ingestion into the cloud.
- **Azure Logic App**: Transfers data from Azure Queue Storage to Azure SQL Database.
- **Azure SQL Database**: Stores the processed sensor data.
- **Data Consumers**:
  - **Grafana**: Visualizes the sensor data using a dashboard hosted on a virtual machine (VM).
  - **PowerBI**: Provides insights and reports based on the stored sensor data.
  - **Menu-Driven UI**: A cloud-side Python program that allows interaction with the data through a terminal-based interface.

---

## Prerequisites

Before you begin, ensure you have the following:

1. **Azure Account**: Set up your Azure environment, including a Virtual Machine, SQL Server, SQL Database, Storage Account, and Logic App.
2. **Python 3.12**: Make sure Python 3.12 is installed on both your local machine and VM.
3. **Required Python Libraries**: Install the required libraries, such as `pyodbc`, `azure-storage-queue`, and `python-dotenv`.
4. **Azure SQL Database**: Ensure you have created an Azure SQL Database instance for storing sensor data.

---

## Steps to Run the Project

### 1. Clone the Repository

To clone the project repository, run the following command in your terminal:

```bash
git clone https://github.com/AurelijusMorkvenas/Azure-pipeline1.git

### 2. Set Up the Virtual Machine (VM)

After cloning the repository, you need to ensure the virtual machine is running and that you have set up the necessary dependencies.

#### a. Connect to the VM

Log into your virtual machine (VM1) using SSH:

```bash
ssh azureuser@<your-vm-ip>
