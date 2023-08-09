# Performance Monitoring and Data Visualization Project

Welcome to the Performance Monitoring and Data Visualization project! This project aims to capture, store, and visualize real-time system performance metrics through an end-to-end data pipeline. By leveraging Python, MySQL, SQL Server, and Power BI, we've created a comprehensive solution to enhance decision-making.

----
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Data Flow](#data-flow)
- [Dashboard Preview](#dashboard-preview)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

----
## Introduction

System performance monitoring is crucial for maintaining operational efficiency and preemptively identifying potential issues. This project takes a data-driven approach to capture, store, and visualize performance metrics in real-time, providing insights for informed decision-making.

---
## Features

- Fetches real-time Performance Monitoring Data using Python scripts(using psutil library).
- Stores captured data securely in a MySQL database (using mysql-connector-python API).
- Establishes a data pipeline to transfer data from MySQL to SQL Server database(using pyodbc API).
- Connects SQL Server to Power BI for creating dynamic visualizations.
- Constructs an interactive real-time dashboard for monitoring system performance.

---
## Technologies Used

- Python
- MySQL
- SQL Server
- Power BI

---
## Setup Instructions

1. Clone the repository: `git clone https://github.com/aymane-maghouti/Real-time-Computer-Performance-Dashboard.git`
2. Install required dependencies by following the instructions in the `requirements.txt` file.
3. Set up the MySQL and SQL Server databases according to the provided schema.(Execute the `database_installation.sql` script on both the MySQL and SQL Server databases.)
4. Configure the Python scripts with the necessary connection details.

    **For MySQL:**\n
    *host* = 'localhost'\n
    *database* = 'system_Performance'\n
    *user* = your username (root by default)\n
    *password* = your password\n
    *table_name* = 'performance'\\n

    **For SQL Server:**
    "*Driver*={SQL Server};"
    "*Server*=your server name;"
    "*Database*=System_Performance;"
    "*Trusted_Connection*=yes;"


5. Install Power BI and connect to the SQL Server database(Or you can just open the system_performance.pbix file with powerBI software).

---
## Usage

1. Run the Python script to fetch Performance Monitoring Data.(main.py script)
2. Data is automatically stored in the MySQL database.
3. The data pipeline transfers data from MySQL to SQL Server.
4. Open the Power BI file to access the real-time dashboard.

[video]

---
## Data Flow

1. Python script fetches data →
2. Data stored in MySQL database →
3. Data transferred to SQL Server via pipeline →
4. Power BI accesses SQL Server and creates visualizations.

![Screenshot of the Real-time Dashboard](/images/workFlow.png)

---
## Dashboard Preview

The final result of the project is a `real time dashboard`

![Screenshot of the Real-time Dashboard](/images/system_performance.png)

---
## Acknowledgments
-We would like to express our gratitude to the following resources for their valuable contributions to this project:

The official documentation of `Python` language.

The documentation provided by `MySQL` and `SQL Server` for configuring and working with the database.

The `Power BI` documentation, which aided in creating the dashboard.


Feel free to customize the content and functionality of this Project according to your specific requirements.

---
## Contact
<a href="https://www.linkedin.com/in/aymane-maghouti/" target="_blank">Aymane Maghouti</a><br>


---