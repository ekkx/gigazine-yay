import re
import discord

from models import GigazineArticle

def get_article_title(text, url):
    if url is not None:
        return re.sub(url, '', text)
    return text

def extract_article(message: discord.Message) -> GigazineArticle:
  if message.embeds and message.embeds[0]:
    url = message.embeds[0].url
    title = get_article_title(message.content, url)
    return GigazineArticle(title, url)
  return GigazineArticle(message.content)
