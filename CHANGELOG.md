# Changelog

Newest first. Every entry has its change ID.

## CHG-2026-016 (live)
- EE: rule for new merchant Saare Pagarid (bakery chain) as Groceries; about 120 transactions per week were landing in Uncategorised.

## CHG-2026-014 (2026-10-28)
- LT: fuzzy-match threshold raised from 0.15 to 0.20 after false positives on new e-commerce merchants.
  October sample: false positives 37 → 4, uncategorised share 1.8% → 2.1%. LV and EE unchanged.

## CHG-2026-013 (2026-10-20)
- Audit line for every fuzzy decision (score and margin) for the monthly rule review.

## CHG-2026-012 (2026-10-07)
- LT: rules for e-commerce marketplaces (ShopLT Market, Baltic Parcel Shop, Kaunas Online).

## CHG-2026-011 (2026-09-24)
- EE: new category *Fast food*, split from *Restaurants* (Burger Saar moved).

## CHG-2026-010 (2026-09-10)
- Normalisation removes diacritics and legal suffixes (SIA, UAB, OÜ, AS) before matching.

## CHG-2026-009 (2026-08-29)
- LV: rules for fuel stations (Ziemeļu Degviela, Vidzemes DUS).

## CHG-2026-008 (2026-08-18)
- Initial categorization service: normalisation, exact/regex rules, fuzzy match with an ambiguity margin.
- Rules for LV, LT and EE (`fuzzy_threshold` 0.15 everywhere).
