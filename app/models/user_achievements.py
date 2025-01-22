from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from ..db import db
from typing import TYPE_CHECKING
from .user import User
from datetime import datetime

class UserAchievements(db.Model):
    achievements_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    date_earned: Mapped[str]

    user: Mapped['User'] = relationship('User', back_populates='achievements')

    def to_dict(self):
        return {
            'userachievements_id': self.id,
            'user_id': self.user_id,
            'date_earned': self.date_earned
        }

    @classmethod
    def from_dict(cls, data):
        return UserAchievements(user_id=data['user_id'], 
                                date_earned=data['date_earned']
        )