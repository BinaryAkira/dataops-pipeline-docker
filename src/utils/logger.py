"""
Shared logging configuration for the data pipeline.

This module:
- Creates a centralised logs/ directory
- Defines a consistent logging format
- Provides a helper function for retrieving configured loggers
"""

import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger with a consistent format.

    Args:
        name (str): Name of the logger, typically the module's __name__.

    Returns:
        logging.Logger: A configured logger instance with both file and
        console handlers attached.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is requested multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
