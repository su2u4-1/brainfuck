import sys
from typing import Any


class my_dict(dict):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __getitem__(self, key: int) -> int:
        if key not in self:
            self[key] = 0
        return super().__getitem__(key)

    def __setitem__(self, key: int, value: int) -> None:
        if -128 <= value <= 127:
            return super().__setitem__(key, value)
        value = value & 0xFF
        if value > 127:
            value -= 256
        return super().__setitem__(key, value)


args = sys.argv
if len(args) > 1 and args[1].endswith == "bf":
    with open(args[1], "r") as f:
        code = ""
        for i in f.read():
            if i in "<>+-,.[]":
                code += i
else:
    print("error")

space = my_dict({0: 0})
point = 0

for i in code:
    match i:
        case ">":
            point += 1
        case "<":
            point -= 1
