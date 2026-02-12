#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        line = ""
        for j in range(1, 11):
            line += f"{i * j:>2}"
            line += "\t"
        line.rstrip()
        print(f"{line}")

if __name__ == "__main__":
    main()
