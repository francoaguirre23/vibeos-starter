# UI Recipes (Loop v0.1a)

Reusable recipes for reproducing this project’s neumorphic UI in other projects.

Use this as a practical playbook: each recipe follows **Intent -> Tokens -> Markup -> CSS -> Tuning knobs**.

---

## 1) Design Foundation

### Intent
Build soft-depth UI where surfaces are mostly the same base color and depth comes from shadow contrast, not flat color blocks.

### Core Tokens
Start with these global variables:

```css
:root {
  --shell: #f4f4f5;
  --bg: var(--shell);
  --surface: #f4f4f5;
  --inset-wash: #e0e1e7;
  --surface-inset: color-mix(in srgb, var(--surface) 88%, var(--inset-wash));

  --text: #111111;
  --muted: #5c5f66;
  --focus: #0066cc;

  --shadow-dark: #b4b8c6;
  --shadow-light: #ffffff;

  --neo-raise-xl: 12px 12px 30px var(--shadow-dark), -12px -12px 36px rgba(255, 255, 255, 1);
  --neo-raise-lg: 9px 9px 22px var(--shadow-dark), -9px -9px 28px rgba(255, 255, 255, 1);
  --neo-raise-md: 6px 6px 16px var(--shadow-dark), -6px -6px 20px rgba(255, 255, 255, 1);
  --neo-raise-sm: 5px 5px 12px var(--shadow-dark), -5px -5px 14px rgba(255, 255, 255, 1);

  --neo-inset-xl: inset 8px 8px 18px var(--shadow-dark), inset -7px -7px 22px rgba(255, 255, 255, 1);
  --neo-inset-lg: inset 6px 6px 14px var(--shadow-dark), inset -6px -6px 18px rgba(255, 255, 255, 1);
  --neo-inset-md: inset 5px 5px 11px var(--shadow-dark), inset -5px -5px 14px rgba(255, 255, 255, 1);
  --neo-inset-sm: inset 4px 4px 9px var(--shadow-dark), inset -4px -4px 11px rgba(255, 255, 255, 1);
}
```

### Tuning Knobs
- **Safe to tweak**: `--shell`, `--surface`, `--inset-wash`, `--text`, `--muted`, `--focus`, `--shadow-dark`.
- **Layout-coupled (tread carefully)**: offsets used for header/nav alignment (`--spine-inset-to-main`, spacing tokens).
- Keep `--surface` close to `--shell`; use shadows to separate layers.

---

## 2) Theme System Recipe

### Intent
Use token overrides for themes instead of per-component color overrides.

### Markup / Runtime
Set `data-theme` on `document.documentElement`:

```ts
const THEMES = ["default", "warm", "cool", "dark-green", "russian-violet"] as const;
type Theme = (typeof THEMES)[number];

function cycleTheme(current: Theme): Theme {
  return THEMES[(THEMES.indexOf(current) + 1) % THEMES.length];
}

document.documentElement.dataset.theme = currentTheme;
```

### CSS Theme Override Example

```css
html[data-theme="dark-green"] {
  --shell: #16302b;
  --surface: #1a3830;
  --inset-wash: #122620;
  --text: #cce0d8;
  --muted: #8ab8a8;
  --focus: #4aaa88;

  --shadow-dark: #060f0b;
  --shadow-light: #25473b;
  --neo-raise-md: 5px 5px 13px #060f0b, -5px -5px 16px #25473b;
  --neo-inset-md: inset 4px 4px 10px #060f0b, inset -4px -4px 12px #25473b;
}
```

### Dark Theme Edge Definition
For deep themes, add subtle edge borders so cards don’t disappear:

```css
html[data-theme="dark-green"] .tile,
html[data-theme="dark-green"] .note-list__item,
html[data-theme="dark-green"] .nav-rail__module {
  border: 1px solid rgba(255, 255, 255, 0.07);
}
```

### Tuning Knobs
- Dark theme quality depends most on `--shadow-dark` / `--shadow-light` separation.
- Increase border alpha in dark mode if edges feel muddy.

---

## 3) Smooth Theme Transition Recipe

### Intent
Avoid abrupt palette flashes when switching between very different themes.

### CSS

```css
:root {
  --theme-transition-duration: 1680ms;
  --theme-transition-ease: cubic-bezier(0.22, 1, 0.36, 1);
}

@media (prefers-reduced-motion: no-preference) {
  body,
  #root,
  .app,
  .app__body,
  .app__spine,
  .tile,
  .btn,
  .nav-rail__module,
  .note-list__item,
  .header-calendar__surface,
  .header-calendar__event,
  .action-creator__band,
  .theme-knob,
  .theme-knob-socket,
  .app__name-letter,
  input,
  textarea,
  select {
    transition:
      background-color var(--theme-transition-duration) var(--theme-transition-ease),
      color var(--theme-transition-duration) var(--theme-transition-ease),
      border-color var(--theme-transition-duration) var(--theme-transition-ease),
      box-shadow var(--theme-transition-duration) var(--theme-transition-ease),
      text-shadow var(--theme-transition-duration) var(--theme-transition-ease);
  }
}
```

### Tuning Knobs
- 400-700ms = crisp; 1000-1700ms = calm/ambient.
- Keep transition scope to color/shadow; avoid layout property transitions.

---

## 4) App Shell + Spine Recipe

### Intent
One raised shell (“spine”) contains nav and active module area.

### Markup

```tsx
<div className="app">
  <div className="app__body">
    <div className="app__top-align">
      <div className="app__top-align__main">{/* header split */}</div>
    </div>
    <div className="app__spine">
      <div className="app__nav-col">{/* theme knob + nav rail */}</div>
      <main className="app__grid">{/* active module */}</main>
    </div>
  </div>
</div>
```

### CSS

```css
.app__spine {
  padding: 0.65rem 0.85rem 0.75rem 0.65rem;
  border-radius: 22px;
  background: var(--shell);
  border: 1px solid rgba(0, 0, 0, 0.05);
  box-shadow:
    0 18px 48px rgba(100, 108, 128, 0.11),
    0 8px 22px rgba(100, 108, 128, 0.07),
    0 1px 0 rgba(255, 255, 255, 1),
    inset 0 1px 0 rgba(255, 255, 255, 1);
}

.app__spine > main {
  padding-top: var(--module-start-offset);
  padding-left: 0.85rem;
  margin-left: 0.35rem;
  border-left: 1px solid var(--spine-divider);
}
```

### Tuning Knobs
- Increase spine radius only if card radius across components also rises.
- Preserve left divider for nav/content separation.

---

## 5) Header Split Layout Recipe

### Intent
Consistent top area across modules: ambient row + action row + right rail (calendar).

### Markup

```tsx
<div className="app__header-split">
  <div className="app__header-split-primary app__header-split-primary--ambient">...</div>
  <div className="app__header-split-primary app__header-split-primary--action">...</div>
  <aside className="app__header-split-rail">...</aside>
</div>
```

### CSS

```css
.app__header-split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(260px, 320px);
  grid-template-rows: minmax(0, 1fr) auto;
  grid-template-areas:
    "ambient rail"
    "action rail";
  column-gap: 1.5rem;
  row-gap: var(--header-ambient-action-gap);
}
```

### Tuning Knobs
- Right rail width range (`260px-320px`) is a key rhythm anchor.
- Do not tweak this independently from saved-notes rail widths.

---

## 6) Nav Rail Module Button Recipe

### Intent
Small, tactile module buttons that feel raised by default and pressed when active.

### Markup

```tsx
<button className={`nav-rail__module${isActive ? " nav-rail__module--active" : ""}`}>
  <Icon className="nav-rail__icon" />
  <span className="nav-rail__label">...</span>
</button>
```

### CSS

```css
.nav-rail__module {
  min-height: 4.4rem;
  border-radius: 12px;
  background: var(--surface);
  box-shadow: var(--neo-raise-md);
  color: var(--muted);
}

.nav-rail__module--active {
  background: var(--nav-rail-active-tint);
  box-shadow: var(--neo-inset-sm);
  color: var(--text);
}
```

### Tuning Knobs
- Keep icon size around `1.25rem`.
- If labels feel cramped, widen rail before reducing typography.

---

## 7) Raised Tile/Card + Inset Field Recipe

### Intent
Build a clear hierarchy: card face raised, fields recessed.

### Markup

```tsx
<section className="tile">
  <input className="field-inset" />
</section>
```

### CSS

```css
.tile {
  background: var(--surface);
  box-shadow: var(--neo-raise-lg);
  border-radius: 16px;
}

.field-inset {
  background: var(--surface-inset);
  box-shadow: var(--neo-inset-md);
  border-radius: 10px;
  border: 1px solid color-mix(in srgb, var(--shadow-dark) 20%, transparent);
}
```

### Tuning Knobs
- Raise depth first by shadow contrast, not by darkening surface too much.
- If inset wells vanish, darken `--inset-wash` slightly.

---

## 8) Saved Notes Rail Card Recipe

### Intent
Keep list cards floating cleanly without right-edge shadow clipping.

### CSS

```css
.note-sidebar__list {
  overflow-y: auto;
  margin: 0;
  padding: 0.15rem 1.6rem 0.5rem 0.15rem; /* right pad prevents shadow clipping */
}

.note-list__item {
  border-radius: 12px;
  padding: 0.75rem 0.85rem;
  background: var(--surface);
  box-shadow: var(--neo-raise-md);
}

.note-list__item--active {
  box-shadow: var(--neo-inset-md);
}
```

### Tuning Knobs
- Keep right padding generous in scroll containers that host shadowed items.
- If shadows clip, increase internal padding before touching shadow blur.

---

## 9) Embossed Logo Recipe

### Intent
“Carved from surface” logotype using text-shadow only.

### Markup

```tsx
<span className="app__name-letters">
  <span className="app__name-letter">L</span>
  <span className="app__name-letter">o</span>
  <span className="app__name-letter">o</span>
  <span className="app__name-letter">p</span>
</span>
```

### CSS (base)

```css
.app__name-letter {
  color: var(--bg);
  text-shadow:
    -0.264rem -0.264rem 0.55rem rgba(255, 255, 255, 1),
    -0.08rem -0.08rem 0.16rem rgba(255, 255, 255, 1),
    0.29rem 0.29rem 0.64rem color-mix(in srgb, var(--shadow-dark) 77%, transparent),
    0.106rem 0.106rem 0.264rem color-mix(in srgb, var(--shadow-dark) 55%, transparent);
}
```

### CSS (dark overrides)

```css
html[data-theme="dark-green"] .app__name-letter {
  color: var(--shell);
  text-shadow:
    -0.38rem -0.38rem 0.72rem #2b5445,
    -0.12rem -0.12rem 0.2rem #204235,
    0.38rem 0.38rem 0.82rem #050e0a,
    0.13rem 0.13rem 0.3rem #0a1813;
}
```

### Tuning Knobs
- Increase top-left highlights to make logo pop.
- Increase bottom-right darks for deeper carve.
- Keep fill equal to shell for “engraved” look.

---

## 10) Soft Scrollbar Recipe

### Intent
Global track channel should feel inset/concave; thumb should feel raised.

### CSS

```css
:root {
  --loop-scrollbar-size: 12px;
  --loop-scrollbar-track: #f4f4f5;
  --loop-scrollbar-thumb: color-mix(in srgb, #cfd2db 65%, #ffffff);
}

* {
  scrollbar-width: thin;
  scrollbar-color: var(--loop-scrollbar-thumb) var(--loop-scrollbar-track);
}

*::-webkit-scrollbar-track {
  background: var(--loop-scrollbar-track);
  border-radius: 9999px;
  box-shadow:
    inset 0 0 0 1px color-mix(in srgb, var(--shadow-dark) 20%, transparent),
    inset 0 1px 2px rgba(0, 0, 0, 0.06);
}
```

### Tuning Knobs
- Keep channel and thumb colors in same palette family.
- In dark themes, override track/thumb tokens in the theme block.

---

## 11) Contextual Help Strip + History Tip Alignment

### Intent
Single-row contextual help with left dynamic message and right history tip reveal.

### Markup

```tsx
<div className="note-footer-help-strip">
  <p className="note-footer-help-strip__text">{activeHelpText}</p>
  <span className="notes-embed__history-tip" aria-hidden>Open earlier versions.</span>
</div>
```

### CSS

```css
.note-footer-help-strip {
  min-height: 2.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.notes-embed__history-tip {
  opacity: 0;
  transition: opacity 0.18s ease;
}

.notes-embed:has(.notes-embed__editor-footer-history:hover) .notes-embed__history-tip,
.notes-embed:has(.notes-embed__editor-footer-history:focus-within) .notes-embed__history-tip {
  opacity: 1;
}
```

### Tuning Knobs
- Keep help strip fixed-height to avoid layout jumps.
- Use `:has()` for cross-region hover coupling (button in one area, text in another).

---

## 12) Entry Animation Recipe

### Intent
Subtle “rise in” motion when module view swaps.

### CSS Pattern

```css
@media (prefers-reduced-motion: no-preference) {
  .app__grid-primary > .app__notes-main,
  .app__grid-primary > .app__action-items-workspace,
  .app__grid-primary > .app__center--solo {
    animation: app-view-content-rise 0.28s ease-out;
  }
}
```

### Tuning Knobs
- Keep motion short and low-distance.
- Match durations across modules to avoid inconsistent feel.

---

## Calibration Checklist (Quick QA)

Use this after token/theme changes:

1. **Depth hierarchy**: raised tiles should read above shell; inset wells should read below tiles.
2. **Shadow clipping**: scrollable rails should not cut right-side card shadows.
3. **Header rhythm**: logo/action/calendar vertical spacing should match across modules.
4. **Nav parity**: active/inactive states should feel consistent in all themes.
5. **Theme transitions**: no flash on light <-> dark switching.
6. **Dark mode legibility**: muted text remains readable at small sizes.
7. **Emboss quality**: logo highlight/shadow direction remains coherent (same light source).

---

## Common Pitfalls + Fixes

- **Pitfall**: Text or cards clip behind right edge in scroll panel.  
  **Fix**: Increase scroll container internal right padding (do not only tweak shadows).

- **Pitfall**: Dark theme looks flat.  
  **Fix**: Increase spread between `--shadow-dark` and `--shadow-light`; add subtle edge border.

- **Pitfall**: Theme switch feels harsh.  
  **Fix**: Add scoped transitions for color/shadow properties with eased timing.

- **Pitfall**: Neumorphism looks noisy.  
  **Fix**: Normalize all depth through shared `--neo-*` tokens; avoid one-off shadow literals.

- **Pitfall**: Logo disappears in dark theme.  
  **Fix**: Set logo fill to shell color and boost highlight/dark text-shadows proportionally.
