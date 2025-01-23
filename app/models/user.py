from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
from .user_achievements import UserAchievements
from .game import Game

class User(db.Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str]
    password_hash: Mapped[str]
    avatar: Mapped[str]

    achievements: Mapped[list['UserAchievements']] = relationship('UserAchievements', back_populates='users')
    games: Mapped[list['Game']] = relationship('Game', back_populates='users')

    def to_dict(self):
        return {
            'user_id': self.id,
            'username': self.username,
            'password_hash': self.password_hash,
            'avatar': self.avatar
        }

    @classmethod
    def from_dict(cls, data):
        return User(username=data['username'], 
                    password_hash=data['password_hash'], 
                    avatar=data.get('avatar')
        )