## Installation

### 1. Clone this repository

bash
git clone https://github.com/Examon-AI/quesgen-v.git
cd quesgen-v


### 2. Install Poetry

On macOS, a common approach is:
bash
brew install pipx
pipx install poetry


> For other platforms or methods, see [Poetry's official docs](https://python-poetry.org/docs/#installation).

### 3. Initialize the project with Poetry

1. **Install dependencies** and create a virtual environment:

   bash
   poetry install
   

2. **(Optional)** Confirm your new virtual environment:

   bash
   poetry env list
   poetry env info --path
   

---

## Virtual Environment Setup

If you're able to use `poetry shell`, do so:
bash
poetry shell

If you receive an error that the `shell` command does not exist, run your commands with:
bash
poetry run python <your_script>.py

or **manually activate** the environment:

1. Find the path of the Poetry venv:
   bash
   poetry env info --path
   
   Example output:
   
   /Users/<username>/Library/Caches/pypoetry/virtualenvs/quesgen-v-XXXX-py3.11
   
2. Activate it manually:
   bash
   source /Users/<username>/Library/Caches/pypoetry/virtualenvs/quesgen-v-XXXX-py3.11/bin/activate
   

---

## Usage

Inside the `quesgen-v` project folder:

bash
# If you can use poetry shell:
poetry shell
python scripts/generate.py <template_id> <topic>

# Or directly with poetry run:
poetry run python scripts/generate.py <template_id> <topic>


- **Example**:
  bash
  poetry run python scripts/generate.py template1 "Biology"
  

This script will:
1. Load a JSON template from `quesgen_v/templates/<template_id>.json`  
2. Optionally filter PPQs (Past Paper Questions) from `quesgen_v/data/ppqs.csv`  
3. Generate a question, then store it in `quesgen_v/workspace/<template_id>/q_<n>.txt`

---

## Managing Dependencies

1. **Add a dependency**:
   bash
   poetry add requests
   
   This updates your `pyproject.toml` and `poetry.lock`.

2. **Remove a dependency**:
   bash
   poetry remove requests
   

3. **Upgrade** dependencies to latest allowed versions:
   bash
   poetry update
   

---

## Configuring VS Code

To get proper IntelliSense and import highlighting in Visual Studio Code:

1. **Install the official Python extension** in VS Code.
2. In the command palette (`Cmd + Shift + P` on macOS), select:
   - **Python: Select Interpreter**
   - Choose **Enter interpreter path...** (or **Find**/ **Browse**).
   - Point to Poetry's virtual environment Python, e.g.:
     
     /Users/<username>/Library/Caches/pypoetry/virtualenvs/quesgen-v-XXXX-py3.11/bin/python
     
3. VS Code should now recognize the environment and show correct import resolution.

---