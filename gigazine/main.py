import os
import logging

import discord
import yaylib

import utils

class Gigazine(discord.Client):
  def __init__(
    self,
    channel_id: int,
    official_bot_id: int,
    tester_id: int,
    yay_email: str,
    yay_password: str,
    intents: discord.Intents
  ):
    super().__init__(intents=intents)
    self.channel_id = channel_id
    self.official_bot_id = official_bot_id
    self.tester_id = tester_id
    self.yay_email = yay_email
    self.yay_password = yay_password
    self.yay = yaylib.Client(loglevel=logging.INFO)

  async def on_ready(self):
    self.yay.logger.info("Gigazine bot is ready!")

  async def on_message(self, message: discord.Message):
    if message.author == self.user:
      return

    if message.channel.id != self.channel_id:
      return

    if message.author.id not in (self.official_bot_id, self.tester_id):
      return

    article = utils.extract_article(message)
    self.yay.logger.info(f"Article Title: {article.title}")
    self.yay.logger.info(f"Article URL: {article.url}")

    await self.yay.auth.login(self.yay_email, self.yay_password)
    await self.yay.post.create_post(text=article.title, shared_url=article.url)
    self.yay.logger.info("Article successfully posted to Yay!")

def main():
  intents = discord.Intents.default()
  intents.message_content = True

  gigazine = Gigazine(
    channel_id=int(os.getenv("DISCORD_GIGAZINE_CHANNEL_ID")),
    official_bot_id=int(os.getenv("DISCORD_GIGAZINE_BOT_ID")),
    tester_id=int(os.getenv("DISCORD_TESTER_ID")),
    yay_email=os.getenv("YAY_EMAIL"),
    yay_password=os.getenv("YAY_PASSWORD"),
    intents=intents
  )

  gigazine.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
  main()
