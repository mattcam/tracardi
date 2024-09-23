import json
import os

from tracardi.exceptions.log_handler import get_logger

logger = get_logger(__name__)


def load_json(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError as e:
            logger.error(f"Predefined {file_path} exists but could not be parsed as JSON file. Details: {str(e)}")
            return None
    else:
        return None


def pre_config_file_loader(file_path):
    content = load_json(file_path)
    if isinstance(content, str):
        try:
            content = json.loads(content)
        except json.decoder.JSONDecodeError as e:
            logger.error(f"Predefined {file_path} exists but could not be parsed as JSON file. Details: {str(e)}")
            return None
    logger.info(f"Preconfiguration file `{file_path}` loaded with {len(content) if content else 'no'} definitions.")
    return content


def load_file_to_dict(file_path: str) -> dict[str, str]:
    my_dict = {}

    if not os.path.exists(file_path):
        return my_dict

    # Open the file in read mode
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace and split only on the first colon
            key_value = line.strip().split(':', 1)

            if len(key_value) == 2:
                key, value = key_value
                my_dict[key.strip()] = value.strip()
            else:
                logger.error(f"Skipping invalid line in tenant-aliases.txt: {line.strip()}")

    return my_dict
