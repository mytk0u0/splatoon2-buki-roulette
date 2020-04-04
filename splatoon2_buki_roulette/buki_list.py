"""
ブキの更新。stat.inkのAPIから取得する。
(もうブキが増えることはないだろうけど...)
"""

import os
import json
from typing import List
import requests

BUKI_LIST_FILE = "buki_list.csv"


def request_buki_names() -> List[str]:
    """
    ブキ名一覧をstat.inkのAPIから取得する
    """
    try:
        r = requests.get("https://stat.ink/api/v2/weapon")
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise e

    return [i["name"]["ja_JP"] for i in json.loads(r.content) if i["reskin_of"] is None]


def get_buki_list_file_path() -> str:
    """
    ブキ名一覧ファイルを取得する
    """
    return os.path.join(os.path.dirname(__file__), BUKI_LIST_FILE)


def write_buki_list(buki_list: List[str]) -> None:
    """
    ブキ名一覧ファイルに、ブキ名一覧を書き込む
    """
    path = get_buki_list_file_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(",".join(buki_list))


def read_buki_list() -> List[str]:
    """
    ブキ名一覧ファイルから、ブキ名一覧を読み込む
    """
    path = get_buki_list_file_path()
    with open(path, "r", encoding="utf-8") as f:
        return f.read().split(",")


def update() -> None:
    """
    ブキ名一覧を更新する
    """
    buki_list = request_buki_names()
    write_buki_list(buki_list)
