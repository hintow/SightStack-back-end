from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from ..db import db
from typing import TYPE_CHECKING
from .user import User
from datetime import datetime

class UserAchievements(db.Model):
    achievement_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'))
    description: Mapped[str]

    user: Mapped['User'] = relationship('User', back_populates='achievements')

    def to_dict(self):
        return {
            'achievement_id': self.id,
            'user_id': self.user_id,
            'description':self.description
        }

    @classmethod
    def from_dict(cls, data):
        return UserAchievements(user_id=data['user_id'], 
                                description=data['description']
        )