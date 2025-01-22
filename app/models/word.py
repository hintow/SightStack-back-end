from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
from .game import Game

class Word(db.Model):
    __tablename__ = 'sight_words'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    word: Mapped[str] 
    definition: Mapped[str] 
    level: Mapped[str]


    # Relationship to GameWords
    game_words = db.relationship('GameWords', back_populates='word')

    # Optional: Access games directly via the relationship
    games = db.relationship('Game', secondary='games_words', back_populates='words')

    def to_dict(self):
        return {
            'word_id': self.id,
            'word': self.word,
            'definition': self.definition,
            'level': self.level
        }

    @classmethod
    def from_dict(cls, data):
        return Word(
            word=data['word'],
            definition=data['definition'],
            level=data['level']
        )