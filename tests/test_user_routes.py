import pytest
from app.models.user import User

def test_create_user(test_client):
    # 测试创建用户的逻辑
    response = test_client.post('/api/users', json={
        'username': 'testuser',
        'password_hash': 'hashedpassword',
        'avatar': 'avatar_url'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['username'] == 'testuser'
    assert data['password_hash'] == 'hashedpassword'
    assert data['avatar'] == 'avatar_url'

def test_get_user(test_client, init_database):
    # 获取测试用户
    user = User.query.filter_by(username='testuser').first()
    user_id = user.id

    # 测试获取用户的逻辑
    response = test_client.get(f'/api/users/{user_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == user_id
    assert data['username'] == 'testuser'
    assert data['password_hash'] == 'hashedpassword'
    assert data['avatar'] == 'avatar_url'