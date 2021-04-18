import importlib
import logging
from sys import stdout

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(stdout))

text_pages = []
i = 1
while True:
    try:
        text_pages.append(
            importlib.import_module(f".p{i}", "text"))
        i += 1
    except ImportError as e:
        logger.info(f"Reached page {i-1}")
        break


def text():
    return [p.honbun for p in text_pages]
