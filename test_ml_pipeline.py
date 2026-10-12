import os
import unittest

import joblib
import pandas as pd

from train_model import create_dataset, train_model


class TestMLPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.accuracy = train_model()
        cls.model = joblib.load("student_result_model.pkl")
        cls.data = pd.read_csv("student_results.csv")

    def test_dataset_has_300_records(self):
        self.assertEqual(len(self.data), 300)

    def test_dataset_has_required_columns(self):
        expected = {
            "attendance",
            "internal_marks",
            "assignment_marks",
            "previous_score",
            "weighted_score",
            "result"
        }
        self.assertTrue(expected.issubset(set(self.data.columns)))

    def test_model_file_exists(self):
        self.assertTrue(os.path.exists("student_result_model.pkl"))

    def test_metrics_file_exists(self):
        self.assertTrue(os.path.exists("metrics.json"))

    def test_model_predicts_pass(self):
        result = self.model.predict(pd.DataFrame([{
            "attendance": 90,
            "internal_marks": 85,
            "assignment_marks": 80,
            "previous_score": 85
        }]))
        self.assertEqual(int(result[0]), 1)

    def test_model_predicts_fail(self):
        result = self.model.predict(pd.DataFrame([{
            "attendance": 50,
            "internal_marks": 25,
            "assignment_marks": 40,
            "previous_score": 35
        }]))
        self.assertEqual(int(result[0]), 0)

    def test_accuracy_is_valid(self):
        self.assertGreaterEqual(self.accuracy, 0.0)
        self.assertLessEqual(self.accuracy, 1.0)


if __name__ == "__main__":
    unittest.main()
