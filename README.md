# DiscreteMathFinalProject
A fuzzy logic system to control green light duration based on traffic density and waiting time.


## Project structure

```
fuzzy_traffic/
├── requirements.txt      # numpy, matplotlib, scikit-fuzzy
├── fuzzy_system.py       # variables, membership functions, rules, controller
├── plots.py              # membership plots + 3D surface
├── main.py               # takes user input, prints the result, shows plots
├── check_setup.py        # test to see if all imports have been installed successfully
└── README.md             # explain your design choices
```

Fuzzy logic has been kept separate from the plotting and the input code to make it easy to explain and test.

## Setup

### Requirements

- **Python 3.14.5** (this exact version is required)
- Git

Check your Python version:

```bash
python --version
```

The output should be `Python 3.14.5`. On macOS/Linux you may need to use `python3` instead of `python` in every command below.

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd fuzzy_traffic
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

| OS / Shell          | Command                          |
| ------------------- | -------------------------------- |
| Windows (PowerShell) | `venv\Scripts\Activate.ps1`     |
| Windows (cmd)        | `venv\Scripts\activate.bat`     |
| macOS / Linux        | `source venv/bin/activate`      |

When activated, `(venv)` appears at the start of your terminal prompt.

> **PowerShell note:** if activation is blocked by an execution policy error, run
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify the installation

```bash
python check _setup.py
```

If version numbers prints without errors, the setup is complete.

### Troubleshooting

- **`ModuleNotFoundError: No module named 'skfuzzy'`**: the virtual environment is not active, or the packages were installed into a different Python. Check for `(venv)` in your prompt and re-run step 4.
- **Wrong Python version**: install Python 3.14.5 from [python.org](https://www.python.org/downloads/) and recreate the virtual environment (delete the `venv` folder, then repeat from step 2).