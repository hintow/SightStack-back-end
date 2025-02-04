from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import TYPE_CHECKING
from werkzeug.security import generate_password_hash, check_password_hash


if TYPE_CHECKING:
    from .achievement import Achievement
    from .user_achievement  import UserAchievement
    from .user_word import UserWord

class User(db.Model):
    """User model representing a child user in the application.
    
    Relationships:
        - achievements: Many-to-many with Achievement through UserAchievements
        - user_achievements: One-to-many with UserAchievement
        - user_words: One-to-many with UserWord
        - mastered_words: One-to-many with UserWord (backref)
    """
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    child_name: Mapped[str] = mapped_column(db.String(100)) 
    child_age: Mapped[int] = mapped_column(db.Integer)
    email: Mapped[str] = mapped_column(db.String(100), unique=True)
    password_hash: Mapped[str] = mapped_column(db.String(128))
    avatar: Mapped[str] = mapped_column(db.String(200))
    score: Mapped[int] = mapped_column(db.Integer, default=0) 


    # mastered_words: Mapped[list['UserWord']] = relationship('UserWord', backref='user', lazy=True)
    
    # Many-to-many relationship with Achievement through UserAchievements
    achievements: Mapped[list['Achievement']] = relationship(
        secondary='user_achievements',
        back_populates='users'
    )

    # One-to-many relationship with UserAchievement
    user_achievements: Mapped[list['UserAchievement']] = relationship(
        'UserAchievement', 
        back_populates='user', 
        overlaps="achievements"
    )

    # One-to-many relationship with UserWord
    # user_words: Mapped[list['UserWord']] = relationship('UserWord', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'child_name': self.child_name,
            'child_age': self.child_age,
            'email': self.email,
            'avatar': self.avatar,
            'score': self.score,
            'achievements': [a.to_dict() for a in self.achievements]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            child_name=data['child_name'],
            child_age=data['child_age'],
            email=data['email'],
            avatar=data['avatar']
        )
        user.set_password(data['password'])
        return user
    
    