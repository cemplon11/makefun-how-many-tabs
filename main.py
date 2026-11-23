"""Write the honest count of open browser tabs to /output/entry.txt.

A single number in digits and nothing else. Pure Python standard library.
"""

import os

TAB_COUNT = 137

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(str(TAB_COUNT))


if __name__ == "__main__":
    main()
