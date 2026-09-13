# Locator Strategy Examples

Practical examples of choosing robust vs. fragile locators for test
automation, worked through during QA training.

## Priority order (most to least reliable)

1. `id` — usually unique and stable
2. `data-testid` — custom attribute added specifically for testing;
   survives visual redesigns because it's unrelated to styling
3. `class` — useful, but often shared across elements or rewritten
   during a redesign
4. Structure/position (e.g. `div > button:nth-child(2)`) — most
   fragile, breaks on any layout change

## Why data-testid survives redesigns

A locator tied to a CSS class (e.g. `.btn-primary`) is tied to
**visual styling**. If a design team rebrands the button (new colors,
new class names), the test breaks — not because functionality
changed, but because the locator was never meant to track identity,
only appearance.

`data-testid="apply-coupon"` exists purely for testing — no styling
depends on it, so nobody has a reason to change it during a redesign.

## Worked example

Given this HTML:
```html
<div class="checkout-box">
  <input type="text" id="coupon-input" class="field-style-2024">
  <button class="rosu-mare-2024" data-testid="apply-coupon">Aplică cupon</button>
</div>
```

Correct locators:
- Input: `#coupon-input` (id — stable, unrelated to the styling class)
- Button: `[data-testid="apply-coupon"]` (never `.rosu-mare-2024`,
  which describes color/size and will likely be rewritten on redesign)

## CSS Selector vs XPath — syntax notes

- CSS attribute selector syntax: `[attribute="value"]` — NOT
  `attribute="value"` (that's HTML syntax, not a selector)
- XPath text match: `//button[text()="Aplică"]` — requires an exact
  text match, including diacritics (ă, ș, etc.)
