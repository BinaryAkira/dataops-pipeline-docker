"""
Runner module for the validation stage of the data pipeline.

This module:
- Loads the processed dataset
- Applies the Pandera validation schema
- Logs validation success or failure

It exposes a single public function: run_validate().
"""

from src.utils.logger import get_logger
from src.validate.validate import load_processed, validate

logger = get_logger(__name__)


def run_validate() -> None:
    """
    Execute the validation step.

    This function:
    - Loads the processed CSV file
    - Validates it against the Pandera schema
    - Logs the validation outcome
    """
    logger.info("Starting validation step")
    df = load_processed()
    validate(df)
    logger.info("Validation successful — processed data is valid.")
