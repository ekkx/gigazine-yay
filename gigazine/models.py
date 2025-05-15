class GigazineArticle:
  def __init__(self, title: str, url: str):
    self.title = title
    self.url = url

  def __str__(self):
    return f"Article Title: {self.title}, URL: {self.url}"
