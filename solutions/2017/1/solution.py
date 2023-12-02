# Template
from io import TextIOWrapper
from typing import Self, Callable

class Solution:
    @classmethod
    def solve(cls: Self, file: TextIOWrapper, stepfunc: Callable[[list[int]], int]) -> int:
        nums = [*map(int, file.read().strip())]
        step = stepfunc(nums)
        length = len(nums)
        rs = 0
        for index, left in enumerate(nums):
            right = nums[(index+step)%length]
            if left==right:
                rs += left
        return rs

    @classmethod
    def part_1(cls: Self, file: TextIOWrapper) -> int:
        return cls.solve(file, lambda l:1) 

    @classmethod
    def part_2(cls: Self, file: TextIOWrapper) -> int:
        return cls.solve(file, lambda l:len(l)//2)

