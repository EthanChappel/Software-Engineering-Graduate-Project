import unittest
from datetime import datetime, timedelta, timezone
from big_number_computation import big_number_computation, to_int
from date_time_transformation import transform_datetime
from string_and_words import word_count, word_replacement, grep_line


# Big Number Computation
class BigNumberComputationTests(unittest.TestCase):
    def test_to_int_normal_positive(self):
        self.assertEqual(to_int("1"), 1)

    def test_to_int_big_positive(self):
        self.assertEqual(
            to_int("100000000000000000000000000000000000000000"),
            100000000000000000000000000000000000000000
        )

    def test_to_int_normal_negative(self):
        self.assertEqual( to_int("-1"), -1)

    def test_to_int_big_negative(self):
        self.assertEqual(
            to_int("-100000000000000000000000000000000000000000"),
            -100000000000000000000000000000000000000000
        )

    def test_to_int_zero(self):
        self.assertEqual(to_int("0"), 0)

    def test_big_number_computation_normal_addition(self):
        self.assertEqual(big_number_computation("2", "+", "1"), "3")

    def test_big_number_computation_normal_subtraction(self):
        self.assertEqual(big_number_computation("2", "-", "1"), "1")

    def test_big_number_computation_normal_multiplication(self):
        self.assertEqual(big_number_computation("2", "*", "1"), "2")

    def test_big_number_computation_big_addition(self):
        self.assertEqual(
            big_number_computation(
                "200000000000000000000000000000000000000000",
                "+",
                "100000000000000000000000000000000000000000"
            )
           , "300000000000000000000000000000000000000000"
        )

    def test_big_number_computation_big_subtraction(self):
        self.assertEqual(
            big_number_computation(
                "200000000000000000000000000000000000000000",
                "-",
                "100000000000000000000000000000000000000000"
            ),
            "100000000000000000000000000000000000000000"
        )

    def test_big_number_computation_big_multiplication(self):
        self.assertEqual(
            big_number_computation(
                "200000000000000000000000000000000000000000",
                "*",
                "100000000000000000000000000000000000000000"
            ),
            "20000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        )


# Datetime transformation

class DateTimeTransformationTests(unittest.TestCase):
    def setUp(self):
        self.f = '%Y-%m-%dT%H:%M:%S%z'

    def test_transform_datetime_outside_dst(self):
        self.assertEqual(
            transform_datetime(
                datetime.strptime("2000-01-01T00:00:00+0000", self.f),
                -6,
                datetime.strptime("2000-03-01T00:00:00+0000", self.f),
                datetime.strptime("2000-11-01T00:00:00+0000", self.f)
            ),
            datetime(1999, 12, 31, 18, 0, 0, tzinfo=timezone(timedelta(hours=-6)))
        )

    def test_transform_datetime_inside_dst(self):
        self.assertEqual(
            transform_datetime(
                datetime.strptime("2000-07-01T00:00:00+0000", self.f),
                -6,
                datetime.strptime("2000-03-01T00:00:00+0000", self.f),
                datetime.strptime("2000-11-01T00:00:00+0000", self.f)
            ),
            datetime(2000, 6, 30, 19, 0, 0, tzinfo=timezone(timedelta(hours=-6)))
        )

    def test_transform_datetime_start_dst(self):
        d = datetime.strptime("2000-03-01T00:00:00+0000", self.f)
        self.assertEqual(
                transform_datetime(
                d,
                -6,
                d,
                datetime.strptime("2000-11-01T00:00:00+0000", self.f)
            ),
            datetime(2000, 2, 29, 19, 0, 0, tzinfo=timezone(timedelta(hours=-6)))
        )

    def test_transform_datetime_end_dst(self):
        d = datetime.strptime("2000-11-01T00:00:00+0000", self.f)
        self.assertEqual(
            transform_datetime(
                d,
                -6,
                datetime.strptime("2000-03-01T00:00:00+0000", self.f),
                d,
            ),
            datetime(2000, 10, 31, 18, 0, 0, tzinfo=timezone(timedelta(hours=-6)))
        )


# String and words

class StringAndWords(unittest.TestCase):
    def setUp(self):
        self.test_text = "The cosmos is all that is...\n...or ever was or ever will be."

    def test_word_count(self):
        self.assertEqual(
            word_count(self.test_text),
            {
                'The': 1,
                'cosmos': 1,
                'is': 2,
                'all': 1,
                'that': 1,
                'or': 2,
                'ever': 2,
                'was': 1,
                'will': 1,
                'be': 1
            }
        )

    def test_word_replacement(self):
        self.assertEqual(
            word_replacement('cosmos', 'universe', self.test_text),
            "The universe is all that is...\n...or ever was or ever will be."
        )

    def test_grep_line(self):
        self.assertEqual(
            grep_line("cosmos", self.test_text),
            [' 1:  The cosmos is all that is...']
        )


if __name__ == '__main__':
    unittest.main()