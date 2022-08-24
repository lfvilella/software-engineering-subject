from functools import cached_property
from typing import Tuple

import utils
from types_ import NUMBER_TYPE, NUMBERS_TYPE


class MaxMin:
    def __init__(self, numbers: NUMBERS_TYPE):
        self.numbers = numbers
        self._validate_numbers_input()

    def _validate_numbers_input(self):
        utils.validate_numbers(self.numbers)

    @cached_property
    def max_pythonic(self):
        return max(self.numbers)

    def max_hard_rock(self) -> NUMBER_TYPE:
        max_number = self.numbers[0]
        for number in self.numbers:
            if max_number < number:
                max_number = number
        return max_number

    @cached_property
    def max(self):
        return self.max_hard_rock()

    @cached_property
    def min_pythonic(self):
        return min(self.numbers)

    def min_hard_rock(self) -> NUMBER_TYPE:
        max_number = self.numbers[0]
        for number in self.numbers:
            if max_number > number:
                max_number = number
        return max_number

    @cached_property
    def min(self):
        return self.min_hard_rock()

    def process(self) -> Tuple[NUMBER_TYPE, NUMBER_TYPE]:
        return self.max, self.min
