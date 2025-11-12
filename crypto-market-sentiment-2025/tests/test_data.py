import unittest
from src.data.load_data import load_data
from src.data.preprocess import preprocess_data

class TestDataFunctions(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize test variables or states
        self.raw_data_path = 'data/raw/sample_data.csv'
        self.processed_data_path = 'data/processed/processed_data.csv'
        self.data = load_data(self.raw_data_path)

    def test_load_data(self):
        # Test if data is loaded correctly
        self.assertIsNotNone(self.data)
        self.assertGreater(len(self.data), 0)

    def test_preprocess_data(self):
        # Test if preprocessing function works correctly
        processed_data = preprocess_data(self.data)
        self.assertIsNotNone(processed_data)
        self.assertEqual(processed_data.shape[0], self.data.shape[0])  # Check if rows are preserved

    def tearDown(self):
        # Cleanup code if necessary
        pass

if __name__ == '__main__':
    unittest.main()