# aoc_run

```yaml
A python module for running AOC solutions with a certain project structure being:

solutions/
    year/
        problem_num/
            input # problem input file, the file handle object (TextIOWrapper) will be automatically provided as the 1st positional arg (after cls)
            solution.py 
                # --- 
                class Solution:
                    @classmethod
                    def part_1(cls, file)

                    @classmethod
                    def part_2(cls, file)
                # ---

Run via: run.py {year} {problem_num} {part} [you can provide additional args and kwargs, check --help]
```
