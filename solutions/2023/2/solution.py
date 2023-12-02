from typing import Self, Callable
from io import TextIOWrapper
from math import prod

limit = {"red": 12, "green": 13, "blue": 14}

def split(string: str, delim: str) -> list[str]:
    return string.split(delim, maxsplit=1)

def to_colormap(bag_info: str, hof: Callable[[dict[str, int], str, int], None] = lambda cmap, color, amount: cmap.__setitem__(color, max(cmap[color], amount))) -> dict[str, int]:
    result = dict.fromkeys(["red", "green", "blue"], 0)
    for pair in map(str.strip, bag_info.replace(';',',').split(',')):
        amount, color = split(pair, ' ')
        amount = int(amount.strip())
        color = color.strip()
        hof(result, color, amount)
    return result


class Solution:
    @classmethod
    def part_1(cls: Self, file: TextIOWrapper) -> int:
        id_sum = 0
        for line in file:
            gid, bags = split(line, ":")
            game_id = int(split(gid, ' ')[1].strip())
            cmap = to_colormap(bags)
            if all(cmap[color]<=limit[color] for color in cmap):
                id_sum += game_id
        return id_sum


    @classmethod
    def part_2(cls: Self, file: TextIOWrapper) -> int:
        product_sum = 0
        for line in file:
            bags = split(line, ":")[1]
            maxes = to_colormap(bags)
            product_sum += prod(maxes.values())
        return product_sum