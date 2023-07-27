```python
import requests
from flask import Flask, request, jsonify
from database import db_session

app = Flask(__name__)

@app.route('/socialMedia', methods=['POST'])
def manage_social_media():
    data = request.get_json()
    post_id = data.get('post_id')
    platform = data.get('platform')

    if platform == 'facebook':
        return post_to_facebook(post_id)
    elif platform == 'twitter':
        return post_to_twitter(post_id)
    else:
        return jsonify({'message': 'Invalid platform'}), 400

def post_to_facebook(post_id):
    post = db_session.query(Post).filter(Post.id == post_id).first()
    if not post:
        return jsonify({'message': 'Post not found'}), 404

    # Replace with your Facebook API credentials
    access_token = 'your-access-token'
    page_id = 'your-page-id'

    url = f'https://graph.facebook.com/{page_id}/feed'
    payload = {
        'message': post.content,
        'access_token': access_token
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return jsonify({'message': 'Post published on Facebook'}), 200
    else:
        return jsonify({'message': 'Failed to publish post on Facebook'}), 500

def post_to_twitter(post_id):
    post = db_session.query(Post).filter(Post.id == post_id).first()
    if not post:
        return jsonify({'message': 'Post not found'}), 404

    # Replace with your Twitter API credentials
    consumer_key = 'your-consumer-key'
    consumer_secret = 'your-consumer-secret'
    access_token = 'your-access-token'
    access_token_secret = 'your-access-token-secret'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        api.update_status(post.content)
        return jsonify({'message': 'Post published on Twitter'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to publish post on Twitter', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```