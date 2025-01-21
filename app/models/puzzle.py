from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING

class Puzzle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    word: Mapped[str] 
    definition: Mapped[str] 
    grade: Mapped[str]

    progress: Mapped[list['UserProgress']] = relationship('UserProgress', back_populates='puzzle')

    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'definition': self.definition,
            'grade': self.grade
        }

    @classmethod
    def from_dict(cls, data):
        return Puzzle(
            word=data['word'],
            definition=data['definition'],
            grade=data['grade']
        )