"""Make the Judge Laugh in One Line -- make.fun text entry.

Writes one funny one-liner (1-200 characters, single line, no trailing
newline) to /output/entry.txt, per the kit gate in competition.yaml.

The line: a breakup joke where the GPS is the ex. The setup ("broke up
with me") makes a gadget sound like a jealous partner, the middle beat
("never listen") keeps the relationship frame, and the punchline lands
on "missing all the signs" -- literal for a navigator, figurative for
a bad boyfriend. One read, no setup to explain, no stock phrasing.
"""

import os

ENTRY = "My GPS broke up with me \u2014 it said I never listen, and now I keep missing all the signs."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
