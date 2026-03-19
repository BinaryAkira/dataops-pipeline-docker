"""
Defines the pipeline workflow (ingest → transform → validate).

This module:
- Coordinates the execution of all pipeline stages
- Provides a single entry point for running the full workflow
- Handles top‑level logging and error reporting
"""

from src.ingest.ingest_main import run_ingest
from src.transform.transform_main import run_transform
from src.utils.logger import get_logger
from src.validate.validate_main import run_validate

logger = get_logger(__name__)


def run_pipeline() -> None:
    """
    Run the full data pipeline with top‑level error handling.

    This function:
    - Executes ingestion, transformation, and validation in sequence
    - Logs the start and end of the pipeline run
    - Captures and logs any unexpected exceptions

    Raises:
        Exception: Propagates any unhandled exception after logging it.
    """
    logger.info("Pipeline run started")

    try:
        run_ingest()
        run_transform()
        run_validate()
        logger.info("Pipeline run completed successfully")

    except Exception as e:
        logger.error(f"Pipeline run failed: {e}", exc_info=True)
        raise
