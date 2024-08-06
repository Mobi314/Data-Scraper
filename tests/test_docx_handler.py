import unittest
from src.file_handler.docx_handler import extract_docx_text

class TestDocxHandler(unittest.TestCase):
    def test_extract_docx_text(self):
        text = extract_docx_text('path_to_sample.docx')
        self.assertIn('Expected text', text)

if __name__ == '__main__':
    unittest.main()
