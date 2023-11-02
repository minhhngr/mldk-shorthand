# Managing Python Dependencies

## Key Differences

---

Feature                            | Pip   | Poetry    | Conda | Virtualenv | Pyenv |  
---                                | ---   | ---       | ---   | ---        | ---   |
Create virtual environments        | No    | Yes       | Yes   | Yes        | Yes   |
Manages dependencies               | No    | Yes       | Yes   | No         | No    |
Creates project files              | No    | Yes       | No    | No         | No    |
Handles packaging and distribution | No    | Yes       | Yes   | No         | No    |
Support multiple Python versions   | No    | No        | Yes   | No         | Yes   |
Command-line interface             | Yes   | Yes       | Yes   | Yes        | Yes   |
User-friendliness                  | Basic | Excellent | Good  | Good       | Good  |

* Need a simple and lightweight tool for managing dependencies, then Pip is a good choice.
* Need a solution that can handle environments and dependencies, then Pipenv is a good choice.
* Need a more comprehensive solution that can handle all aspects of your Python project lifecycle including packaging and distribution, then Poetry is a good choice.
* Need a mature tool that can manage multiple Python versions and other software packages, then Conda is a good choice.
* Need to create isolated Python environments, then Virtualenv is a good choice.
* Need to manage different Python versions on your system, then Pyenv is a good choice

## More References

* [Virtual Environments tutorial using Virtualenv and Poetry](https://serpapi.com/blog/python-virtual-environments-using-virtualenv-and-poetry/)
* [A comparison of various tools to manage Python packages and virtual environments](https://www.linkedin.com/pulse/comparison-various-tools-manage-python-packages-virtual-mukesh-kumar/)
* [Managing Python Dependencies](https://www.fuzzylabs.ai/blog-post/managing-python-dependencies)

---

## Pip

Pip is the official package manager for Python. It is a simple and lightweight tool that can be used to install and manage Python packages. Pip is a good choice if you are just getting started with Python, or if you need a basic tool for managing dependencies.

* [Pip documentation](https://pip.pypa.io/en/stable/)

### Pip CLI

```sh
 pip install ...
```

```sh
 pip install -r requirements.txt
 pip freeze > requirements.txt
 pip uninstall -r requirements.txt -y                  # In case installed via requirements.txt
```

```sh
"""
Clean up environment in python3, if forgot use virtual env
"""
# Unix/MacOS
 pip freeze | xargs pip uninstall -y
 pip freeze | grep -v "^-e"  | xargs pip uninstall -y  # In case have packages installed via VCS
 pip freeze | cut -d "@" -f1 | xargs pip uninstall -y  # Have packages installed directly from github/gitlab

# Windows
 pip freeze | ForEach-Object { pip uninstall -y $_ }
 pip freeze | ForEach-Object { if ($_ -notmatch "^-e") { pip uninstall -y $_ } }
 pip freeze | ForEach-Object { pip uninstall -y ($_.Split('@')[0]) }
```

### Pip Usage

1. Create virtual environment

```sh
 python3 -m venv venv
```

2. Install package manager

```sh
 pip install $Package
```

---

## Poetry

Poetry is a newer tool that is similar to Pipenv. It provides a more comprehensive solution for managing Python packages, including features for dependency management, packaging, and distribution. Poetry is a good choice if you need a tool that can handle all aspects of your Python project lifecycle.

* [Documentation](https://python-poetry.org/docs/)
* [Configuration](https://python-poetry.org/docs/configuration/)

### Poetry CLI

* [Poetry CLI](https://python-poetry.org/docs/master/cli/)

```sh
 poetry new <project-name>                                   # Create a new project
 poetry add <library>                                        # Add a new lib
 poetry remove <library>                                     # Remove a lib
 poetry update <library>                                     # Update a lib
 poetry run which python                                     # Get venv path
 poetry run python app.py                                    # Run app
 poetry run python -m unittest discover                      # Run tests
 poetry run test                                             # Run script
 poetry show                                                 # Show dependencies
 poetry show --tree
 poetry config --list                                        # List configuration
 poetry export -f requirements.txt --output requirements.txt # Export to requirements.txt file
 poetry env list                                             # shows the name of the current environment
 poetry env remove <current environment>
 poetry install                                              # will create a new environment using your updated configuration
```

### Poetry Usage

1. poetry config
    * ```poetry config virtualenvs.create true```
    * ```poetry config virtualenvs.in-project true```
2. poetry install
3. poetry shell

#### Example

```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["Your Name "]
readme = "README.md"

[tool.poetry.dependencies]
python = ">=3.10, <3.11"
pandas = "1.5.2"
sqlalchemy = "<=1.4.41"
zenml = {version = "0.35.0", extras = ["server"]}

[tool.poetry.group.test.dependencies]
pytest = "^6.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

#### Create script

1 - Edit ```pyproject.toml```

```toml
[tool.poetry.scripts]
test = 'scripts:test'
```

2 - Create a `scripts.py` file on the root directory of your project:

```python
import subprocess

def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover`
    """
    subprocess.run(
        ['python', '-u', '-m', 'unittest', 'discover']
    )

def run(command: list[str]):
    """Run the command transparently (as if it was in the same process).

    If an error occurs, exit with the corresponding return code.
    Prints all outputs to stdout.
    """
    result = subprocess.run(command, capture_output=True)
    print(result.stdout.decode('utf8'), end='')
    print(result.stderr.decode('utf8'), end='')
    if result.returncode != 0:
        exit(code=result.returncode)
```

3 - Run script:

```bash
poetry run test
```

### Poetry-Reference

---

## Conda

Conda is a more mature tool that has been around for longer. It is also more widely used, especially in the data science community. Conda can be used to manage multiple Python versions, as well as other software packages. This makes it a good choice if you need to use different versions of Python for different projects, or if you need to install software packages that are not available in the Python Package Index (PyPI).

* [Conda documentation](https://docs.conda.io/en/latest/)

### Conda CLI

```sh
 conda install ...
```

### Conda-Reference
