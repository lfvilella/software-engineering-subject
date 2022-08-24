import copy

import utils
from types_ import NUMBERS_TYPE


class BubbleSort:
    def __init__(self, numbers: NUMBERS_TYPE):
        self.numbers = numbers
        self._validate_numbers_input()

    def _validate_numbers_input(self):
        utils.validate_numbers(self.numbers)

    @staticmethod
    def _swap(x, y, numbers):
        numbers[y], numbers[x] = numbers[x], numbers[y]

    def sort(self, inplace: bool = False) -> NUMBERS_TYPE:
        numbers = copy.deepcopy(self.numbers) if not inplace else self.numbers
        len_number = len(numbers) - 1

        swapped = False
        for i in range(len_number):
            for j in range(len_number - i):
                if numbers[j] > numbers[j + 1]:
                    self._swap(j + 1, j, numbers)
                    swapped = True

            if not swapped:
                return numbers

        return numbers
