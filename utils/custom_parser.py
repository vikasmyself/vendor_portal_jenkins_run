import json
import os
from pathlib import Path

configFile = "automation.json"
configFolder = "config"

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(configFolder).joinpath(configFile)

if CONFIG_FILE.is_file():
    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)
else:
    raise FileNotFoundError(f"Configuration file not found: {CONFIG_FILE}")

def getConfig(section, attribute):
    value = config[section][attribute]
    # Replace environment variables if present
    if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
        env_var = value[2:-1]
        value = os.getenv(env_var, value)
    return value
