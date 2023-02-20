# Apache Airflow

Based on Airflow version 2.0

### What is Apache Airflow?
    - Open-source workflow management platform
    - Create, schedule, and monitor many kinds of workflow
    - Based on Python

### How to run Apache Airflow in Python Environment
1. Check the python version `python --version` [This demo is based on Python 3.10.10]
2. Create the python environment
    ```
    python -m venv py_env
    ```
    py_env = name of the environment folder
3. Activate the python environment
    ```
    Windows: source py_env/Scripts/activate
    MacOS: source py_env/bin/activate
    ```
4. Go to https://github.com/apache/airflow/#installing-from-pypi, click `Installing from PyPI`, and grab this code
    ```
    pip install 'apache-airflow==2.5.1' \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-3.7.txt"
    ```
    Change constraints-3.7.txt to the python version you are using (Example: constraints-3.10.txt)

## FIXES
    As of today(Feb 20, 2023), Airflow does not support Python 3.11  
    Download the different python version and use that python to create virtual environment  
    Check https://www.youtube.com/watch?v=-TZfH7r33CQ for detail
    
    ${Different_Python_Directory} -m venv {VENV Name}
   