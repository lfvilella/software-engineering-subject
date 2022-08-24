import pytest

from max_and_min_values import MaxMin


class TestMaxMin:
    @staticmethod
    def _run_max_min(values):
        instance = MaxMin(values)
        max_and_min = instance.process()
        return max_and_min

    def test_max_and_min(self):
        numbers = [64.11, 34, 25.44, 12, 22, 11, 90]
        max_and_min = self._run_max_min(numbers)
        assert max_and_min == (90, 11)

    def test_max(self):
        numbers = [64.11, 34, 25.44, 12, 22, 11, 90]
        instance = MaxMin(numbers)
        assert instance.max == 90

    def test_min(self):
        numbers = [64.11, 34, 25.44, 12, 22, 11, 90]
        instance = MaxMin(numbers)
        assert instance.min == 11

    def test_max_and_min_with_one_item_on_list(self):
        number = 100
        max_and_min = self._run_max_min([number])
        assert max_and_min == (number, number)

    def test_instantiate_with_empty_list_raises(self):
        invalid_input = []
        with pytest.raises(ValueError):
            MaxMin(invalid_input)

    def test_instantiate_with_letters_raises(self):
        invalid_input = ['a', 'b', 'c']
        with pytest.raises(ValueError):
            MaxMin(invalid_input)

    def test_instantiate_with_mix_of_numbers_and_letters_raises(self):
        invalid_input = [22, 'a', 55.123, 'b', 0.99, 'c']
        with pytest.raises(ValueError):
            MaxMin(invalid_input)

    def test_max_pythonic(self):
        numbers = [64.11, 34, 25.44, 12, 22, 11, 90]
        instance = MaxMin(numbers)
        assert instance.max_pythonic == 90

    def test_min_pythonic(self):
        numbers = [64.11, 34, 25.44, 12, 22, 11, 90]
        instance = MaxMin(numbers)
        assert instance.min_pythonic == 11
