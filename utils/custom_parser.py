import json
from pathlib import Path

configFile = "automation.json"
configFolder = "config"

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(configFolder).joinpath(configFile)

if CONFIG_FILE.is_file():
    with open(CONFIG_FILE, "r") as file:
        config = json.load(file)
    #print("Loaded configuration:", config)  # Debugging line
else:
    raise FileNotFoundError(f"Configuration file not found: {CONFIG_FILE}")


def getConfig(section, attribute):
    value = config[section][attribute]
    #print(f"Retrieving config for section: {section}, attribute: {attribute}, value: {value}")  # Debugging line
    return value
