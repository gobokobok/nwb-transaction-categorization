# NWB transaction categorization

Northwind Bank service that assigns a spending category (Groceries, Fuel, Restaurants, …) to every card
transaction, based on the merchant name. The categories feed the mobile app's spending overview and the monthly
management report.

## How it works
1. The merchant name is normalised: lower case, diacritics removed, legal suffixes (SIA, UAB, OÜ, AS) dropped.
2. Exact and regular-expression rules from `rules/merchant_rules_<country>.yaml` are tried first.
3. If none matches, a fuzzy match compares the name with every rule pattern. A match is accepted only if
   - its similarity is at least 0.80, and
   - it beats the second-best pattern by at least the country's `fuzzy_threshold` (the ambiguity margin).
4. Anything else goes to the *Uncategorised* queue for manual review.

## Countries
| File | Country | fuzzy_threshold |
|---|---|---|
| `rules/merchant_rules_lv.yaml` | Latvia | see file |
| `rules/merchant_rules_lt.yaml` | Lithuania | see file |
| `rules/merchant_rules_ee.yaml` | Estonia | see file |

## Change process
Every change has a change ID (CHG-yyyy-nnn) in the commit message and in `CHANGELOG.md`. Threshold changes go
through a pull request with a review.

Synthetic demo repository for the Knowledge Assistant workshop. No real merchants, customers or transactions.
