# Oracle - Python Database Connector
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

Clone repository

```bash
git clone https://github.com/r3card0/Python-Oracle-Toolkit.git
```

### Prerequisites

* Python 3.10
* Oracle Client Libraries
* Access to Oracle Database 12g or higher

### Requirements

The file [requierements.txt](/requirements.txt) contains the libraries and dependencies.

```
pandas
cx_Oracle
jupyter
git+https://github.com/r3card0/WSL-path-converter.git@v0.1.0
```

Create  a virtual environment

```python
python3 -m venv venv_name
```

Activate the virtual environment

```python
source venv_name/bin/activate
```


You can use the requirements.txt file to perform the installation of libraries and dependencies.

```bash
pip install -r requirements.txt
```

This project requires an additional dependency that must be installed directly from GitHub repository.

Make sure to install it before running the project. It can be installed manually

```bash
pip install git+https://github.com/r3card0/WSL-path-converter.git@v0.1.0
```

> ⚠️ Note: This dependency is not available on PyPI. It must be installed directly from the GitHub source

## Implementation

1. Open a new python file or notebook
2. Set parent folder and SqlQuery class
   ```python
   # Import 
    import sys
    from pathlib import Path

    # Add the parent folder of Python to the path
    parent_folder = Path.cwd().parent  # Move up one directory from notebooks/
    sys.path.insert(0, str(parent_folder))

    from utils.process_sql_query import SqlQuery
   ```

3. Set Parameters
    ```python
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
    ```

4. Run process
    ```python
    connection = SqlQuery(json_file,sql_query,schema)
    ```

    ```python
    # get dataframe
    df = connection.create_dataframe
    ```

Or go to [notebook1](/notebooks/notebook1.ipynb) file and follow the instructions to start.


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


