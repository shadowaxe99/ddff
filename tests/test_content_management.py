```python
import unittest
from backend.content_management import ContentManagement

class TestContentManagement(unittest.TestCase):

    def setUp(self):
        self.cm = ContentManagement()

    def test_create_post(self):
        result = self.cm.create_post("Test Title", "Test Content")
        self.assertEqual(result['status'], 'success')

    def test_edit_post(self):
        result = self.cm.edit_post(1, "Updated Title", "Updated Content")
        self.assertEqual(result['status'], 'success')

    def test_publish_post(self):
        result = self.cm.publish_post(1)
        self.assertEqual(result['status'], 'success')

    def test_delete_post(self):
        result = self.cm.delete_post(1)
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
```