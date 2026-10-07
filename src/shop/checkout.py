"""Order checkout.

The rules live in `src/shop/specs/checkout.md` - read it first.
Both functions below are stubs: their signature is final, the bodies are yours.
Do not change the constants: the tests rely on them.
"""

PROMO_CODES = {"WELCOME10": 10, "SUMMER15": 15, "VIP35": 35}
SUPPORTED_CITIES = ("msk", "spb")
MAX_DISCOUNT_PERCENT = 30
VAT_PERCENT = 20
SHIPPING_KOPEKS = 49_000
FREE_DELIVERY_FROM_KOPEKS = 500_000
TIER_DISCOUNTS = ((10, 5), (25, 10), (50, 15))
REQUIRED_LINE_KEYS = ("sku", "qty", "unit_price_kopecks")


def validate_order(
    lines: list[dict[str, str]],
    promo_code: str = "",
    shipping_city: str = "",
) -> str | None:
    """Return a human readable reason why the order is invalid, or None if it is fine."""
    if not lines:
        return "order must contain at least one line"

    seen: set[str] = set()
    for index, item in enumerate(lines, start=1):
        for key in REQUIRED_LINE_KEYS:
            if key not in item:
                return f"line {index}: missing key {key}"

        sku = item["sku"]
        if not sku:
            return f"line {index}: sku must not be empty"
        if sku in seen:
            return f"line {index}: duplicate sku {sku}"
        seen.add(sku)

        try:
            qty = int(item["qty"])
        except ValueError:
            return f"line {index}: qty is not a number"
        if qty <= 0:
            return f"line {index}: qty must be positive"

        try:
            price = int(item["unit_price_kopecks"])
        except ValueError:
            return f"line {index}: price is not a number"
        if price < 0:
            return f"line {index}: price must not be negative"

    if promo_code and promo_code not in PROMO_CODES:
        return f"unknown promo code {promo_code}"
    if shipping_city and shipping_city not in SUPPORTED_CITIES:
        return f"unsupported city {shipping_city}"
    return None 


def calculate_order_total(
    lines: list[dict[str, str]],
    promo_code: str = "",
    shipping_city: str = "",
) -> int | None:
    """Return the order total in kopecks, or None if the order is invalid."""
    ...
