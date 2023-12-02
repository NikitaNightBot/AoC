# Template
from io import TextIOWrapper
from typing import Self
from collections import Counter

class Solution:
    @classmethod
    def part_1(cls: Self, file: TextIOWrapper) -> int:
        two = 0
        three = 0
        for line in file:
            counts = Counter(line)
            freq = set(counts.values())
            if 2 in freq:
                two += 1
            if 3 in freq:
                three += 1
        return two*three
             

    @classmethod
    def part_2(cls: Self, file: TextIOWrapper) -> str:
        words = list(map(str.strip, file.readlines()))
        for i_index, i_word in enumerate(words):
            for j_index, j_word in enumerate(words):
                if i_index == j_index:
                    continue
                matching = ''.join(i_word[idx] for idx in range(len(i_word)) if i_word[idx]==j_word[idx])
                if len(matching)==len(i_word)-1:
                    return matching
