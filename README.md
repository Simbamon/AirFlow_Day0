# Apache Airflow

Based on [this video](https://www.youtube.com/watch?v=K9AnJ9_ZAXE)  
Based on Airflow version 2.0
<br><br/>

## What is Apache Airflow?
- Open-source workflow management platform
- Create, schedule, and monitor many kinds of workflow
- Based on Python
<br><br/>

## How to Install and run Apache Airflow (Docker)
[Download](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#running-airflow-in-docker) Docker in your machine

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

## Installing Python Packages

|      | Extending | Customizing|
|:-----|:----------|:--------|
| Can be built without airflow sources | Yes | No |
| Uses familiar 'FROM' pattern of image building | Yes | No |
| Requires only basic knowledge about images | Yes | No |
| Builds quickly | Yes | No |
| Produces image heavily optimized for size | No | Yes |
| Can build from custom airflow sources (forks) | No | Yes |
| Can build on air-gapped environment | No | Yes |

Image Extending:
  1. Write the Dockerfile
  2. Build that Dockerfile and tag it  
     `docker build {DOCKERFILE_LOCATION} --tag {EXTENDED_IMAGE_TAG}`
  3. In docker yaml file, change the `AIRFLOW_IMAGE_NAME` to the image you just built with Dockerfile  
     `image: ${AIRFLOW_IMAGE_NAME:-{EXTENDED_IMAGE_TAG}}` <- Check docker-compose.yaml line 49
  4. Restart the Airflow  
     `docker compose up -d --no-deps --build airflow-webesrver airflow-scheduler`

Image Customizing:
  1. Grab [Apache Airflow](https://github.com/apache/airflow) git repository to your machine (Different directory)
     `git clone https://github.com/apache/airflow`
  2. In docker-context-files directory, make `requirements.txt` file  
      in requirements.txt file(Example):
      ```
      scikit-leran==0.24.2
      matplotlib==3.3.3
      ```
  3. Build the Dockerfile from Github repo  
     `docker build {GITHUB_REPO_DOCKERFILE_LOCATION} --build-arg AIRFLOW_VERSION='{AIRFLOW_VERSION}' --tag {CUSTOMIZED_IMAGE_TAG}`
  4. Come back to original docker yaml file, change the `AIRFLOW_IMAGE_NAME` to the image you just built from Github repo  
     `image: ${AIRFLOW_IMAGE_NAME:-{CUSTOMIZED_IMAGE_TAG}}` <- Check docker-compose.yaml line 49
  5. Restart the Airflow  
     `docker compose up -d --no-deps --build airflow-webesrver airflow-scheduler`
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

| Preset | Definition | Cron|
|:-----|:---------|:---|
| `None` | Don't scehdule, use for exclusively "externally triggered" DAGs | |
| `@once` | Schedule once and only once | |
| `@hourly` | Run once an hour at the beginning of the hour | `0 * * * *` |
| `@daily` | Run once a day at midnight | `0 0 * * *` |
| `@weekly` | Run once a week at midnight on Sunday morning| `0 0 * * 0` |
| `@monthly` | Run once a month at midnight of the first day of the month| `0 0 1 * *` |
| `@yearly` | Run once a year at midnight of January 1 | `0 0 1 1 *` |


## FIXES
1.  As of today(Feb 20, 2023), Airflow does not support Python 3.11  
    Download the different python version and use that python to create virtual environment  
    Check [this video](https://www.youtube.com/watch?v=-TZfH7r33CQ) for detail

    ${Different_Python_Directory} -m venv {VENV Name}

2.  ModuleNotFoundError: No module named 'pwd'
    pwd is not available on Windows environment
    You can either use WSL or running the Airflow in a Docker container

3.  Airflow Dag status is Success, but task states Dag has yet to run
    The start date should be yesterday. If you set the start date as today or right now,
    which is always >= the dag_run start_date. Choose the minimum date of your runs,
    and if you don't have one, you can use the yesterday date
    Check this [Stackoverflow case](https://stackoverflow.com/questions/73622833/airflow-dag-status-is-success-but-task-states-dag-has-yet-to-run)