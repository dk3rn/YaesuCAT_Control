import json


def read_config(file_path):
    """
    Liest das JSON-File mit Button-Konfigurationen ein.

    :param file_path: in the same directory just: "ctrl_config.json"
    :return: list of buttons
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config.get('buttons', [])
