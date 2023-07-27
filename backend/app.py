```python
from flask import Flask, render_template, request, redirect, url_for
from content_management import ContentManagement
from writer_coordination import WriterCoordination
from editorial_calendar import EditorialCalendar
from content_analytics import ContentAnalytics
from social_media_integration import SocialMediaIntegration
from database import init_db, db_session

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/content', methods=['GET', 'POST'])
def content_management():
    if request.method == 'POST':
        ContentManagement.create_post(request.form)
        return redirect(url_for('dashboard'))
    else:
        posts = ContentManagement.get_all_posts()
        return render_template('content.html', posts=posts)

@app.route('/writers', methods=['GET', 'POST'])
def writer_coordination():
    if request.method == 'POST':
        WriterCoordination.assign_task(request.form)
        return redirect(url_for('dashboard'))
    else:
        writers = WriterCoordination.get_all_writers()
        return render_template('writers.html', writers=writers)

@app.route('/calendar', methods=['GET', 'POST'])
def editorial_calendar():
    if request.method == 'POST':
        EditorialCalendar.schedule_post(request.form)
        return redirect(url_for('dashboard'))
    else:
        calendar = EditorialCalendar.get_calendar()
        return render_template('calendar.html', calendar=calendar)

@app.route('/analytics')
def content_analytics():
    analytics = ContentAnalytics.get_analytics()
    return render_template('analytics.html', analytics=analytics)

@app.route('/socialMedia', methods=['GET', 'POST'])
def social_media_integration():
    if request.method == 'POST':
        SocialMediaIntegration.create_post(request.form)
        return redirect(url_for('dashboard'))
    else:
        posts = SocialMediaIntegration.get_all_posts()
        return render_template('socialMedia.html', posts=posts)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)
```