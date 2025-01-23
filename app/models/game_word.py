from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .word import Word
from .game import Game

class GameWord(db.Model):
    __tablename__ = 'games_words'

    game_id: Mapped[int] = mapped_column(ForeignKey("game.id"), primary_key=True)
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id"), primary_key=True)

    # Relationships 
    games: Mapped[list["Word"]] = relationship(secondary="games_words", back_populates="words")
    words: Mapped[list["Game"]] = relationship(secondary="games_words", back_populates="games")
