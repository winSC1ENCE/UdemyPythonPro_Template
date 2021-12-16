from typing import NamedTuple


class User(NamedTuple):
    name: str
    age: int = 27


user1 = User('Jan')

print(user1)
print(dir(user1))

# user1.age = 30
# print(user1)
