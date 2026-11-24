#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds absurd until the business logic lands.
"""
import os

TEXT = (
    "We rent out stern grandmothers to scold startup founders until they ship "
    "\u2014 $90 an hour, because guilt is the only growth hack that has ever "
    "actually worked."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
