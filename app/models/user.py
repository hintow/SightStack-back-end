from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .achievement import Achievement
    from .user_achievement import UserAchievement
    from .game import Game

class User(db.Model):
    __tablename__ = 'users'
    
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    child_name: Mapped[str] = mapped_column(db.String(100)) 
    child_age: Mapped[int] = mapped_column(db.Integer)
    email: Mapped[str] = mapped_column(db.String(100), unique=True)
    password_hash: Mapped[str] = mapped_column(db.String(128))
    avatar: Mapped[str] = mapped_column(db.String(200))
    score: Mapped[int] = mapped_column(db.Integer, default=0) 

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
            'child_name': self.child_name,
            'child_age': self.child_age,
            'email': self.email,
            'avatar': self.avatar,
            'score': self.score,
            'achievements': [a.to_dict() for a in self.achievements]
        }

    @classmethod
    def from_dict(cls, data):
        return User(
            child_name=data['child_name'],
            child_age=data['child_age'],
            email=data['email'],
            password_hash=data['password_hash'],  
            avatar=data['avatar']
        )