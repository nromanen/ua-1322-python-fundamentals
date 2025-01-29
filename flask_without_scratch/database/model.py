from datetime import datetime


class Post:
    def __init__(self, title, content, created_at=None, id=None):
        self.title = title
        self.content = content
        self.created_at = created_at
        self.id = id

    @staticmethod
    def validate(title, content):
        errors = []
        if not title or not title.strip():
            errors.append("Title is required!")
        if not content or not content.strip():
            errors.append("Content is required!")
        return errors

    def __repr__(self):
        return f"<Post: {self.id}, title = {self.title}, content = {self.content}, created_at = {self.created_at}>"
