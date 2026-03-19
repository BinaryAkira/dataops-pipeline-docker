"""
Tests for validation logic.

Functions tested:
- load_processed : test_load_processed_reads_csv
- validate : test_validate_passes_with_valid_schema
- validate : test_validate_fails_missing_column
- validate : test_validate_fails_wrong_type
"""

from pathlib import Path

import pandas as pd
import pytest
from pandera.errors import SchemaError

from src.validate.validate import load_processed, validate


class TestValidate:
    """
    Test suite for validation module functions.
    """

    def test_load_processed_reads_csv(self, tmp_path):
        """
        test_load_processed_reads_csv:
        Ensures load_processed correctly reads a CSV file into a DataFrame.
        """
        test_file = tmp_path / "processed.csv"
        df_expected = pd.DataFrame([{"name": "pikachu", "url": "http://pokeapi.co/25"}])
        df_expected.to_csv(test_file, index=False)

        df_loaded = load_processed(path=test_file)

        assert isinstance(df_loaded, pd.DataFrame)
        assert df_loaded.iloc[0]["name"] == "pikachu"

    def test_validate_passes_with_valid_schema(self):
        """
        test_validate_passes_with_valid_schema:
        Ensures validate() returns the DataFrame unchanged when schema is valid.
        """
        df = pd.DataFrame([{"name": "bulbasaur", "url": "http://pokeapi.co/1"}])

        validated_df = validate(df)

        assert isinstance(validated_df, pd.DataFrame)
        assert validated_df.equals(df)

    def test_validate_fails_missing_column(self):
        """
        test_validate_fails_missing_column:
        Ensures validate() raises SchemaError when required columns are missing.
        """
        df = pd.DataFrame([{"name": "charmander"}])  # missing "url"

        with pytest.raises(SchemaError):
            validate(df)

    def test_validate_fails_wrong_type(self):
        """
        test_validate_fails_wrong_type:
        Ensures validate() raises SchemaError when column types are incorrect.
        """
        df = pd.DataFrame(
            [{"name": 123, "url": "http://pokeapi.co/4"}]  # name should be string
        )

        with pytest.raises(SchemaError):
            validate(df)
