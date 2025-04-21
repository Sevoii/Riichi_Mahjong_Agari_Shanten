import re

PATTERN = r"([1-9]+[mps]|[1-7]+z)"
OFFSETS = {
    "m": 0,
    "p": 9,
    "s": 18,
    "z": 27
}


def construct_hand(s: str):
    h = [0 for i in range(34)]

    for i in re.findall(PATTERN, s):
        offset = OFFSETS[i[-1]]

        for j in i[:-1]:
            h[offset + int(j) - 1] += 1

    return h
