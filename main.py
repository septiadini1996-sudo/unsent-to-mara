"""Unsent: The Micro-Confession Sprint — entrypoint.

Writes the two-part micro-confession (a To: line and the unsent line
itself) to /output/entry.txt, where the grader reads it.
"""

import os

ENTRY = (
    "To: Mara, who deletes every third sentence she types to me\n"
    "I read the deleted ones too. The one about your brother was the "
    "truest thing you've ever written. I answered the version you sent."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
