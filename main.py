# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            a = opening_brackets_stack.pop()
            if not are_matching(a.char, next):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"


def main():
    print("[!] \tUse an input to choose files or input - F or I ?")
    text = input(">:: \t")
    if text == "F":
        print("[!] \tEnter file name or file path. For example 'test/0'.")
        fileName = input(">:: \t")
        with open(fileName, "r") as file:
            text = file.read().strip()
    elif text == "I":
        print("[!] \tEnter text below.")
        text = input(">:: \t").strip()
    else:
        print("[Err] \tWrong input.")
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
