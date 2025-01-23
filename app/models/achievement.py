from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .user_achievements import UserAchievements


class Achievement(db.Model):
    __tablename__ = 'achievements'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]

    user_achievements: Mapped[list['UserAchievements']] = relationship('UserAchievements', back_populates='achievements')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        return Achievement(
            title=data['title'],
            description=data['description']
        )
