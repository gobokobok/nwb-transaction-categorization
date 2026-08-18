"""Assign a spending category to a card transaction from the merchant name (synthetic demo)."""
from difflib import SequenceMatcher
from pathlib import Path
import re
import unicodedata

import yaml

RULES_DIR = Path(__file__).resolve().parent.parent / "rules"
MIN_SIMILARITY = 0.80


def load_rules(country: str) -> dict:
    with open(RULES_DIR / f"merchant_rules_{country.lower()}.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalise(name: str) -> str:
    return " ".join(name.lower().split())


def categorize(merchant: str, country: str) -> str:
    rules = load_rules(country)
    name = normalise(merchant)
    for rule in rules["rules"]:
        if re.fullmatch(rule["pattern"], name):
            return rule["category"]
    return fuzzy_category(name, rules)


def fuzzy_category(name: str, rules: dict) -> str:
    scores = sorted(((SequenceMatcher(None, name, r["pattern"]).ratio(), r["category"]) for r in rules["rules"]),
                    reverse=True)
    best, second = scores[0], scores[1] if len(scores) > 1 else (0.0, None)
    if best[0] >= MIN_SIMILARITY and best[0] - second[0] >= rules["fuzzy_threshold"]:
        return best[1]
    return "Uncategorised"
