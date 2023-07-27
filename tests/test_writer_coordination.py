```python
import unittest
from backend.writer_coordination import WriterCoordination

class TestWriterCoordination(unittest.TestCase):

    def setUp(self):
        self.writer_coordination = WriterCoordination()

    def test_task_assignment(self):
        result = self.writer_coordination.assign_task('writer1', 'task1')
        self.assertEqual(result, 'Task assigned successfully')

    def test_progress_tracking(self):
        result = self.writer_coordination.track_progress('task1')
        self.assertEqual(result, 'In Progress')

    def test_communication_tools(self):
        result = self.writer_coordination.send_message('writer1', 'Hello')
        self.assertEqual(result, 'Message sent successfully')

if __name__ == '__main__':
    unittest.main()
```