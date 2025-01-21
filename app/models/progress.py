from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import TYPE_CHECKING

class UserProgress(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    puzzle_id: Mapped[int] = mapped_column(db.ForeignKey('puzzle.id'))
    score: Mapped[int]
    completion_time: Mapped[int]
    attempts: Mapped[int]

    user: Mapped['User'] = relationship('User', back_populates='progress')
    puzzle: Mapped['Word'] = relationship('Puzzle', back_populates='progress')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'puzzle_id': self.puzzle_id,
            'score': self.score,
            'completion_time': self.completion_time,
            'attempts': self.attempts
        }

    @classmethod
    def from_dict(cls, data):
        return UserProgress(user_id=data['user_id'], 
                            puzzle_id=data['puzzle_id'],
                            score=data['score'], 
                            completion_time=data['completion_time'], 
                            attempts=data['attempts']
        )