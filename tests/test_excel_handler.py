import unittest
from src.file_handler.excel_handler import extract_excel_data

class TestExcelHandler(unittest.TestCase):
    def test_extract_excel_data(self):
        data = extract_excel_data('path_to_sample.xlsx')
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
