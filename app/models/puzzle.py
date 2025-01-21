from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING

class Puzzle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    level: Mapped[int]
    content: Mapped[str]

    progress: Mapped[list['UserProgress']] = relationship('UserProgress', back_populates='puzzle')

    def to_dict(self):
        return {
            'id': self.id,
            'level': self.level,
            'content': self.content
        }

    @classmethod
    def from_dict(cls, data):
        return Puzzle(level=data['level'], content=data['content'])