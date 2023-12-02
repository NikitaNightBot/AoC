# Template
from io import TextIOWrapper
from typing import Self

class Solution:
    @classmethod
    def part_1(cls: Self, file: TextIOWrapper):
        rs = 0
        for line in file:
            la,sm=0,float('+inf')
            for n in map(int, line.split()):
                la=max(la,n)
                sm=min(sm,n)
            rs += la - sm
        return rs

    @classmethod
    def part_2(cls: Self, file: TextIOWrapper):
        rs = 0
        for line in file:
            numbers = [*map(int, line.split())]
            flag = False
            for i_index, i_number in enumerate(numbers):
                if flag:
                    break
                for j_index, j_number in enumerate(numbers):
                    if i_index == j_index:
                        continue 
                    if i_number%j_number==0:
                        rs += i_number/j_number
                        flag = True
                        break
        return int(rs)
                        
                        