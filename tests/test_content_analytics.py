```python
import unittest
from backend.content_analytics import ContentAnalytics

class TestContentAnalytics(unittest.TestCase):

    def setUp(self):
        self.analytics = ContentAnalytics()

    def test_get_post_views(self):
        post_id = 1
        views = self.analytics.get_post_views(post_id)
        self.assertIsInstance(views, int)

    def test_get_post_shares(self):
        post_id = 1
        shares = self.analytics.get_post_shares(post_id)
        self.assertIsInstance(shares, int)

    def test_get_post_comments(self):
        post_id = 1
        comments = self.analytics.get_post_comments(post_id)
        self.assertIsInstance(comments, int)

    def test_get_top_posts(self):
        top_posts = self.analytics.get_top_posts()
        self.assertIsInstance(top_posts, list)

    def test_get_performance_metrics(self):
        metrics = self.analytics.get_performance_metrics()
        self.assertIsInstance(metrics, dict)

if __name__ == '__main__':
    unittest.main()
```