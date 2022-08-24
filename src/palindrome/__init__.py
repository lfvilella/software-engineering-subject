import re
from functools import cached_property


class Palindrome:
    VALID_ALPHABETIC_REGEX = r'[a-zA-Z]+'

    def __init__(self, text: str):
        self.text = text
        self._validate_string_input()

    def _validate_string_input(self):
        if not self.text:
            raise ValueError(f"The param 'numbers' cannot be empty")
        if not isinstance(self.text, str):
            raise ValueError(
                f"Expected string as a param but got '{type(self.text)}'")
        if not bool(re.match(self.VALID_ALPHABETIC_REGEX, self.text)):
            raise ValueError("The text is not alphabetic")

    @cached_property
    def text_formatted(self) -> str:
        return self.text.strip().lower()

    def is_palindrome(self) -> bool:
        return self.text_formatted == self.text_formatted[::-1]
