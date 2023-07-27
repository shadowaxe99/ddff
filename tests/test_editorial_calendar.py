```python
import unittest
from backend.editorial_calendar import EditorialCalendar

class TestEditorialCalendar(unittest.TestCase):

    def setUp(self):
        self.calendar = EditorialCalendar()

    def test_schedule_post(self):
        result = self.calendar.schedule_post('Test Post', '2022-12-31')
        self.assertEqual(result, 'Post scheduled successfully')

    def test_set_deadline(self):
        result = self.calendar.set_deadline('Test Post', '2022-12-31')
        self.assertEqual(result, 'Deadline set successfully')

    def test_send_reminder(self):
        result = self.calendar.send_reminder('Test Post', '2022-12-31')
        self.assertEqual(result, 'Reminder sent successfully')

if __name__ == '__main__':
    unittest.main()
```