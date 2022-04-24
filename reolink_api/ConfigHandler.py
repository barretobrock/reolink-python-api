import io
from typing import (
    Dict,
    Optional
)
from loguru import logger
import yaml


class ConfigHandler:
    camera_settings = {}

    @staticmethod
    def load() -> Optional[Dict]:
        try:
            stream = io.open("config.yml", 'r', encoding='utf8')
            data = yaml.safe_load(stream)
            return data
        except Exception as e:
            logger.error("Config Property Error\n", e)
        return None
