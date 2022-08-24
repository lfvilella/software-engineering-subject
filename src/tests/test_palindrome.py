import random

import pytest

from palindrome import Palindrome


class TestPalindrome:
    @staticmethod
    def _run_is_palindrome(text):
        instance = Palindrome(text)
        max_and_min = instance.is_palindrome()
        return max_and_min

    @pytest.mark.parametrize("input_, expected_output",
                             [("arara", True), ("AraRA", True), ("AnA", True),
                              ("not palindrome", False), ("dummy", False)])
    def test_is_palindrome(self, input_, expected_output):
        assert self._run_is_palindrome(input_) == expected_output

    def test_instantiate_with_invalid_alphabetic_raises(self):
        with pytest.raises(ValueError):
            Palindrome('á0é1230d')

    def test_instantiate_with_empty_string_raises(self):
        with pytest.raises(ValueError):
            Palindrome('')

    def test_instantiate_with_number_raises(self):
        random_number = random.uniform(1, 999)
        with pytest.raises(ValueError):
            Palindrome(random_number)
