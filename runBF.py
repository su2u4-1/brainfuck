from sys import argv
from typing import Any


class my_dict(dict[int, int]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def __getitem__(self, key: int) -> int:
        if key not in self:
            self[key] = 0
        return super().__getitem__(key)

    def __setitem__(self, key: int, value: int) -> None:
        super().__setitem__(key, value % 256)


flag = True
if len(argv) > 1:
    if argv[1].endswith(".bf"):
        path = argv[1]
    else:
        print(f"Error: {argv[1]} is not brainfuck file.")
        exit()
else:
    path = input()
    if path == "source":
        flag = False

if flag:
    with open(path, "r") as f:
        source = f.readlines()
else:
    source = [input()]

code = ""
brackets: dict[int, int] = {}
stack: list[int] = []
n = 0
repeat = 1
for l in source:
    for c in l:
        if c in "0123456789":
            repeat = int(c)
        if c in "<>+-,.[]":
            if c == "[":
                repeat = 1
                stack.append(n)
            elif c == "]":
                repeat = 1
                t = stack.pop()
                brackets[n] = t
                brackets[t] = n
            code += c * repeat
            n += repeat
            repeat = 1
        elif c == "*":
            break
code += "E"

space = my_dict({0: 0})
point = 0

n = 0
i = "S"
while i != "E":
    i = code[n]
    match i:
        case ">":
            point += 1
        case "<":
            point -= 1
        case "+":
            space[point] += 1
        case "-":
            space[point] -= 1
        case ".":
            print(chr(space[point]), end="")
        case ",":
            space[point] = ord(input())
        case "[":
            if space[point] == 0:
                n = brackets[n]
                continue
        case "]":
            if space[point] != 0:
                n = brackets[n]
                continue
        case "E":
            break
        case _:
            pass
    n += 1
