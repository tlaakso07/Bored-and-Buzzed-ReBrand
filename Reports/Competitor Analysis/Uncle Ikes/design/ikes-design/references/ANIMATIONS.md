# Animation Reference

> Cinematic motion design extracted from live DOM. Follow these specs exactly to recreate the experience.

## Motion Technology Stack

Pure CSS animations — no external animation libraries detected.

## Scroll Journey

The page is **900px** tall. Each frame below shows what the user sees at that scroll depth.

> **Use these screenshots to understand WHAT animates, WHEN it animates, and HOW it moves.**

### 0% — Top / Hero
Scroll position: 0px

![Scroll 0%](../screens/scroll/scroll-000.png)

### 17% — Opening Section
Scroll position: 0px

![Scroll 17%](../screens/scroll/scroll-017.png)

### 33% — First Feature Section
Scroll position: 0px

![Scroll 33%](../screens/scroll/scroll-033.png)

### 50% — Mid-Page
Scroll position: 0px

![Scroll 50%](../screens/scroll/scroll-050.png)

### 67% — Lower Content
Scroll position: 0px

![Scroll 67%](../screens/scroll/scroll-067.png)

### 83% — Near Footer
Scroll position: 0px

![Scroll 83%](../screens/scroll/scroll-083.png)

### 100% — Bottom / Footer
Scroll position: 0px

![Scroll 100%](../screens/scroll/scroll-100.png)

## CSS Keyframes (33 extracted)

### `@keyframes fa-spin`

Duration: `var(--fa-animation-duration,2s)` · Easing: `var(--fa-animation-timing,linear)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-spin`, `.fa-pulse, .fa-spin-pulse`

```css
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```

> Transform/motion animation

### `@keyframes fa-beat`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,ease-in-out)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-beat`

```css
@keyframes fa-beat {
  0%, 90% {
    transform: scale(1);
  }
  45% {
    transform: scale(var(--fa-beat-scale,1.25));
  }
}
```

> Transform/motion animation

### `@keyframes fa-bounce`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,cubic-bezier(.28,.84,.42,1))` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-bounce`

```css
@keyframes fa-bounce {
  0% {
    transform: scale(1) translateY(0px);
  }
  10% {
    transform: scale(var(--fa-bounce-start-scale-x,1.1),var(--fa-bounce-start-scale-y,.9))translateY(0);
  }
  30% {
    transform: scale(var(--fa-bounce-jump-scale-x,.9),var(--fa-bounce-jump-scale-y,1.1))translateY(var(--fa-bounce-height,-.5em));
  }
  50% {
    transform: scale(var(--fa-bounce-land-scale-x,1.05),var(--fa-bounce-land-scale-y,.95))translateY(0);
  }
  57% {
    transform: scale(1,1)translateY(var(--fa-bounce-rebound,-.125em));
  }
  64% {
    transform: scale(1) translateY(0px);
  }
  100% {
    transform: scale(1) translateY(0px);
  }
}
```

> Transform/motion animation

### `@keyframes fa-fade`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-fade`

```css
@keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity,.4);
  }
}
```

> Opacity fade

### `@keyframes fa-beat-fade`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-beat-fade`

```css
@keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity,.4);
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(var(--fa-beat-fade-scale,1.125));
  }
}
```

> Fade + motion enter animation

### `@keyframes fa-flip`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,ease-in-out)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-flip`

```css
@keyframes fa-flip {
  50% {
    transform: rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));
  }
}
```

> Transform/motion animation

### `@keyframes fa-shake`

Duration: `var(--fa-animation-duration,1s)` · Easing: `var(--fa-animation-timing,linear)` · Delay: `var(--fa-animation-delay,0s)` · Iteration: `var(--fa-animation-iteration-count,infinite)`

Used by: `.fa-shake`

```css
@keyframes fa-shake {
  0% {
    transform: rotate(-15deg);
  }
  4% {
    transform: rotate(15deg);
  }
  8%, 24% {
    transform: rotate(-18deg);
  }
  12%, 28% {
    transform: rotate(18deg);
  }
  16% {
    transform: rotate(-22deg);
  }
  20% {
    transform: rotate(22deg);
  }
  32% {
    transform: rotate(-12deg);
  }
  36% {
    transform: rotate(12deg);
  }
  40%, 100% {
    transform: rotate(0deg);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__trackProgress`

Duration: `auto` · Easing: `linear` · Delay: `0s` · Iteration: `1` · Fill: `forwards`

Used by: `.Toastify__progress-bar--animated`

```css
@keyframes Toastify__trackProgress {
  0% {
    transform: scaleX(1);
  }
  100% {
    transform: scaleX(0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__bounceInRight`

Used by: `.Toastify__bounce-enter--top-right, .Toastify__bounce-enter--bottom-right`

```css
@keyframes Toastify__bounceInRight {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(3000px, 0px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(-25px, 0px, 0px);
  }
  75% {
    transform: translate3d(10px, 0px, 0px);
  }
  90% {
    transform: translate3d(-5px, 0px, 0px);
  }
  100% {
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutRight`

Used by: `.Toastify__bounce-exit--top-right, .Toastify__bounce-exit--bottom-right`

```css
@keyframes Toastify__bounceOutRight {
  20% {
    opacity: 1;
    transform: translate3d(-20px,var(--y),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(2000px,var(--y),0);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceInLeft`

Used by: `.Toastify__bounce-enter--top-left, .Toastify__bounce-enter--bottom-left`

```css
@keyframes Toastify__bounceInLeft {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(-3000px, 0px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(25px, 0px, 0px);
  }
  75% {
    transform: translate3d(-10px, 0px, 0px);
  }
  90% {
    transform: translate3d(5px, 0px, 0px);
  }
  100% {
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutLeft`

Used by: `.Toastify__bounce-exit--top-left, .Toastify__bounce-exit--bottom-left`

```css
@keyframes Toastify__bounceOutLeft {
  20% {
    opacity: 1;
    transform: translate3d(20px,var(--y),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(-2000px,var(--y),0);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceInUp`

Used by: `.Toastify__bounce-enter--bottom-center`

```css
@keyframes Toastify__bounceInUp {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0px, 3000px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(0px, -20px, 0px);
  }
  75% {
    transform: translate3d(0px, 10px, 0px);
  }
  90% {
    transform: translate3d(0px, -5px, 0px);
  }
  100% {
    transform: translateZ(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutUp`

Used by: `.Toastify__bounce-exit--top-center`

```css
@keyframes Toastify__bounceOutUp {
  20% {
    transform: translate3d(0,calc(var(--y) - 10px),0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0,calc(var(--y) + 20px),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(0px, -2000px, 0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceInDown`

Used by: `.Toastify__bounce-enter--top-center`

```css
@keyframes Toastify__bounceInDown {
  0%, 60%, 75%, 90%, 100% {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0px, -3000px, 0px);
  }
  60% {
    opacity: 1;
    transform: translate3d(0px, 25px, 0px);
  }
  75% {
    transform: translate3d(0px, -10px, 0px);
  }
  90% {
    transform: translate3d(0px, 5px, 0px);
  }
  100% {
    transform: none;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__bounceOutDown`

Used by: `.Toastify__bounce-exit--bottom-center`

```css
@keyframes Toastify__bounceOutDown {
  20% {
    transform: translate3d(0,calc(var(--y) - 10px),0);
  }
  40%, 45% {
    opacity: 1;
    transform: translate3d(0,calc(var(--y) + 20px),0);
  }
  100% {
    opacity: 0;
    transform: translate3d(0px, 2000px, 0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__zoomIn`

Used by: `.Toastify__zoom-enter`

```css
@keyframes Toastify__zoomIn {
  0% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  50% {
    opacity: 1;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__zoomOut`

Used by: `.Toastify__zoom-exit`

```css
@keyframes Toastify__zoomOut {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
    transform: translate3d(0,var(--y),0) scale3d(.3,.3,.3);
  }
  100% {
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__flipIn`

Used by: `.Toastify__flip-enter`

```css
@keyframes Toastify__flipIn {
  0% {
    transform: perspective(400px) rotateX(90deg);
    animation-timing-function: ease-in;
    opacity: 0;
  }
  40% {
    transform: perspective(400px) rotateX(-20deg);
    animation-timing-function: ease-in;
  }
  60% {
    transform: perspective(400px) rotateX(10deg);
    opacity: 1;
  }
  80% {
    transform: perspective(400px) rotateX(-5deg);
  }
  100% {
    transform: perspective(400px);
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__flipOut`

Used by: `.Toastify__flip-exit`

```css
@keyframes Toastify__flipOut {
  0% {
    transform: translate3d(0,var(--y),0) perspective(400px);
  }
  30% {
    transform: translate3d(0,var(--y),0) perspective(400px) rotateX(-20deg);
    opacity: 1;
  }
  100% {
    transform: translate3d(0,var(--y),0) perspective(400px) rotateX(90deg);
    opacity: 0;
  }
}
```

> Fade + motion enter animation

### `@keyframes Toastify__slideInRight`

Used by: `.Toastify__slide-enter--top-right, .Toastify__slide-enter--bottom-right`

```css
@keyframes Toastify__slideInRight {
  0% {
    transform: translate3d(110%, 0px, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideInLeft`

Used by: `.Toastify__slide-enter--top-left, .Toastify__slide-enter--bottom-left`

```css
@keyframes Toastify__slideInLeft {
  0% {
    transform: translate3d(-110%, 0px, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideInUp`

Used by: `.Toastify__slide-enter--bottom-center`

```css
@keyframes Toastify__slideInUp {
  0% {
    transform: translate3d(0px, 110%, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideInDown`

Used by: `.Toastify__slide-enter--top-center`

```css
@keyframes Toastify__slideInDown {
  0% {
    transform: translate3d(0px, -110%, 0px);
    visibility: visible;
  }
  100% {
    transform: translate3d(0,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutRight`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--top-right, .Toastify__slide-exit--bottom-right`

```css
@keyframes Toastify__slideOutRight {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(110%,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutLeft`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--top-left, .Toastify__slide-exit--bottom-left`

```css
@keyframes Toastify__slideOutLeft {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(-110%,var(--y),0);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutDown`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--bottom-center`

```css
@keyframes Toastify__slideOutDown {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(0px, 500px, 0px);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__slideOutUp`

Duration: `0.3s` · Easing: `ease-in`

Used by: `.Toastify__slide-exit--top-center`

```css
@keyframes Toastify__slideOutUp {
  0% {
    transform: translate3d(0,var(--y),0);
  }
  100% {
    visibility: hidden;
    transform: translate3d(0px, -500px, 0px);
  }
}
```

> Transform/motion animation

### `@keyframes Toastify__spin`

Duration: `0.65s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.Toastify__spinner`

```css
@keyframes Toastify__spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```

> Transform/motion animation

### `@keyframes toastSlideInRight`

Duration: `0.3s` · Easing: `ease-out` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.Toastify__slide-enter--top-right, .Toastify__slide-enter--bottom-right`

```css
@keyframes toastSlideInRight {
  0% {
    opacity: 0;
    transform: translate(100%);
  }
  100% {
    opacity: 1;
    transform: translate(0px);
  }
}
```

> Fade + motion enter animation

### `@keyframes toastSlideOutRight`

Duration: `0.2s` · Easing: `ease-in` · Delay: `0s` · Iteration: `1` · Fill: `none`

Used by: `.Toastify__slide-exit--top-right, .Toastify__slide-exit--bottom-right`

```css
@keyframes toastSlideOutRight {
  0% {
    opacity: 1;
    transform: translate(0px);
  }
  100% {
    opacity: 0;
    transform: translate(100%);
  }
}
```

> Fade + motion enter animation

### `@keyframes spin`

```css
@keyframes spin {
  100% {
    transform: rotate(360deg);
  }
}
```

> Transform/motion animation

### `@keyframes pulse`

```css
@keyframes pulse {
  50% {
    opacity: 0.5;
  }
}
```

> Opacity fade

## Motion Tokens (CSS Variables)

### Duration Tokens

```css
--default-transition-duration: .15s;
```

### Easing Tokens

```css
--ease-in-out: cubic-bezier(.4,0,.2,1);
--default-transition-timing-function: cubic-bezier(.4,0,.2,1);
--ease-out: cubic-bezier(0,0,.2,1);
```

## Global Transition Declarations

These `transition` values were extracted from CSS rules across the site:

```css
transition: transform 0.3s;
transition: opacity 0.1s;
transition: 0.3s;
transition: transform 0.2s;
transition: top 0.2s;
transition: 0.2s;
transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
transition: 0.15s;
```

## How to Recreate This Motion Design

### Step 2 — Scroll-Reveal Pattern

Elements that animate into view follow this pattern:

```css
/* Initial hidden state */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity .15s cubic-bezier(.4,0,.2,1),
              transform .15s cubic-bezier(.4,0,.2,1);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Step 3 — Key Motion Principles

- **Duration scale:** `.15s` · `0.3s` · `0.1s` · `0.2s` — use these values, never invent new durations
- **Always add** `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }`

### Step 4 — Scroll Journey Reference

Match what happens at each scroll position:

- **0%** (`0px`) → `screens/scroll/scroll-000.png`
- **17%** (`0px`) → `screens/scroll/scroll-017.png`
- **33%** (`0px`) → `screens/scroll/scroll-033.png`
- **50%** (`0px`) → `screens/scroll/scroll-050.png`
- **67%** (`0px`) → `screens/scroll/scroll-067.png`
- **83%** (`0px`) → `screens/scroll/scroll-083.png`
- **100%** (`0px`) → `screens/scroll/scroll-100.png`

