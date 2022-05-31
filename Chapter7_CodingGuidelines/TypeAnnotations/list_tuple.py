from __future__ import annotations

from typing import Any
from typing import List
from typing import Tuple
from typing import Union


Number = Union[int, float]


def append_list(lst: List[Number], val: Number) -> None:
    lst.append(val)


def print_3d_tuple(tpl: Tuple[Number, bool, str]) -> None:
    for val in tpl:
        print(val)


if __name__ == "__main__":
    l: List[Union[int, float]] = [1, 2, 3]
    t = (1, True, "")

    append_list(l, 4)
    print_3d_tuple(t)
