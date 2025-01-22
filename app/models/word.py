from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
from .game import Game
from .game_word import GameWord


class Word(db.Model):
    __tablename__ = 'words'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    word: Mapped[str] 
    hint: Mapped[str] 
    level: Mapped[str]

    # Relationship to GameWords
    game_words: Mapped[list['GameWord']] = relationship('GameWord', back_populates='word')

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