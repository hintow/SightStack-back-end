from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import TYPE_CHECKING
from .user import User
from .word import Word

class Game(db.Model):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    score: Mapped[int]
    level: Mapped[str]


    user: Mapped['User'] = relationship('User', back_populates='games')
    words: Mapped[list["Word"]] = relationship(secondary="game_word", back_populates="games")
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'score': self.score,
            'level': self.level
        }

    @classmethod
    def from_dict(cls, data):
        return Game(user_id=data['id'], 
                    word_id=data['word_id'],
                    score=data['score'],
                    level=data['level']
        )