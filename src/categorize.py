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


LEGAL_SUFFIXES = ("sia", "uab", "ou", "as")


def normalise(name: str) -> str:
    """Lower case, no diacritics, no legal suffixes, single spaces."""
    plain = unicodedata.normalize("NFKD", name.lower()).encode("ascii", "ignore").decode()
    words = [w.strip(".,") for w in plain.split()]
    return " ".join(w for w in words if w not in LEGAL_SUFFIXES)


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
    accepted = best[0] >= MIN_SIMILARITY and best[0] - second[0] >= rules["fuzzy_threshold"]
    log_match(name, "fuzzy", best[0], best[0] - second[0], accepted)
    return best[1] if accepted else "Uncategorised"


def log_match(name: str, method: str, score: float, margin: float, accepted: bool) -> None:
    """Audit line per fuzzy decision (method, score, margin) for the monthly rule review."""
    print(f"match name={name!r} method={method} score={score:.3f} margin={margin:.3f} accepted={accepted}")
