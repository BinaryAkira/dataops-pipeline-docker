"""
Top‑level entrypoint for running the data pipeline.

This module:
- Imports the pipeline controller
- Provides a main() function for execution
- Allows the pipeline to be run directly via `python main.py`
"""

from src.pipeline import run_pipeline


def main() -> None:
    """
    Main entrypoint for executing the full data pipeline.

    This function simply delegates to the pipeline controller, ensuring
    a clean and minimal top‑level script.
    """
    run_pipeline()


if __name__ == "__main__":
    main()
