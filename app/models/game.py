from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .word import Word
    from .game_word import GameWord

class Game(db.Model):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'))
    score: Mapped[int]
    level: Mapped[str]

     # Many-to-one relationship with User
    user: Mapped['User'] = relationship('User', back_populates='games')

    # One-to-many relationship with GameWord
    game_words: Mapped[list['GameWord']] = relationship('GameWord', back_populates='game')

    # Many-to-many relationship with Word through GameWord
    words: Mapped[list['Word']] = relationship(secondary='games_words', back_populates='games')

    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'score': self.score,
            'level': self.level
        }

    @classmethod
    def from_dict(cls, data):
        return Game(user_id=data['user_id'], 
                    score=data['score'],
                    level=data['level']
        )
    