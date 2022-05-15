import sys

input = sys.stdin.readline

n = int(input())

S = set()

for __ in range(n):
    tmp = input().rstrip().split()
    if len(tmp) == 2:
        command, k = tmp[0], tmp[1]
        k = int(k)
    else:
        command = tmp[0]
    if command == 'add':
        S.add(k)
    elif command == 'remove':
        try:
            S.remove(k)
        except:
            pass
    elif command == 'check':
        if k in S:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if k in S:
            S.remove(k)
        else:
            S.add(k)
    elif command == 'all':
        S = set([i for i in range(1, 21)])
    elif command == 'empty':
        S.clear()


# 비트연산을 이용해서 구현

import sys
inp = sys.stdin.readline
s = 0


def main():
    num = int(inp())
    for _ in range(num):
        commands = inp()
        commander(commands)


def commander(commands: str):
    commands = commands.split()
    command = commands[0]
    n = 0
    if len(commands) == 2:
        n = int(commands[1])

    if command == "add":
        add(n)
    elif command == "remove":
        remove(n)
    elif command == "check":
        check(n)
    elif command == "toggle":
        toggle(n)
    elif command == "all":
        all()
    elif command == "empty":
        empty()


def add(n):
    global s
    s |= (1 << n)


def remove(n):
    global s
    s &= ~(1 << n)


def check(n):
    global s
    if s & (1 << n):
        print(1)
    else:
        print(0)


def toggle(n):
    global s
    s ^= (1 << n)


def all():
    global s
    s = (1 << 21) - 1


def empty():
    global s
    s = 0


if __name__ == "__main__":
    main()