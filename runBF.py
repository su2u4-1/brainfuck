import sys


class my_dict(dict):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __getitem__(self, key: int) -> int:
        if key not in self:
            self[key] = 0
        return super().__getitem__(key)

    def __setitem__(self, key: int, value: int) -> None:
        super().__setitem__(key, value % 256)


args = sys.argv
if len(args) > 1:
    if args[1].endswith(".bf"):
        path = args[1]
    else:
        print(f"Error: {args[1]} is not brainfuck file.")
else:
    path = input()

with open(path, "r") as f:
    source = f.readlines()

code = ""
brackets = {}
stack = []
n = 0
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
    n += 1
