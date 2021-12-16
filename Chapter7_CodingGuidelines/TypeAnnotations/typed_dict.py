from typing import TypedDict
from typing import Union


class Point2D(TypedDict, total=False):
    x: int
    y: int
    label: Union[str, int]


a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
print(a)

b: Point2D = {'x': 1, 'y': 2, 'label': 2}  # OK
print(b)

c: Point2D = {'x': 0, 'label': 'bad'}           # Fails type check
print(c)

print(c.keys(), c.values(), c.items())
