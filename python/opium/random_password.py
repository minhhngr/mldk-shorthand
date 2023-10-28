#!/usr/bin/python3
import string
import itertools

result = []
count = 0
char = 6


"""itertools.combinations

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

"""

try:
    letters = string.ascii_letters
    for i in range(0, len(letters) + 1):
        for _combine in itertools.combinations(letters, i):
            if len(_combine) < char:
                continue
            if len(_combine) > char:
                break
            count += 1
            result.append("".join(_combine))
except:
    print(f"Has issues but completed: {count} password with {char} character")
finally:
    print(f"Completed: {count} password with {char} character")
    with open("generate_password.txt", "w+") as _f:
        for _password in result:
            _f.write(_password + "\n")

import random

generate_password = lambda x: "".join(
    [random.choice(string.ascii_letters + string.hexdigits) for _ in range(x)]
)

# line      = 1000 * int(1e3) # Number one created (1 * 1000) = 1000 line
# character = 6            # Number char password

# list_password = [generate_password(character) for _ in range(line)]

# with open('generate_password', 'w+') as _f:
#     for _password in list_password:
#         _f.write(_password + "\n")

# print(f'Đã tạo {line} password, thành công')

# Generate password ascii
