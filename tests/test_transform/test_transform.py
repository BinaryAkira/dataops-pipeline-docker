"""
Tests for transformation logic.

Functions tested:
- load_raw : test_load_raw_reads_json
- extract_records : test_extract_records_parses_results
- extract_records : test_extract_records_empty_results
- save_processed : test_save_processed_creates_csv
"""

import json
from pathlib import Path

import pandas as pd

from src.transform.transform import extract_records, load_raw, save_processed


class TestTransform:
    """
    Test suite for transformation module functions.
    """

    def test_load_raw_reads_json(self, tmp_path):
        """
        test_load_raw_reads_json:
        Ensures load_raw correctly reads and parses a JSON file.
        """
        test_data = {"results": [{"name": "bulbasaur"}]}
        test_file = tmp_path / "raw.json"

        with test_file.open("w", encoding="utf-8") as f:
            json.dump(test_data, f)

        result = load_raw(path=test_file)

        assert isinstance(result, dict)
        assert result["results"][0]["name"] == "bulbasaur"

    def test_extract_records_parses_results(self):
        """
        test_extract_records_parses_results:
        Ensures extract_records returns simplified Pokémon records.
        """
        raw_data = {
            "results": [
                {"name": "charmander", "url": "http://pokeapi.co/4"},
                {"name": "squirtle", "url": "http://pokeapi.co/7"},
            ]
        }

        records = extract_records(raw_data)

        assert isinstance(records, list)
        assert len(records) == 2
        assert records[0]["name"] == "charmander"
        assert records[1]["url"] == "http://pokeapi.co/7"

    def test_extract_records_empty_results(self):
        """
        test_extract_records_empty_results:
        Ensures extract_records handles missing or empty results safely.
        """
        raw_data = {}  # no "results" key

        records = extract_records(raw_data)

        assert isinstance(records, list)
        assert len(records) == 0

    def test_save_processed_creates_csv(self, tmp_path):
        """
        test_save_processed_creates_csv:
        Ensures save_processed writes a DataFrame to CSV.
        """
        df = pd.DataFrame([{"name": "pikachu", "url": "http://pokeapi.co/25"}])

        filename = "processed_test.csv"
        output_path = tmp_path / filename

        # Override PROCESSED_DIR by writing directly to tmp_path
        saved_path = save_processed(df, filename=output_path.name)

        # save_processed writes into data/processed by default,
        # so we check that file exists there
        saved_path = Path("data/processed") / output_path.name
        assert saved_path.exists()

        loaded_df = pd.read_csv(saved_path)
        assert loaded_df.iloc[0]["name"] == "pikachu"
