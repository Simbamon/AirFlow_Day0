# Apache Airflow

Based on https://www.youtube.com/watch?v=K9AnJ9_ZAXE
Based on Airflow version 2.0

### What is Apache Airflow?
    - Open-source workflow management platform
    - Create, schedule, and monitor many kinds of workflow
    - Based on Python

### How to Install and use Apache Airflow
    Check the OS folder for deatil (MacOS and Windows included)

### Manage Workflows
    - Workflow 
      Sequence of tasks
      In Airflow, it is defined as DAG
    - DAG(Directed Acyclic Graph)
      Collection of all the tasks you want to run
      Organized in a way that reflects their relationships and dependencies
        - Task
          Defines a unit of work within a DAG
          Represented as a node in the DAG graph, written in Python
        - Operator
          Method used to achieve a specific thing
          While DAGs describe how to run a workflow, Operators determine what actually gets done by a task
          Example:
          1. BashOperator
          2. PythonOperator
          3. Customized Operator
    - Execution Date
      Logical date and time which the DAG Run, and its task instances are running for
    - Task Instance
      Run of a task at a specific point of time(Execution Date)
    - DAG Run
      Instantiation of a DAG, containing task instances that run for a specific Execution Date

## FIXES
    1.  As of today(Feb 20, 2023), Airflow does not support Python 3.11  
        Download the different python version and use that python to create virtual environment  
        Check https://www.youtube.com/watch?v=-TZfH7r33CQ for detail

        ${Different_Python_Directory} -m venv {VENV Name}
   
    2.  ModuleNotFoundError: No module named 'pwd'
        pwd is not available on Windows environment
        You can either use WSL or running the Airflow in a Docker container