from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .word import Word
    from .user import User

class UserWord(db.Model):
    
    # 记录用户对单词的掌握情况。
    __tablename__ = 'users_words'

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    word_id: Mapped[int] = mapped_column(ForeignKey("words.id"), primary_key=True)

    mastered: Mapped[bool] = mapped_column(db.Boolean, default=False)
    attempts: Mapped[int] = mapped_column(db.Integer, default=0)    