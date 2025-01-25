from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
from .game import Game

if TYPE_CHECKING:
    from .game_word import GameWord


class Word(db.Model):
    __tablename__ = 'words'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    word: Mapped[str] 
    hint: Mapped[str] 
    level: Mapped[str]

    # One-to-many relationship with GameWord
    game_words: Mapped[list['GameWord']] = relationship('GameWord', back_populates='word')

    # Many-to-many relationship with Game through GameWord
    games: Mapped[list['Game']] = relationship(secondary='games_words', back_populates='words')

    def to_dict(self):
        return {
            'word_id': self.id,
            'word': self.word,
            'hint': self.hint,
            'level': self.level
        }

    @classmethod
    def from_dict(cls, data):
        return Word(
            word=data['word'],
            hint=data['hint'],
            level=data['level']
        )