from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from ..db import db
from typing import TYPE_CHECKING
from datetime import datetime

class UserAchievements(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    achievement_id: Mapped[int]
    date_earned: Mapped[str]

    user: Mapped['User'] = relationship('User', back_populates='achievements')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'achievement_id': self.achievement_id,
            'date_earned': self.date_earned
        }

    @classmethod
    def from_dict(cls, data):
        return UserAchievements(user_id=data['user_id'], 
                                achievement_id=data['achievement_id'], 
                                date_earned=data['date_earned']
        )