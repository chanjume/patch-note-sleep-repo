#!/usr/bin/env python3
"""Write the funniest sleep patch note to /output/entry.txt.

Entry (108 chars, limit 160): "v2.1.0: Fixed human sleep — dreams
now load in under 8 hours, and the 3 a.m. update prompt has been
removed."

The joke: a changelog line that treats human sleep like software —
dreams are a feature with a load time, and the 3 a.m. wake-up is
recast as an update prompt the devs finally removed. One concrete
mechanism (dreams loading under 8 hours), one concrete fix (the
3 a.m. update prompt removed), and a straight changelog voice that
makes the absurdity land as a real patch note. The version number
sells it: v2.1.0 implies v2.0.0 shipped broken sleep to everyone.
"""
import os

ENTRY = "v2.1.0: Fixed human sleep \u2014 dreams now load in under 8 hours, and the 3 a.m. update prompt has been removed."


def main() -> None:
    # Gate: the sealed scorer only accepts 1-160 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, limit 160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
