from unittest import TestCase

from logic.nearby import meters_to_walking_time


class Nearby(TestCase):

    @staticmethod
    def test_meters_to_walking_time_integer_result():
        assert 1 == meters_to_walking_time(80)

    @staticmethod
    def test_meters_to_walking_time_floating_result():
        assert 1 == meters_to_walking_time(81)

    @staticmethod
    def test_meters_to_walking_time_zero_edge_case():
        assert 0 == meters_to_walking_time(79)

    @staticmethod
    def test_meters_to_walking_time_floating_param():
        assert 1 == meters_to_walking_time(80.5)

    @staticmethod
    def test_meters_to_walking_time_floating_param():
        assert -1 == meters_to_walking_time(None)