import re
import discord

from models import GigazineArticle

def get_article_url(text: str):
    url_regex = r"(?P<url>https?://[^\s]+)"
    match = re.search(url_regex, text)
    if match:
        return match.group("url")
    else:
        return ""

def get_article_title(text:str, url:str):
    if url is not None:
        return re.sub(url, '', text)
    return text

def extract_article(message: discord.Message) -> GigazineArticle:
  url = get_article_url(message.content)
  return GigazineArticle(
    title=get_article_title(message.content, url),
    url=url
  )
