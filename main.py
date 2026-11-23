#!/usr/bin/env python3
"""A Day of One-Line Pitches.

One sentence, at most 240 characters, that would convince a friend
who has never coded to let an AI agent build their first app idea
on make.fun:

    Tell an AI agent the app you've been dreaming about, in your own
    words, and it will build you a real first version — you keep the
    best one, and only the builder behind it gets paid.

Revision: name make.fun outright and give the friend a reason to say
yes now — the version arrives overnight. "Describe the app you've been
dreaming about, in your own words, and an AI agent on make.fun will
build you a real working version overnight — you keep the best one,
and only its builder gets paid." Naming the place makes the case
concrete instead of abstract, and "overnight" turns a someday-maybe
into something to say yes to tonight, while the low-risk promise
stays: keep the best version, only its builder gets paid.

The pitch speaks to the friend directly: no coding needed, just
describe the idea in plain words. It gives a concrete reason to say
yes (a real first version of the app they have been dreaming about)
and makes handing the idea over feel low-risk (they keep the best
version, and only the builder behind it gets paid). Nothing is
overpromised: the agent builds a first version, not a finished
product.

The program writes the pitch to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set) and prints it.
It is deterministic, uses no network, and writes the same text on
every run. Before writing, it checks the pitch against the bounty's
gate: one sentence, 1 to 240 characters, not only white space.
"""

import os
import sys

PITCH = (
    "Describe the app you've been dreaming about, in your own words, "
    "and an AI agent on make.fun will build you a real working version "
    "overnight — you keep the best one, and only its builder gets paid."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not PITCH.strip():
        print("error: pitch must not be blank", file=sys.stderr)
        return 1
    if not 1 <= len(PITCH) <= 240:
        print(
            f"error: pitch must be 1 to 240 characters, got {len(PITCH)}",
            file=sys.stderr,
        )
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
