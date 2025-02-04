
def test_daily_challenge(test_client):
    response = test_client.get('/words/daily')
    assert response.status_code == 200
    data = response.get_json()
    assert 'word' in data
    assert 'hint' in data
    assert 'level' in data

def test_get_words_by_level(test_client):
    response = test_client.get('/words/level/prek')
    assert response.status_code == 200
    data = response.get_json()
    assert 'word' in data
    assert 'hint' in data
    assert 'level' in data