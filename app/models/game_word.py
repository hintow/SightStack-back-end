from app import db

class GameWords(db.Model):
    __tablename__ = 'game_words'

    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), primary_key=True)

    # Relationships (optional, for easier navigation)
    game = db.relationship('Game', back_populates='game_words')
    word = db.relationship('Word', back_populates='game_words')
