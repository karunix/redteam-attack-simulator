Red Team Attack Simulator

CLI-based security simulation tool for practicing detection engineering concepts.

Current Features

SSH Brute Force simulation (MITRE T1110)

Human-readable output

JSON output mode

Unit tested

Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

Usage
python main.py ssh-bruteforce --user admin --attempts 10


JSON mode:

python main.py ssh-bruteforce --user admin --attempts 10 --json
