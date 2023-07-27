```python
import requests
from database import Database

class ContentAnalytics:
    def __init__(self):
        self.db = Database()

    def get_post_data(self, post_id):
        response = requests.get(f"https://your-wordpress-site.com/wp-json/wp/v2/posts/{post_id}")
        return response.json()

    def track_views(self, post_id):
        post_data = self.get_post_data(post_id)
        views = post_data.get('views', 0)
        self.db.update_post_views(post_id, views)
        return views

    def track_shares(self, post_id):
        post_data = self.get_post_data(post_id)
        shares = post_data.get('shares', 0)
        self.db.update_post_shares(post_id, shares)
        return shares

    def track_comments(self, post_id):
        post_data = self.get_post_data(post_id)
        comments = post_data.get('comments', 0)
        self.db.update_post_comments(post_id, comments)
        return comments

    def get_content_performance(self, post_id):
        views = self.track_views(post_id)
        shares = self.track_shares(post_id)
        comments = self.track_comments(post_id)
        return {
            'views': views,
            'shares': shares,
            'comments': comments
        }
```