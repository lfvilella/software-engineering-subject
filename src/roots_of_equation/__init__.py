from functools import cached_property
from typing import Tuple, Optional

import utils
from types_ import NUMBER_TYPE


class SecondDegreeEquation:
    def __init__(self, a: NUMBER_TYPE, b: NUMBER_TYPE, c: NUMBER_TYPE):
        self.a = a
        self.b = b
        self.c = c
        self._validate_numbers_input()

    def _validate_numbers_input(self):
        utils.validate_number(self.a)
        utils.validate_number(self.b)
        utils.validate_number(self.c)

    @cached_property
    def delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def get_roots(self) -> Tuple[Optional[NUMBER_TYPE], Optional[NUMBER_TYPE]]:
        if self.a == 0:
            raise ValueError("The param 'a' cannot be zero")

        root1, root2 = None, None
        if self.delta < 0:
            return root1, root2

        if self.delta == 0:
            root1 = (-self.b + self.delta ** (1 / 2)) / (2 * self.a)
        else:
            root1 = (-self.b + self.delta ** (1 / 2)) / (2 * self.a)
            root2 = (-self.b - self.delta ** (1 / 2)) / (2 * self.a)

        return root1, root2
