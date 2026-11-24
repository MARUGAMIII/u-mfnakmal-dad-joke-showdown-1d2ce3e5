#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single dad joke (at most 200 characters) to /output/entry.txt.
Stdlib only, no network, deterministic: the same joke every run.
"""

import os

JOKE = "I asked my dog what's two minus two. He said nothing."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Fail loudly instead of shipping an invalid entry.
assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke violates the gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
