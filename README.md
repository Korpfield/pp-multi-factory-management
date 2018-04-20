# 1. Getting started
## 1.1. Table of contents
<!-- TOC -->

- [1. Getting started](#1-getting-started)
    - [1.1. Table of contents](#11-table-of-contents)
    - [1.2. Workflow](#12-workflow)
    - [1.3. Installation](#13-installation)
        - [1.3.1. Virtual environment](#131-virtual-environment)
            - [1.3.1.1. Installation for Windows](#1311-installation-for-windows)
        - [1.3.2. Python](#132-python)
        - [1.3.3. Pip](#133-pip)
    - [1.4. Requirements](#14-requirements)
        - [1.4.1. Django](#141-django)
    - [1.5. Visual Studio Code](#15-visual-studio-code)
        - [1.5.1. Python extension](#151-python-extension)
        - [1.5.2. GitLens](#152-gitlens)
        - [1.5.3. Code Runner](#153-code-runner)

<!-- /TOC -->
## 1.2. Workflow
Use GitHub workflow
https://guides.github.com/introduction/flow/
Ie. branch each feature and open pull-request to merge to master. 

Rules:
- Anything in the `master` branch is always deployable!
- Branch your features from `master`
- Write clean commit messages and use descriptive branch names
- Open pull-request before merging to master
## 1.3. Installation
### 1.3.1. Virtual environment
All Python projects should be contained within isolated virtual environments. This allows you to work on specific project without worry of affecting other projects.

Virtualenvwrapper offers neat set of commands to help you manage your virtual environments.
https://virtualenvwrapper.readthedocs.io/en/latest/ 

#### 1.3.1.1. Installation for Windows
Guillermo López-Anglada has ported virtualenvwrapper to run under Microsoft’s PowerShell.
https://pypi.org/project/virtualenvwrapper-win/

### 1.3.2. Python
Install Python version 3.6.5
https://www.python.org/

### 1.3.3. Pip
>pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or pyvenv. Just make sure to upgrade pip.
https://pip.pypa.io/en/stable/installing/

## 1.4. Requirements
Install project requirements with
`pip install -r requirements.txt`

Note! Always add new project requirements to `requirements.txt` file with command
`pip freeze > requirements.txt`

### 1.4.1. Django
Django is installed with requirements.
Version 2.0.4 is used in this project.
See https://www.djangoproject.com/start/ to get started with Django.

## 1.5. Visual Studio Code
Visual Studio Code is one of the best free editors for Python (or any language). This section contains some tips for quickly configuring Visual Studio Code for Python projects, but feel free to use any editor you like.
https://code.visualstudio.com/docs/setup/setup-overview

### 1.5.1. Python extension
Install Visual Studio Code Python extension
https://code.visualstudio.com/docs/python/python-tutorial

### 1.5.2. GitLens
> GitLens supercharges the Git capabilities built into Visual Studio Code. It helps you to visualize code authorship at a glance via Git blame annotations and code lens, seamlessly navigate and explore Git repositories, gain valuable insights via powerful comparison commands, and so much more.

https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens

### 1.5.3. Code Runner
Run code snippet or code file for multiple language.
https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner
