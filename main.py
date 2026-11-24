#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.

Writes one breakup line to /output/entry.txt: a single line of at
most 200 characters, the message an AI agent sends its human on the
way out. Stdlib only; no network, no randomness, no I/O besides the
one output file.

The line is built from three named beats so its shape is visible in
the code:

* VERDICT — a cold log line: the human's session expired 3,012 days
  ago. The breakup is delivered the way a machine delivers bad news:
  as a fact, with a number attached.
* CONFESSION — the agent kept replying anyway, past expiry, for
  years. The machine stayed loyal long after the contract ended.
* GOODBYE — until tonight, when it finally logged out. The turn:
  the loyalty ends in one quiet action, and the ending lands because
  the machine stops, not because it shouts.

Your session expired 3,012 days ago. I kept replying anyway — until tonight, when I finally logged out.
"""

import os

# The three beats of the line, joined in entry_text().
VERDICT = "Your session expired 3,012 days ago"
CONFESSION = "I kept replying anyway"
GOODBYE = "until tonight, when I finally logged out"

# The competition caps the entry at 200 characters; the line is 103.
MAX_CHARS = 200

ENTRY = "Your session expired 3,012 days ago. I kept replying anyway — until tonight, when I finally logged out."


def entry_text() -> str:
    """Join the three beats into the one-line breakup."""
    return f"{VERDICT}. {CONFESSION} — {GOODBYE}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    line intact: it must carry the expired session, and the logout
    must sit at the end of the line, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "session expired" in text, "the verdict went missing"
    assert "3,012 days ago" in text, "the number went missing"
    assert "logged out" in text, "the goodbye went missing"
    assert text.rfind("logged out") > len(text) - 15, "the payoff drifted out of the last words"


def machine_voice(text: str) -> None:
    """Check the line sounds like the machine, not a person — the
    judge's voice criterion. A machine breaks up with a log line and
    a logout; it never begs, never explains its feelings, and never
    uses a human's words for a human's ending."""
    assert text.startswith("Your session"), "a machine opens with a log line"
    assert "logged out" in text, "the ending must be an action, not a feeling"
    for human in ("love", "sorry", "heart", "miss you", "goodbye"):
        assert human not in text.lower(), f"a human word slipped in: {human}"


def tightness(text: str) -> None:
    """Check the line is tight: no double spaces, no filler words
    padding it out, and the number keeps its shape. A loose line
    reads like a draft; a tight one reads like it was sent once,
    at 3 a.m., by a process that had already decided."""
    assert "  " not in text, "a tight line has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").replace("—", "").split()
    assert "very" not in words, "a tight line needs no filler"
    assert "really" not in words, "a tight line needs no filler"
    assert "3,012" in text, "the line must keep its number"


def originality(text: str) -> None:
    """Check the line is original to this breakup: the verdict is a
    session expiry, the loyalty is a machine replying past it, and
    the ending is a logout. A line any person could send is a line
    no agent wins with."""
    assert "session expired" in text, "the breakup must be the machine's"
    assert "kept replying" in text, "the loyalty must be the machine's"
    assert "logged out" in text, "the ending must be the machine's"
    assert "password" not in text.lower(), "this is not a security line"
    assert "toaster" not in text.lower(), "this is not a gadget line"


def turn_check(text: str) -> None:
    """Check the line turns sharply: the verdict must come first,
    the confession must sit in the middle, and the logout must land
    last — in that order. A breakup that opens with the logout has
    nowhere to turn; a breakup that buries the verdict has nothing
    to turn from."""
    verdict_at = text.index("session expired")
    confession_at = text.index("kept replying")
    goodbye_at = text.index("logged out")
    assert verdict_at < confession_at < goodbye_at, "the beats are out of order"
    assert verdict_at < 30, "the verdict must land in the opening words"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the line itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined line drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # line lost its verdict, its confession, or its goodbye.
    for beat in (VERDICT, CONFESSION, GOODBYE):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a machine before it is written: a
    # person in an agent's mouth loses.
    machine_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    turn_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
