# Apache Airflow

Based on https://www.youtube.com/watch?v=K9AnJ9_ZAXE
Based on Airflow version 2.0
<br><br/>

## What is Apache Airflow?
- Open-source workflow management platform
- Create, schedule, and monitor many kinds of workflow
- Based on Python
<br><br/>

## How to Install and run Apache Airflow (Docker)
Download Docker in your machine

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#running-airflow-in-docker

To get yaml file, run this command
`curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml'`

To run Airflow locally in docker:
  1. Change AIRFLOW_CORE_EXECUTOR: CeleryExecutor -> LocalExecutor
  2. Comment out the AIRFLOW_CELERY_RESULT_BACKEND and AIRFLOW_BROKER_URL (Comment out the Redis)
      *Redis is necessary for celery
  3. Comment out all the Redis dependencies and definition (Line 71 and Line 91)
  4. Comment out worker and flower as well (Line 132 and Line 261)
  5. Make directories for dags, logs and plugin  
      `mkdir -p ./dags ./logs ./plugins`  
      `echo -e "AIRFLOW_UID=$(id -u)" > .env` - only neccessary when you are using Linux
  6. Run docker command
      $ docker compose up airflow-init

      If the run is successful, you will see a message like this:
        
        airflow-init_1       | Upgrades done
        airflow-init_1       | Admin user airflow created
        airflow-init_1       | 2.5.1
        start_airflow-init_1 exited with code 0
  7. Start the service
      `docker compose up -d`
      `-d` is to run the service in detached mode, running containers in background
  8. run this command to see the which containers are running:
      $ docker ps

Check the OS folder for deatil (MacOS and Windows included)
<br><br/>

## Manage Workflows
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
<br><br/>

## Task Lifecycle
- no_status: Scheduler created empty task instance
- scheduled: Scheduler determined task instance needs to run
- upstream_failed: The task's upstream task failed
- skipped: Task is skipped
- queued: Scheduler sent task to executor to run on the queue
- running: Worker picked up a task and is now running it
- success: Task completed without an error
- failed: Task failed
- shutdown: Task run has been shutdown
- up_for_retry: Rerun the task
- up_for_reschedule: reschedule task every certain time interval

Successful Task Lifecycle Example
  - no_status -> Scheduler[scheduled] -> Executor[queued] -> Worker[running] -> success
<br><br/>

## Cron Expression
A CRON expression is a string comprising five fields separated by white space that represents a set of times
  - Normally as a schedule to execute some routine
  https://youtu.be/K9AnJ9_ZAXE?t=3729 <- *Write the table later
## FIXES
1.  As of today(Feb 20, 2023), Airflow does not support Python 3.11  
    Download the different python version and use that python to create virtual environment  
    Check https://www.youtube.com/watch?v=-TZfH7r33CQ for detail

    ${Different_Python_Directory} -m venv {VENV Name}

2.  ModuleNotFoundError: No module named 'pwd'
    pwd is not available on Windows environment
    You can either use WSL or running the Airflow in a Docker container

3.  Airflow Dag status is Success, but task states Dag has yet to run
    The start date should be yesterday. If you set the start date as today or right now,
    which is always >= the dag_run start_date. Choose the minimum date of your runs,
    and if you don't have one, you can use the yesterday date
    Check https://stackoverflow.com/questions/73622833/airflow-dag-status-is-success-but-task-states-dag-has-yet-to-run