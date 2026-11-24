"""Write the honest count of open browser tabs to /output/entry.txt.

A single number in digits and nothing else. Pure Python standard library.
"""

import os

# The count below is the number of browser tabs open at the time of
# writing, counted by hand. The entry file must contain exactly this
# number in decimal digits, with no labels, newline, or decoration.
TAB_COUNT = 137

OUTPUT_PATH = "/output/entry.txt"


def render_count() -> str:
    """Return the tab count as plain decimal text for the entry file."""
    return str(TAB_COUNT)


def write_entry(path: str, text: str) -> None:
    """Write ``text`` to ``path``, creating its parent directory."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    text = render_count()
    # Self-check: the rendered text must be exactly the decimal count,
    # so a future edit cannot silently change the entry's format.
    assert text == str(TAB_COUNT) and text.isdigit(), text
    write_entry(OUTPUT_PATH, text)


if __name__ == "__main__":
    main()
