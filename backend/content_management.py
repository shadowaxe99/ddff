```python
import requests
from flask import Flask, request
from database import db_session, init_db
from models import Post

app = Flask(__name__)

def get_wordpress_posts():
    response = requests.get('https://your-wordpress-site.com/wp-json/wp/v2/posts')
    return response.json()

@app.route('/content', methods=['GET', 'POST'])
def manage_content():
    if request.method == 'POST':
        post_data = request.get_json()
        new_post = Post(title=post_data['title'], content=post_data['content'])
        db_session.add(new_post)
        db_session.commit()
        return {'message': 'Post created'}, 201

    posts = get_wordpress_posts()
    return {'posts': posts}, 200

@app.route('/content/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_single_content(post_id):
    post = Post.query.get(post_id)
    if request.method == 'GET':
        return {'post': post.to_dict()}, 200
    elif request.method == 'PUT':
        post_data = request.get_json()
        post.title = post_data['title']
        post.content = post_data['content']
        db_session.commit()
        return {'message': 'Post updated'}, 200
    elif request.method == 'DELETE':
        db_session.delete(post)
        db_session.commit()
        return {'message': 'Post deleted'}, 200

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
```