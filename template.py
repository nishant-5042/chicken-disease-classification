import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
#it will get the current time and the logging message


project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep", #we need this at the time of deployment. CI/CD command
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init.py",
    f"src/{project_name}/utils/__init.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"


]

for filepath in list_of_files:
    filepath = Path(filepath) #this is used to make it compatible with windows as it uses \
    filedir, filename = os.path.split(filepath) #splits path into dir and filename

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) #exist_ok=True will not create a dir if it already exists
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already existing")

