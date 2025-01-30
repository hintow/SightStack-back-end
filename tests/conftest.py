import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client  # this is where the testing happens!

            db.session.remove()
            db.drop_all()

@pytest.fixture(scope='module')
def init_database():
    # Create a test user
    user = User(username='testuser', password_hash='hashedpassword', avatar='avatar_url')
    db.session.add(user)
    db.session.commit()

    yield db  # this is where the testing happens!

    db.session.remove()
    db.drop_all()