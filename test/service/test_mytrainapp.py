import unittest
from src.service.MyTrainApp import Train

# Command to run: python -m unittest test/service/test_mytrainapp.py

class TestTrain(unittest.TestCase):

    def test_calculate_capacity_sufficient(self):
        train = Train("Tube", 6)  # 6 carriages, each with 28 seats
        result = train.calculate_capacity(160)  # 6 * 28 = 168 capacity
        self.assertEqual(result, "Sufficient")

    def test_calculate_capacity_insufficient(self):
        train = Train("SouthWestRail", 4)  # 4 carriages, each with 50 seats
        result = train.calculate_capacity(250)  # 4 * 50 = 200 capacity
        self.assertEqual(result, "Insufficient")

    def test_invalid_train_type(self):
        with self.assertRaises(ValueError) as context:
            Train("UnknownTrain", 5)  # Invalid train type
        self.assertEqual(
            str(context.exception),
            "Unknown train type: UnknownTrain. Valid types are: Tube, SouthWestRail, Eurostar"
        )

    def test_static_method_sufficient_carriage_capacity(self):
        result = Train.calculate_carriage_capacity(28, 20)  # 28 seats, 20 passengers
        self.assertEqual(result, "Sufficient")

    def test_static_method_insufficient_carriage_capacity(self):
        result = Train.calculate_carriage_capacity(28, 30)  # 28 seats, 30 passengers
        self.assertEqual(result, "Insufficient")

    def test_valid_train_type_eurostar(self):
        train = Train("Eurostar", 3)  # 3 carriages, each with 80 seats
        result = train.calculate_capacity(240)  # 3 * 80 = 240 capacity
        self.assertEqual(result, "Sufficient")

    def test_edge_case_zero_passengers(self):
        train = Train("Tube", 3)  # 3 carriages, each with 28 seats
        result = train.calculate_capacity(0)  # No passengers
        self.assertEqual(result, "Sufficient")

    def test_edge_case_no_carriages(self):
        train = Train("Tube", 0)  # 0 carriages, no capacity
        result = train.calculate_capacity(10)  # Passengers present
        self.assertEqual(result, "Insufficient")

    def test_edge_case_max_capacity(self):
        train = Train("Tube", 6)  # 6 carriages, each with 28 seats
        result = train.calculate_capacity(168)  # 6 * 28 = 168
        self.assertEqual(result, "Sufficient")

    def test_beyond_max_capacity(self):
        train = Train("Eurostar", 2)  # 2 carriages, each with 80 seats
        result = train.calculate_capacity(170)  # 2 * 80 = 160; 170 exceeds
        self.assertEqual(result, "Insufficient")


if __name__ == "__main__":
    unittest.main()
