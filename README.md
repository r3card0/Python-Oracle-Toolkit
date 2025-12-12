# Oracle - Python Database Connector

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Toolkit to connect and manage Oracle databases with Python.

## Description
This toolkit provides a robust solution for connecting to Oracle databases and managing Pluggable Databases (PDB) through Python.

It streamlines database operations by offering a unified interface for executing SQL scripts, performing data extractions and integrating with various analytical and ETL workflows.

The connector is designed for data professionals who need reliable Oracle database connectivity for business analytics, data quality assesments, geospatial data processing, dashboard creation and ETL pipeline development.

## Key Features
* 🔌**Smart Oracle Connection Management** - Seamless connection to Oracle databases with PDB selection.
* 📜 **SQL Script Execution** - Run complex SQL scripts with error handling and logging.
* 🗺️ **Shapefile Export** - Convert spatial data directly to ESRI Shapefile format.
* 🔧 **ETL integration** - Compatible with ETL tools.
* 📊 **Data Quality Tools** - Built-in data validation and quality assessment functions.
* 📈 **Analytics Ready** - Optimized for business intelligence and reporting workflows
* ⚡ **Performance Optimized** - Efficient connection pooling and query execution
  

## Installation

### Prerequisites

* Python 3.10
* Oracle Client Libraries
* Access to Oracle Database 12g or higher

### Installation

You can use this repository in two different ways:

1. **Clone the repository**

Follow the steps below to clone and work directly with the source code.

Clone repository

```bash
git clone https://github.com/r3card0/Python-Oracle-Toolkit.git
```

2. **Install as a dependency**

Alternatively, you can install this repository as a dependency within your own project

1. Create a Python's virtual environment
    ```python
    python3 -m venv <name>
    ```

2. Activate virtual environment
    ```python
    source <name>/bin/activate
    ```

3. Install libraries and dependencies  using the [requirements.txt](/requirements.txt) file

    ```python
    pip install -r requirements.txt
    ```

or install manually

```bash
pip install git+https://github.com/r3card0/Python-Oracle-Toolkit.git@v0.1.0
```

### Usage

Basic Example

```python
from python_oracle_toolkit.process_sql_query import SqlQuery

## Parameters

json_file = r"C:\Users\user\file.json" # or "/mnt/c/Users/user/file.json"

sql_query = r"C:\Users\user\file.sql"  # or "/mnt/c/Users/user/file.sql"

# or 

sql_query2 = """
    SELECT employee_id
    FROM employees
    """

# schema/puggable database
schema = "production_B"

# Run proces
connection = SqlQuery(json_file,sql_query,schema)

# get dataframe
df = connection.create_dataframe()
```

Or go to [notebook1](/notebooks/notebook1.ipynb) file and follow the instructions to start.

### Requirements

The file [requirements.txt](/requirements.txt) contains the libraries and dependencies.

```
pandas
cx_Oracle
jupyter
git+https://github.com/r3card0/Python-Oracle-Toolkit.git@v0.1.0
git+https://github.com/r3card0/WSL-path-converter.git@v0.1.0
```


This project requires an additional dependency that must be installed directly from GitHub repository.

Make sure to install it before running the project. It can be installed manually

```bash
pip install git+https://github.com/r3card0/WSL-path-converter.git@v0.1.0
```

> ⚠️ Note: This dependency is not available on PyPI. It must be installed directly from the GitHub source


## Use cases
**📊 Busines Intelligence**
* Calculate KPIs ad metrics from operational data
* Generate reports for stakeholders meetings
* Perform trend analysis on historical data

**🛣️ Location Intelligence**
* Calculate road network distances: Measure total kilometers of road infraestructure
* Spatial data extraction: Export geographic data for GIS analysis
* Location analysis: Analyze patterns based on geographic distribution

**🔍 Dashboard Integration**
* Validate data integrity
* Identify missing or insconsistencies records
* Generate data quality reports

**🔁 ETL Processes**
* Feed real-time data to Bussines tools such a Tableau
* Create KPI dashboards
* Monitor operational metrics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License

## Acknowledgments

* Inspired by the need for seamless file path conversion when working with WSL
* Built for developers who frequently switch between Windows and Linux environments.

## Author
@[r3card0](https://github.com/r3card0)

Project Links: https://github.com/r3card0/Python-Oracle-Toolkit.git

Dependencies : https://github.com/r3card0/WSL-path-converter


