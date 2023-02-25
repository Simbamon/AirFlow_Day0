# Windows(WSL) Setup

### How to install WSL Ubuntu on your machine
1. In search, type 'Turn Windows features on or off'

2. In the box, check these two:  
    - Virtual Machine Platform
    - Windows Subsystem for Linux<br/><br/>
  
3. Restart the PC and download Ubuntu in Microsoft Store

4. go to https://aka.ms/wsl2kernel and download the Linux kernel update package
   Install the software you downloaded in that page

5. Set up Username and Password in Ubuntu

### How to run Apache Airflow in WSL Ubuntu (Windows)
1. In Ubuntu environment, type `python3 --version` to verify your python version (> 3.6)

2. Run these commands to add packages that will help pip work
   - `sudo apt-get install software-properties-common`
   - `sudo apt-add-repository universe`
   - `sudo apt-get update` <br/><br/>

3. Install pip with this command
   - `sudo apt-get install python3-pip`<br/><br/>

4. Run these commands to install Apache Airflow
   - `export SLUGIFY_USES_TEXT_UNIDECODE=yes`
   - `pip3 install apache-airflow`<br/><br/>

5. Initiate Airflow DB (SQLite)
   - `airflow db init`<br/><br/>

6. Run the Airflow on local server:
   - `airflow webserver -p {PORT_NUMBER}`

## Fixes
    1. The scheduler does not appear to be running. 
       The DAGs list may not update, and new tasks will not be scheduled.
       
       Solution:
       In a new terminal, run:
       $ airflow scheduler
       and leave it open