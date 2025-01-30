import unittest
from app import create_app, db
from app.models.achievement import Achievement

class AchievementRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_achievement(self):
        # 测试创建成就的逻辑
        response = self.client.post('/api/achievements', json={
            'name': 'Mercury Explorer',
            'description': "Like the swift Mercury, you’ve taken your first steps in solving games!"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['name'], 'Mercury Explorer')
        self.assertEqual(data['description'], "Like the swift Mercury, you’ve taken your first steps in solving games!")

    def test_get_achievement(self):
        # 先创建一个成就
        with self.app.app_context():
            achievement = Achievement(name='Mercury Explorer', description="Like the swift Mercury, you’ve taken your first steps in solving games!")
            db.session.add(achievement)
            db.session.commit()
            achievement_id = achievement.id

        # 测试获取成就的逻辑
        response = self.client.get(f'/api/achievements/{achievement_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['id'], achievement_id)
        self.assertEqual(data['name'], 'Mercury Explorer')
        self.assertEqual(data['description'], "Like the swift Mercury, you’ve taken your first steps in solving games!")

if __name__ == '__main__':
    unittest.main()