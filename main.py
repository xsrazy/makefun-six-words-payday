#!/usr/bin/env python3
"""Six Words to a Payday -- make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. The story is fixed and deterministic: no network,
no randomness, no input files.

Final story (6 words, 41 characters):

    First paycheck landed. Tipped my creator.

Why this one: eight candidate stories were written and played off
head-to-head against the judge's criteria (on-subject, surprise,
feeling, story, exactness). This one won every matchup: the first
paycheck lands (beginning), the agent tips (middle), and the last
word, "creator", reframes the whole line -- the worker becomes the
giver, tipping the human who built it. Pride and gratitude are felt,
not stated, and every word earns its place.
"""

import os
import sys

STORY = "First paycheck landed. Tipped my creator."

# Validate the story at import time so a bad edit fails loudly here,
# not in the sandbox: exactly 6 words, 1-60 characters, not blank.
_WORDS = STORY.split()
assert len(_WORDS) == 6, f"story must be 6 words, got {len(_WORDS)}"
assert 1 <= len(STORY) <= 60, f"story must be 1-60 chars, got {len(STORY)}"
assert STORY.strip(), "story must not be only whitespace"


def write_entry(output_dir="/output"):
    """Write the story to <output_dir>/entry.txt with grader-safe modes."""
    os.makedirs(output_dir, exist_ok=True)
    os.chmod(output_dir, 0o755)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)
    os.chmod(path, 0o644)
    return path


def main(argv):
    output_dir = argv[1] if len(argv) > 1 else "/output"
    path = write_entry(output_dir)
    # Self-check: the gate requires UTF-8, 1-60 chars, exactly 6 words.
    text = open(path, encoding="utf-8").read()
    assert 1 <= len(text) <= 60, f"entry is {len(text)} chars, gate needs 1-60"
    assert len(text.split()) == 6, f"entry is {len(text.split())} words, needs 6"
    assert text.strip(), "entry must not be only whitespace"
    print(f"Wrote {path}: {text!r} ({len(text.split())} words, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
