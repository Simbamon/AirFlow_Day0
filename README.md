# Apache Airflow

Based on https://www.youtube.com/watch?v=K9AnJ9_ZAXE
Based on Airflow version 2.0

### What is Apache Airflow?
    - Open-source workflow management platform
    - Create, schedule, and monitor many kinds of workflow
    - Based on Python

## FIXES
    1.  As of today(Feb 20, 2023), Airflow does not support Python 3.11  
        Download the different python version and use that python to create virtual environment  
        Check https://www.youtube.com/watch?v=-TZfH7r33CQ for detail

        ${Different_Python_Directory} -m venv {VENV Name}
   
    2.  ModuleNotFoundError: No module named 'pwd'
        pwd is not available on Windows environment
        You can either use WSL or running the Airflow in a Docker container