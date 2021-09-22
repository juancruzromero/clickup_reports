import yaml
from pathlib import Path

__config = None

base_path = Path(__file__).parent
file_path = (base_path / 'config.yaml')

__file = str(file_path)

def config():
    global __config
    if not __config:
        with open(__file, mode='r') as f:
            __config = yaml.load(f, Loader=yaml.FullLoader)
    return __config