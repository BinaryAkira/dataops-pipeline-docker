"""
Runner module for the ingestion stage of the data pipeline.

This module:
- Coordinates the ingestion workflow
- Logs progress and completion status
- Calls the underlying ingestion logic functions

It exposes a single public function: run_ingest().
"""

from src.ingest.ingest import fetch_pokemon, save_raw
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_ingest() -> None:
    """
    Execute the ingestion step.

    This function:
    - Fetches Pokémon data from the API
    - Saves the raw JSON response to disk
    - Logs progress and completion status
    """
    logger.info("Starting ingestion step")
    data = fetch_pokemon(limit=20)
    path = save_raw(data)
    logger.info(f"Ingestion complete: saved to {path}")
