import copy

import pytest

from bubble_sort import BubbleSort


class TestBubbleSort:
    @staticmethod
    def _run_bubble_sort(values):
        instance = BubbleSort(values)
        numbers_sorted = instance.sort()
        return numbers_sorted

    def test_sort_numbers(self):
        numbers = [64.11, 34, 25.44, 12, 22, 11, 90]
        numbers_sorted = self._run_bubble_sort(numbers)
        assert numbers_sorted != numbers

        expected_numbers = [11, 12, 22, 25.44, 34, 64.11, 90]
        assert numbers_sorted == expected_numbers

    def test_sort_numbers_reverted(self):
        numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        numbers_sorted = self._run_bubble_sort(numbers)
        assert numbers_sorted != numbers

        assert numbers_sorted == numbers[::-1]

    def test_sort_letters_raises(self):
        letters = ['a', 'd', 'b', 'z', 'c', 'j']
        with pytest.raises(ValueError):
            self._run_bubble_sort(letters)

    def test_sort_sort_empty_list_raises(self):
        with pytest.raises(ValueError):
            self._run_bubble_sort([])

    def test_sort_mix_of_letter_and_numbers_raises(self):
        """
        Raises:
            '>' not supported between instances of 'int' and 'str'
        """
        mix_values = [64, 'a', 25, 'b', 22, 'c', 90]
        with pytest.raises(ValueError):
            self._run_bubble_sort(mix_values)

    def test_sort_numbers_already_sorted(self):
        numbers = [11, 12, 22, 25, 34, 64, 90]
        numbers_sorted = self._run_bubble_sort(numbers)
        assert numbers_sorted == numbers

    def test_sort_numbers_inplace(self):
        numbers = [64, 34, 25, 12, 22, 11, 90]
        numbers_copied = copy.deepcopy(numbers)

        instance = BubbleSort(numbers)
        numbers_sorted = instance.sort(inplace=True)
        assert numbers_sorted != numbers_copied
        assert numbers_sorted == numbers
        expected_numbers = [11, 12, 22, 25, 34, 64, 90]
        assert numbers_sorted == expected_numbers
