# Template
from io import TextIOWrapper
from typing import Self, Callable

class Solution:
    @staticmethod
    def solve(file: TextIOWrapper, func: Callable[[str], bool]):
        return sum(map(lambda line: len((words:=func(line)))==len(set(words)), file))
        
    @classmethod
    def part_1(cls: Self, file: TextIOWrapper) -> int:
        return cls.solve(file, str.split)

    @classmethod
    def part_2(cls: Self, file: TextIOWrapper) -> int:
        return cls.solve(file, lambda line: [''.join(sorted(word)) for word in line.split()])