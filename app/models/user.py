from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .achievement import Achievement
    from .user_achievement import UserAchievement
    from .game import Game

class User(db.Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str]
    password_hash: Mapped[str]
    avatar: Mapped[str]=mapped_column(nullable=True)

    # achievements: Mapped[list['UserAchievements']] = relationship(secondary='user_achievements', back_populates='user')
    # games: Mapped[list['Game']] = relationship('Game', back_populates='user')

    # Many-to-many relationship with Achievement through UserAchievements
    achievements: Mapped[list['Achievement']] = relationship(
        secondary='user_achievements',
        back_populates='users'
    )

    # One-to-many relationship with UserAchievement
    user_achievements: Mapped[list['UserAchievement']] = relationship('UserAchievement', back_populates='user')


    # One-to-many relationship with Game
    games: Mapped[list['Game']] = relationship('Game', back_populates='user')


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