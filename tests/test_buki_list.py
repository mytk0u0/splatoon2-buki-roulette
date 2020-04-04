"""
buki_list.py
"""
import tempfile
from unittest.mock import patch
from splatoon2_buki_roulette.buki_list import write_buki_list, read_buki_list, update

BUKI_LIST_FILE = "buki_list.csv"


def test_write_buki_list() -> None:
    """
    write_buki_list
    """
    with tempfile.NamedTemporaryFile() as fp:
        path = fp.name
        buki_list = ["a", "b", "c"]
        with patch(
            "splatoon2_buki_roulette.buki_list.get_buki_list_file_path",
            return_value=path,
        ) as mock_gblfp:
            write_buki_list(buki_list)
            assert fp.read().decode("utf-8") == "a,b,c"
            mock_gblfp.assert_called_once()


def test_read_buki_list() -> None:
    """
    read_buki_list
    """
    with tempfile.NamedTemporaryFile() as fp:
        path = fp.name
        buki_list = ["a", "b", "c"]
        with patch(
            "splatoon2_buki_roulette.buki_list.get_buki_list_file_path",
            return_value=path,
        ) as mock_gblfp:
            fp.write(",".join(buki_list).encode("utf-8"))
            fp.flush()
            assert read_buki_list() == ["a", "b", "c"]
            mock_gblfp.assert_called_once()


def test_update() -> None:
    """
    update
    """
    buki_list = ["a", "b", "c"]
    with patch(
        "splatoon2_buki_roulette.buki_list.request_buki_names", return_value=buki_list,
    ) as mock_rbn, patch(
        "splatoon2_buki_roulette.buki_list.write_buki_list"
    ) as mock_wbl:
        update()
        mock_rbn.assert_called_once()
        mock_wbl.assert_called_once_with(buki_list)
