#!/usr/bin/env python3
"""
load_crds.py

Reference loader for the CRDS dataset. Demonstrates how a downstream
researcher should load and access scenario records.

Usage:
    python load_crds.py path/to/crds_v1.0.jsonl
"""

import json
import sys
from pathlib import Path
from collections import Counter


def load_crds(path):
    """Load CRDS as a list of dicts."""
    records = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def filter_by_domain(records, domain):
    """Return all scenarios in a given domain (web_ui, marketing, ...)."""
    return [r for r in records if r["domain"] == domain]


def filter_by_audience(records, audience_id):
    """Return all scenarios for a given audience descriptor (U01..U07)."""
    return [r for r in records if r["audience_id"] == audience_id]


def get_palette_lab(record):
    """Return the gold palette as a list of [L, a, b] triplets."""
    return record["gold_palette_lab"]


def get_palette_hex(record):
    """Return the gold palette as a list of hex codes."""
    return record["gold_palette_hex"]


def summary(records):
    """Print a quick summary of the dataset."""
    print(f"Total scenarios: {len(records)}")
    print()
    print("By domain:")
    for d, n in Counter(r["domain"] for r in records).most_common():
        print(f"  {d:15s}  {n:4d}")
    print()
    print("By audience:")
    for a, n in Counter(r["audience_id"] for r in records).most_common():
        print(f"  {a:5s}  {n:4d}")
    print()
    kappas = [r["annotator_kappa"] for r in records]
    if kappas:
        avg = sum(kappas) / len(kappas)
        print(f"Mean per-scenario kappa: {avg:.3f}")
        print(f"Min / Max:               {min(kappas):.3f} / {max(kappas):.3f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    path = Path(sys.argv[1])
    records = load_crds(path)
    summary(records)
    print()
    print("First record:")
    print(json.dumps(records[0], indent=2, ensure_ascii=False))
