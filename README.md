FastAPI Base Scaffolding
=============================================================================

![GitHub](https://img.shields.io/github/license/blevinscm/fastapi-scaffold-base) ![GitHub contributors](https://img.shields.io/github/contributors/blevinscm/fastapi-scaffold-base) ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/blevinscm/fastapi-scaffold-base?include_prereleases)


<img align="center" width="400" src="./images/fastapi-logo.png"/>

#### Project Lead : | [Chris Blevins](https://github.com/blevinscm)

Thanks to [Sebastián Ramírez @tiangolo](https://github.com/tiangolo) we have the wonderful FastAPI package for developing applications and APIs. Anyone looking at this repository is most likely familiar with the project.  If not I highly recommend Reading the Docs. 

### [FastAPI](https://fastapi.tiangolo.com/)

While learning and using FastAPI I have often needed/wanted lightweight project scaffolding.  The project generators and scaffolding projects in the FastAPI ecosystem have been either too deterministic and too big or not deterministic enough for me.  

This uis how I set up a new FastAPI project.  I hope this is helpful. 

## Dependencies: 

  |Package | Note |
  |:----|:------------|
  |[Python 3.6+](https://www.python.org/downloads/) | This project uses Python 3.9 but should work on Python 3.6+. |
  |[pip](https://pip.pypa.io/en/stable/installing/) | I use Pip for pacakage management and pin versions.  I don't think anything more complex than that is necessary.  Adjust for your flow. |
  |[virtualenv](https://virtualenv.pypa.io/en/stable/installation.html) | Again I am not trying to get fancy.  ```py -m pip install virtualenv```|
  |[FastAPI](https://github.com/tiangolo/fastapi) |  I usally install all related packages in my venv. ```pip install fastapi[all]```  |
  |[Docker](https://www.docker.com/products/docker-desktop) | (Optional) I use it to startup DBs instead of installing directly. Will make your life easier. There are also images for bundled FastAPI environmets on Docker Hub.
  |[ODMantic](https://art049.github.io/odmantic/) | (Optional) ORM for MongoDB with great model and document support. |
  |[TortoiseORM](https://tortoise-orm.readthedocs.io/en/latest/) | (Optional) ASYNC ORM that works well with FastAPI and Postgres/MySQL


## Get Started

1. Install Python if not already installed

2. Clone this repository: 
   ```git
    git clone https://github.com/blevinscm/fastapi-scaffold-base.git
    ```

3. Install virtualenv
    ```zsh
    py -m pip install --user virtualenv
    ```
4. CD into project directory
    ```zsh
        cd dir 
    ```
5. Create virtual environment
    ```bash
    py -m venv env
    ```
6. Activate virtual environment
    ```bash
    source .\env\bin\activate
    ```
7. Install pip dependencies (This will install all FastAPI Modules.  If you do not want [all] plese adjust the req file.)
    ```bash
    pip install -r requirements.txt
    ```
8. (Optional) Pull latest Mongo image and create mongo container for dev purposes
    ```docker
    docker pull mongo:latest
    docker run --rm --net=host mongo
    ```
9. Set execute permissions on either win-start-FastApi.ps1 or nix-start-FastAPI

10. Run the start-FastAPI for your system 

11. Go to https://localhost:8000/docs to see your FastAPI documentation and explore the sample docs. 


12. Close your FastAPI terminal and your Mongo Terminal.

11. To get out of venv
    ```bash
    deactivate
    ```
