```python
import unittest
from backend.social_media_integration import SocialMediaIntegration

class TestSocialMediaIntegration(unittest.TestCase):

    def setUp(self):
        self.social_media = SocialMediaIntegration()

    def test_post_to_social_media(self):
        result = self.social_media.post_to_social_media("Test post", "https://test.com")
        self.assertEqual(result, "Post successful")

    def test_track_social_media_engagement(self):
        result = self.social_media.track_social_media_engagement("Test post")
        self.assertIsInstance(result, dict)
        self.assertIn('likes', result)
        self.assertIn('shares', result)
        self.assertIn('comments', result)

    def test_manage_social_media_posts(self):
        result = self.social_media.manage_social_media_posts()
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
```