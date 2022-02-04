# dbt_project_cutter
Based on the requirements of DBT project structure, best practices, and code and naming conversion. This app is working for initial and setup a new project branch from main, if main existing. otherwise, it will create a new project.

## How to run it.

### Run python script
```python
git clone https://github.com/cove9988/dbt_project_cutter.git
cd dbt_project_cutter
python dbt_project_cutter.py

```
### Input parameters:
    User Name: [your name as creator]
    Repo Local Directory: [absolute path in your local e.g /my_dbt_test_project/ ]
    DBT Fork URL: [your forked repo from project, e.g https://github.com/yourname/project/]
    Project Name: [your new dbt project, e.g dbt_test]
    Data Domain: [which Data Domain the project belongs to, e.g. data_domain]
    Source Schema: [your data source from source layer. e.g. schema_name]

## Folder File Sturcture
project_root_folder/data_domain/project/

                                                   readme.md
                                                   dbt_project.yml
                                                   profiles.yml
                                                   packages.yml
                                                   dbt_modules/ (this folder copied from master, developer cannot change anything, READONLY)
                                                   models/
                                                   models/dbt_curated_source/schema_name/
                                                                                       _schema_name_source.yml (source list file)
                                                   snapshots/dbt_curated_source/project_root_folder/
                                                                                            data_domain/schema_name/sample.sql
                                                                                            data_domain/schema_name/sample.yml
                                                   macros/tests/
                                                                sample.sql
                                                   macros/other_test/
                                                                    sample.sql
                                                   data/
                                                   archived/
                                                   logs/ (developer local folder)
                                                   targets/ (developer local folder)


## Steps:
1. check & verify input parameter
2. mkdir repo directory and cd to the directory
3. git clone project_root_folder
4. git checkout project_name based on master
5. setup remote pull/push and create remote branch
6. create new project folder sturcture 
7. copy initial/example files into the new project
8. setup dbt venv/docker? 
9. open the project readme.md


