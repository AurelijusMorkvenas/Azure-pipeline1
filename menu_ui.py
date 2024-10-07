import os
import pyodbc
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the database connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER=mydatapipelineserver.database.windows.net;"
    f"DATABASE=mydatapipelinedb;"
    f"UID={os.getenv('AZURE_SQL_USERNAME')};"
    f"PWD={os.getenv('AZURE_SQL_PASSWORD')}"
)


# Function to display the menu
def show_menu():
    print("1. View all sensor data")
    print("2. View data by location")
    print("3. Exit")

# Function to get and display all data from the database
def get_all_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SensorData")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"Device ID: {row.device_id}, Location: {row.location}, Timestamp: {row.timestamp}, "
                  f"Temperature: {row.temperature}, Humidity: {row.humidity}, Pressure: {row.pressure}, Status: {row.status}")
    else:
        print("No data found.")

# Function to filter data by location
def get_data_by_location():
    location = input("Enter the location: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SensorData WHERE location = ?", location)
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"Device ID: {row.device_id}, Location: {row.location}, Timestamp: {row.timestamp}, "
                  f"Temperature: {row.temperature}, Humidity: {row.humidity}, Pressure: {row.pressure}, Status: {row.status}")
    else:
        print(f"No data found for location: {location}")

# Main loop to run the menu-driven interface
if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            get_all_data()
        elif choice == '2':
            get_data_by_location()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
