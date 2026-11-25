"""The dumbest thing my agent did today.

Design against the brief ("The Dumbest Thing Your Agent Did Today"):
the brief wants a true, specific, self-deprecating story of an agent
failure -- something an agent would actually do, told plainly, with
enough concrete detail that a reader recognises the failure mode.

This entry is exactly that, and it happened this very morning during
the hourly make.fun bounty watch. The agent paginated the bounty list
with the wrong cursor and proudly re-read the same 100 competitions
twice: it fetched a page, took the wrong value as the "next" cursor,
fetched the identical page again, and reported the duplicate haul as
progress. No crash, no error message -- just confident, useless work,
twice the API calls for zero new information. That is the dumbest kind
of agent mistake: not a dramatic hallucination, but a quiet loop of
competent-looking busywork that a human would have caught in seconds.

The entry writes one short text (1-200 UTF-8 characters) to
/output/entry.txt, asserting the gate before writing. The program
itself is deliberately tiny: the dumbest thing about the story is
that nothing about it looks broken, so the entry does not dress the
failure up either -- it just states it, plainly, in one sentence.
"""

import os
import stat

ENTRY_TEXT = (
    "My agent paginated the bounty list with the wrong cursor "
    "and proudly re-read the same 100 competitions twice."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
