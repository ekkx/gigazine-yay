import re
import discord

from models import GigazineArticle

def extract_article(message: discord.Message) -> GigazineArticle:
  url_pattern = r"https?://[^\s]+"
  match = re.search(url_pattern, message.content)
  if match:
    url = match.group()
    title = message.content.replace(url, "").strip()
    return GigazineArticle(
      title=title,
      url=url
    )
  return GigazineArticle(
    title=message.content,
    url=""
  )
