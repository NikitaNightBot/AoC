from typing import Iterable, Self
from io import TextIOWrapper

class Solution:
    @staticmethod
    def first_and_last_digits_sum(string_gen: Iterable[str]) -> int:
        rs = 0
        for string in string_gen:
            digits = [int(char) for char in string if char in "0123456789"]
            if digits:
                rs += (digits[0] * 10) + digits[-1]
        return rs

    @staticmethod
    def replace_digitwords(
        line: str,
        mappings: dict[str, str] = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        },
    ) -> str:
        return "".join(
            x
            if (x := "".join(v for k, v in mappings.items() if line[i:].startswith(k)))
            else line[i]
            for i in range(len(line))
        )

    @classmethod
    def part_1(cls: Self, file: TextIOWrapper) -> int:
        return cls.first_and_last_digits_sum(iter(file))

    @classmethod
    def part_2(cls: Self, file: TextIOWrapper) -> int:
        return cls.first_and_last_digits_sum(map(cls.replace_digitwords, iter(file)))
