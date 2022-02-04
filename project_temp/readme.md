# Project: {{ project_name }}

Team Member: {{ user_name }}

Project Period: {{ date }} -- 

Project Description: 


## DBT Project Development Guideline
1. [Overview](#Overview)
2. [Github Structure](#Github)
3. [Model](#Model)

### Overview
Project overview here

### Github Structure

GITHUB REPOSITORY: https://github.com/yourname/project/

DBT Projects will reside in the project_root_folder repository with the following folder structure:
    ![](../doc/project_root_folder.png)


### Model

•	Each model to be created MUST have their own .sql file and an associated .yml file with the same file name. The .yml file will be used to provide table and column descriptions as well as define schema and logical tests.

•	The name of the file must be lower case, do not include the schema name.

•	The file name should be self-explainable as possible.

•	Names should only use alphanumeric and underscore characters only.

•	Names should be singular as opposed to plurals. E.g. “shop” not “shops” as a table name.

•	File name must be 256 characters or less

•	Do not use MV or TB or VW prefixes (with dbt you can easily change between tables and views therefore prefixing is not necessary)

•	The name of the file will be the final object name create on the database.

•	In dbt_curated_source layer, name should be prefixed with the source system code . This is help avoid naming clashes and physically group together.

•	In dbt_integration_<data product> layer, prefix objects with the subject area of the content of the data. This is help avoid naming clashes and physically group together.

•	In dbt_consumption layer, 

    o	Prefix objects with the subject area of your stakeholder (ie. ). This is help avoid naming clashes and physically group together.

    o	Use dim and fact prefix where star schema is deployed (ie. dim_customer, fact_transaction)

•	Sources yaml file MUST be named as _<source_schema>_sources.yml (ie. _schema_name_sources.yml). The underscore at the front is order the file at the tope so it is easy to locate amongst model sql/yml files.
