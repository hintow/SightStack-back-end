from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .word import Word
    from .game import Game

class GameWord(db.Model):
    __tablename__ = 'games_words'

    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), primary_key=True)
    word_id: Mapped[int] = mapped_column(ForeignKey("words.id"), primary_key=True)

    # Relationships 
    game: Mapped["Game"]= relationship("Game", back_populates="game_words")
    word: Mapped["Word"] = relationship("Word", back_populates="game_words")
