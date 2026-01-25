
import os
import yaml
from pathlib import Path
from functools import lru_cache # Cache config so it’s loaded once only:
from dotenv import load_dotenv; load_dotenv()

CONFIG_FILE_PATH= os.getenv("CONFIG_FILE_PATH")

@lru_cache
def load_config_file(filepath: Path) -> dict:
    try:
        with open(filepath, 'r') as file:
            config_data = yaml.safe_load(file)
        return config_data
    except yaml.YAMLError as exc:
        print(f"Error reading YAML file: {exc}")
        return None
    except FileNotFoundError:
        print(f"Error: The file '{str(filepath)}' was not found.")
        return None


def load_config(*keys, default=None):

    config = load_config_file(filepath=CONFIG_FILE_PATH)
    value = config

    for key in keys:
        if not isinstance(value, dict) or key not in value:
            if default is not None:
                return default
            raise KeyError(f"Config key not found: {' -> '.join(keys)}")
        value = value[key]  
    return value      

print(load_config("model", "key"))


