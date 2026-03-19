"""
Validation module for enforcing schema checks on processed Pokémon data.

This module:
- Loads the processed CSV output
- Applies a Pandera schema to ensure structural correctness
- Logs validation success or raises errors on failure
"""

from pathlib import Path

import pandas as pd
import pandera as pa
from pandera import Check, Column, DataFrameSchema

from src.utils.logger import get_logger

logger = get_logger(__name__)

PROCESSED_PATH = Path("data/processed/pokemon_processed.csv")

# Modern Pandera schema (compatible with current versions)
pokemon_schema = DataFrameSchema(
    {
        "name": Column(pa.String, nullable=False),
        "url": Column(pa.String, nullable=False),
    },
    strict=True,
)


def load_processed(path: Path = PROCESSED_PATH) -> pd.DataFrame:
    """
    Load the processed Pokémon CSV file from disk.

    Args:
        path (Path): Path to the processed CSV file.

    Returns:
        pd.DataFrame: DataFrame containing processed Pokémon records.
    """
    return pd.read_csv(path)


def validate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate the processed Pokémon DataFrame using the defined schema.

    Args:
        df (pd.DataFrame): DataFrame to validate.

    Returns:
        pd.DataFrame: The validated DataFrame (unchanged if valid).

    Raises:
        pandera.errors.SchemaError: If the DataFrame does not match the schema.
    """
    return pokemon_schema.validate(df)
