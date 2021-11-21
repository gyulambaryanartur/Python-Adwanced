import itertools


class NumGroups:
    def __init__(self, *args: tuple):
        self.values = args

    def group_in_tens(self) -> list:
        sorted_args = sorted(self.values)
        groups = [None] * (sorted_args[-1] // 10 + 1)
        for number in sorted_args:
            idx = number // 10
            if groups[idx] is None:
                groups[idx] = []
            groups[idx].append(number)
            
        return groups

    def group_in_10s(self) -> list:
        groups = [None] * (max(self.values) // 10 + 1)
        for idx, group in itertools.groupby(sorted(self.values), lambda item: item // 10):
            groups[idx] = list(group)
        return groups

    def is_colorful(self, idx: int) -> bool:
        digits = list(map(int, str(self.values[idx])))
        tmp = digits + [digits[idx - 1] * digits[idx] for idx in range(1, len(digits))]
        return len(set(tmp)) == len(tmp)


if __name__ == '__main__':
    print(NumGroups(4, 78, 71, 3).group_in_10s())
