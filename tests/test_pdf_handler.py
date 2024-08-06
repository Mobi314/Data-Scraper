import unittest
from src.file_handler.pdf_handler import extract_pdf_text

class TestPDFHandler(unittest.TestCase):
    def test_extract_pdf_text(self):
        text = extract_pdf_text('path_to_sample.pdf')
        self.assertIn('Expected text', text)

if __name__ == '__main__':
    unittest.main()
