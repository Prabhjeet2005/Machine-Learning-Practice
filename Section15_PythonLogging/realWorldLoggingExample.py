"""
# REAL WORLD EXAMPLE
- .StreamHandler() => Puts all info in the file
"""

import logging

logger = logging.getLogger("ArithmaticApp")
logger.setLevel(level=logging.DEBUG)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(filename="realWorld_Example.log"),
        logging.StreamHandler(),
    ],
)


def add(a, b):
    result = a + b
    logger.debug(f"Addition of {a}+{b}={result}")
    return result


def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Division of {a}/{b}={result}")
        return result
    except Exception as e:
        logger.error(f"Error Occured While Dividing: {e}")


add(2, 3)
divide(10, 2)
divide(10, 0)
