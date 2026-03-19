"""
Runner module for the transformation stage of the data pipeline.

This module:
- Loads raw data
- Applies transformation logic
- Saves the processed dataset
- Logs progress and completion status

It exposes a single public function: run_transform().
"""

import pandas as pd

from src.transform.transform import extract_records, load_raw, save_processed
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_transform() -> None:
    """
    Execute the transformation step.

    This function:
    - Loads raw JSON data from disk
    - Extracts relevant Pokémon fields
    - Converts the records into a pandas DataFrame
    - Saves the processed dataset to data/processed/
    """
    logger.info("Starting transformation step")
    raw = load_raw()
    records = extract_records(raw)
    df = pd.DataFrame(records)
    path = save_processed(df)
    logger.info(f"Transformation complete: saved to {path}")
