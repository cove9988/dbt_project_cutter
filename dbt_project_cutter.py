from json.tool import main
import os
from datetime import datetime

def input_dialog():
    user_name = input('User Name:')
    repo_local_directory = input('Repo Local Directory (e.g /temp/): ')
    dbt_fork_url = input(
        'DBT Fork URL(e.g https://github.com/yourname/project/:')
    project_name = input('Project Name: ')
    data_domain = input('Data Domain (e.g data_domain or new one): ')
    source_schema = input('Source schema (e.g schema_name): ')
    print(
        f"""\n---------Your Initial Setup----------------\n User Name: {user_name}\nRepo Local Directory: {repo_local_directory}\n DBT Fork URL: {dbt_fork_url}\n Project Name: {project_name}\n Data Domain: {data_domain}\n Source Schema: {source_schema}\n\n""")

    yn = input('Do you want to execute project initial:(y/n)')
    if yn.lower() != "y":
        exit()
    return [user_name, repo_local_directory, dbt_fork_url, project_name.lower(), data_domain.lower(), source_schema.lower()]


def create_folder(folder_path):
    print(f'creating folder: {folder_path}')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def clone_dbt_repo(repo_local_directory, dbt_fork_url):
    os.chdir(repo_local_directory)
    print(f'clone repo {dbt_fork_url} to {repo_local_directory}')
    os.system('git clone ' + dbt_fork_url)

def replace_in_file(_s, _d):
    with open(_s, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('{{ creator }}', user_name)
    filedata = filedata.replace('{{ date }}', create_date)
    filedata = filedata.replace('{{ project_name }}', project_name)
    filedata = filedata.replace('{{ schema }}', project_name)
    filedata = filedata.replace('{{ profile }}', "profile")

    with open(_d, 'w') as file:
        file.write(filedata)


args = input_dialog()
user_name = args[0]
repo_local_directory = args[1]
dbt_fork_url = args[2]
project_name = args[3]
data_domain = args[4]
source_schema = args[5]

create_date = datetime.today().strftime('%Y-%m-%d')
src = os.path.join(os.path.abspath(os.getcwd()), 'project_temp')
print(f'project_temp: {src}')
folders = [
    "macros/tests/",
    "logs/",
    "data/",
    "archived/",
    f"models/dbt_curated_source/{source_schema}/",
    "snapshots/dbt_curated_source/",
    "targets/"
]

files = [
    "lazypush.sh",
    ".gitignore",
    "dbt_project.yml",
    "profiles.yml", "packages.yml",
    "readme.md",
    "macros/tests/example.sql",
    "models/dbt_curated_source/schema/_schema.yml",
    "snapshots/dbt_curated_source/sample.yml",
    "snapshots/dbt_curated_source/sample.sql",
]

create_folder(repo_local_directory)
clone_dbt_repo(repo_local_directory, dbt_fork_url)
p = os.path.join(repo_local_directory, 'project_root_folder')
print(f'cd to folder: {p}')
os.chdir(p)
print(f'connect to remote : {dbt_fork_url}')
os.system('git remote add upstream ' + dbt_fork_url)
cmd = f'git checkout -b  {project_name}'  # upstream/{project_name}'
print(cmd)
os.system(cmd)

for f in folders:
    _p = os.path.join(p, data_domain, project_name, f)
    print(f'create folder {_p}')
    create_folder(_p)

for f in files:
    _s = os.path.join(src, f)
    _p = os.path.join(p, data_domain, project_name,
                      f).replace('schema', source_schema)
    print(f"copy file: {_s} to {_p}")
    replace_in_file(_s, _p)

cmd = f"git push --set-upstream origin {project_name}"
os.system(cmd)
cmd = './lazypush.sh "initial project {project_name}"'
os.system(cmd)
