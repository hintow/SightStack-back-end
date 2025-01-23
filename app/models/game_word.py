from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .word import Word
from .game import Game

class GameWord(db.Model):
    __tablename__ = 'game_word'

    game_id: Mapped[int] = mapped_column(ForeignKey('games.id'), primary_key=True)
    word_id: Mapped[int] = mapped_column(ForeignKey('words.id'), primary_key=True)

    # Relationships 
    games: Mapped[list["Word"]] = relationship(secondary="game_word", back_populates="words")
    words: Mapped[list["Game"]] = relationship(secondary="game_word", back_populates="games")
