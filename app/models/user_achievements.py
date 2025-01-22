from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from ..db import db
from typing import TYPE_CHECKING
from .user import User
from .achievement import Achievement
from datetime import datetime

class UserAchievements(db.Model):
    __tablename__ = 'user_achievements'

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    achievement_id: Mapped[int] = mapped_column(ForeignKey('achievement.id'), primary_key=True)

    user: Mapped['User'] = relationship('User', back_populates='achievements')
    achievement: Mapped['Achievement'] = relationship('Achievement', back_populates='user_achievements')

    def to_dict(self):
        return {
            'achievement_id': self.achievement_id,
            'user_id': self.user_id,
        }

    @classmethod
    def from_dict(cls, data):
        return UserAchievements(user_id=data['user_id'], 
                                achievement_id=data['achievement_id']
        )