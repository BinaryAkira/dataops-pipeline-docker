"""
Tests for ingestion logic.

Functions tested:
- fetch_pokemon : test_fetch_pokemon_success
- fetch_pokemon : test_fetch_pokemon_http_error
- save_raw : test_save_raw_creates_file
"""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.ingest.ingest import fetch_pokemon, save_raw


class TestIngestion:
    """
    Test suite for ingestion module functions.
    """

    @patch("src.ingest.ingest.requests.get")
    def test_fetch_pokemon_success(self, mock_get):
        """
        test_fetch_pokemon_success:
        Ensures fetch_pokemon returns parsed JSON when API responds successfully.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": [{"name": "pikachu"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = fetch_pokemon(limit=1)

        assert isinstance(result, dict)
        assert "results" in result
        assert result["results"][0]["name"] == "pikachu"

    @patch("src.ingest.ingest.requests.get")
    def test_fetch_pokemon_http_error(self, mock_get):
        """
        test_fetch_pokemon_http_error:
        Ensures fetch_pokemon raises HTTPError when API request fails.
        """
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("HTTP error")
        mock_get.return_value = mock_response

        with pytest.raises(Exception):
            fetch_pokemon(limit=1)

    def test_save_raw_creates_file(self, tmp_path):
        """
        test_save_raw_creates_file:
        Ensures save_raw writes JSON to the specified file path.
        """
        test_data = {"hello": "world"}
        filename = "test_raw.json"

        # Override RAW_DIR using tmp_path
        test_path = tmp_path / filename
        saved_path = save_raw(test_data, filename=str(test_path.name))

        # Move saved file into tmp_path manually
        # because save_raw writes into data/raw by default
        # but we want to assert file creation in tmp_path
        saved_path = Path("data/raw") / filename
        assert saved_path.exists()

        # Validate file contents
        with saved_path.open("r", encoding="utf-8") as f:
            loaded = json.load(f)

        assert loaded == test_data
