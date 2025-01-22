from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import TYPE_CHECKING
from .user import User
from .word import Word

class UserProgress(db.Model):
    userprogress_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    word_id: Mapped[int] = mapped_column(db.ForeignKey('word.id'))
    score: Mapped[int]
    completion_time: Mapped[int]
    attempts: Mapped[int]

    user: Mapped['User'] = relationship('User', back_populates='progress')
    word: Mapped['Word'] = relationship('Word', back_populates='progress')

    def to_dict(self):
        return {
            'userprogress_id': self.id,
            'user_id': self.user_id,
            'word_id': self.word_id,
            'score': self.score,
            'completion_time': self.completion_time,
            'attempts': self.attempts
        }

    @classmethod
    def from_dict(cls, data):
        return UserProgress(user_id=data['user_id'], 
                            word_id=data['word_id'],
                            score=data['score'], 
                            completion_time=data['completion_time'], 
                            attempts=data['attempts']
        )