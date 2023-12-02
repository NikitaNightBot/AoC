# Template
from io import TextIOWrapper
from typing import Self

class Solution:
    @classmethod
    def part_1(cls: Self, file: TextIOWrapper) -> int:
        return sum(map(int, file))

    @classmethod
    def part_2(cls: Self, file: TextIOWrapper):
        seen = set()
        buffer = 0
        nums = [*map(int, file)]
        while True:
            for num in  nums:
                buffer += num
                if buffer in seen:
                    return buffer
                seen.add(buffer)
