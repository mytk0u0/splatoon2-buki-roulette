"""
ブキルーレット
"""

import os
import random
from typing import List
from dotenv import load_dotenv
import discord
from .buki_list import read_buki_list


load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
buki_list = read_buki_list()


def generate_buki_lot_table(names: List[str]) -> str:
    """
    ブキの割り当て表を作る
    """
    result = ""
    for name in sorted(names):
        buki = random.choice(buki_list)
        result += f"{name}:\t{buki}\n"
    return result


class Splatool2BukiRouletteClient(discord.Client):
    """
    ブキルーレット
    チャンネルの閲覧権限と、メッセージの送信権限が必要です
    """

    async def on_message(self, message: discord.Message) -> None:
        """
        メッセージを受け取ったときの行動
        """
        if message.author == self.user:
            return

        if message.content.startswith("/bukinani"):
            if message.content.startswith("/bukinani help"):
                await message.channel.send(
                    "/bukinani で、あなたやあなたと同じボイスチャンネルにいるプレイヤーのブキをランダムに選びます"
                )
            elif message.author.voice is None:
                await message.channel.send("ボイスチャンネルに入った状態で実行してね")
            else:
                voice_channel_members = message.author.voice.channel.members
                names = [i.name for i in voice_channel_members]
                await message.channel.send(generate_buki_lot_table(names))


def run() -> None:
    """
    実行
    """
    client = Splatool2BukiRouletteClient()
    client.run(discord_token)
