#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word: the word an ex would use to describe you.

REVISED word: "roommate".
Why it beats the v1 draft ("exhausting"): "exhausting" is a generic
adjective any ex could say about anyone, swappable with tiring /
draining with nothing lost. "roommate" is a sharp turn — it does not
describe a trait, it reclassifies the whole relationship: you were
not a partner, you were a roommate. One word delivers the demotion,
the shared flat, the separate lives, the dead intimacy. It is the
exact word people actually say ("he was basically my roommate"),
it stings because it is painfully true, it lands instantly with no
explanation, and no near synonym keeps its edge ("flatmate" /
"housemate" sound like a listing, not a verdict). Relatable to
anyone who has lived through a relationship quietly becoming
a co-tenancy.
"""
import os

WORD = "roommate"


def main():
    word = WORD.strip()
    # Gate: exactly one word, 1-24 characters, no whitespace inside.
    assert word and len(word) <= 24 and len(word.split()) == 1, word
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
