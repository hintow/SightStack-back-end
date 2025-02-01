from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .user_achievement import UserAchievement

class Achievement(db.Model):
    __tablename__ = 'achievements'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    required_score: Mapped[int]

    # Many-to-many relationship with User through UserAchievements
    users: Mapped[list['User']] = relationship(
        secondary='user_achievements',
        back_populates='achievements'
    )

    # One-to-many relationship with UserAchievement
    user_achievements: Mapped[list['UserAchievement']] = relationship('UserAchievement', back_populates='achievement')


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'required_score': self.required_score
        }

    @classmethod
    def from_dict(cls, data):
        return Achievement(
            title=data['title'],
            description=data['description'],
            required_score=data['required_score']
        )
