```python
from flask import Flask, request, jsonify
from database import db_session, init_db
from models import Writer, Task

app = Flask(__name__)

@app.route('/writers', methods=['GET'])
def get_writers():
    writers = Writer.query.all()
    return jsonify([writer.serialize for writer in writers])

@app.route('/writer', methods=['POST'])
def add_writer():
    new_writer = Writer(name=request.json['name'], email=request.json['email'])
    db_session.add(new_writer)
    db_session.commit()
    return jsonify(new_writer.serialize), 201

@app.route('/writer/<int:writer_id>', methods=['GET'])
def get_writer(writer_id):
    writer = Writer.query.get(writer_id)
    if writer is None:
        return jsonify({'error': 'Writer not found'}), 404
    return jsonify(writer.serialize)

@app.route('/writer/<int:writer_id>', methods=['PUT'])
def update_writer(writer_id):
    writer = Writer.query.get(writer_id)
    if writer is None:
        return jsonify({'error': 'Writer not found'}), 404
    writer.name = request.json.get('name', writer.name)
    writer.email = request.json.get('email', writer.email)
    db_session.commit()
    return jsonify(writer.serialize)

@app.route('/writer/<int:writer_id>', methods=['DELETE'])
def delete_writer(writer_id):
    writer = Writer.query.get(writer_id)
    if writer is None:
        return jsonify({'error': 'Writer not found'}), 404
    db_session.delete(writer)
    db_session.commit()
    return jsonify({'result': True})

@app.route('/task', methods=['POST'])
def add_task():
    new_task = Task(title=request.json['title'], description=request.json['description'], writer_id=request.json['writer_id'])
    db_session.add(new_task)
    db_session.commit()
    return jsonify(new_task.serialize), 201

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.writer_id = request.json.get('writer_id', task.writer_id)
    db_session.commit()
    return jsonify(task.serialize)

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    db_session.delete(task)
    db_session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```