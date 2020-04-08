import unittest

from app.tests.practice_centers.fakes import center1, center2, center3
from app.tests.shops.fakes import shop3, shop2, shop1
from app.tests.sports.fakes import sport1, sport2, sport3
from app.tests.test_basic_views import BasicViewTests
from app.tests.users.fakes import user1, user2, user3


class RootViewsTests(BasicViewTests):

    def test_search_with_sports_should_redirect(self):
        form = {'search_route': 'sports.sports'}
        response = self.app.post('/search', follow_redirects=True, data=form)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Sports', response.data)
        self.assertIn(sport1.name.encode(), response.data)
        self.assertNotIn(sport2.name.encode(), response.data)
        self.assertNotIn(sport3.name.encode(), response.data)

    def test_search_with_practice_centers_should_redirect(self):
        form = {'search_route': 'practice_centers.practice_centers'}
        response = self.app.post('/search', follow_redirects=True, data=form)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Practice Centers', response.data)
        self.assertIn(center1.name.encode(), response.data)
        self.assertNotIn(center2.name.encode(), response.data)
        self.assertNotIn(center3.name.encode(), response.data)

    def test_search_with_shops_should_redirect(self):
        form = {'search_route': 'shops.shops'}
        response = self.app.post('/search', follow_redirects=True, data=form)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Shops', response.data)
        self.assertIn(shop1.name.encode(), response.data)
        self.assertNotIn(shop2.name.encode(), response.data)
        self.assertNotIn(shop3.name.encode(), response.data)

    def test_search_with_users_should_redirect(self):
        form = {'search_route': 'users.users'}
        response = self.app.post('/search', follow_redirects=True, data=form)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SportsApp', response.data)
        self.assertIn(b'Users', response.data)
        self.assertIn(user1.username.encode(), response.data)
        self.assertNotIn(user2.username.encode(), response.data)
        self.assertNotIn(user3.username.encode(), response.data)


if __name__ == "__main__":
    unittest.main()
