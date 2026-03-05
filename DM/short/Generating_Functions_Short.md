---
tags:
  - "#dm"
  - "#combinatorics"
  - "#short"
  - "#gate"
---

# Generating Functions (Short Cheat Notes)

Generating functions hume sequence ko ek algebraic function equation me convert karne me help karti hai. Isse recurrence relation and combinatorics questions jaldi solve hote hain!

## Basic Power Series
Yeh 3 formulas GATE me direct apply hote hain, yaad rakhna:

1. **All 1s Sequence** $\langle 1, 1, 1, \dots \rangle$:
   $$ \frac{1}{1-x} = 1 + x + x^2 + x^3 \dots $$

2. **Alternating Sequence** $\langle 1, -1, 1, -1 \dots \rangle$:
   $$ \frac{1}{1+x} = 1 - x + x^2 - x^3 \dots $$

3. **Counting Numbers** $\langle 1, 2, 3, 4 \dots \rangle$: (Differentiate $\frac{1}{1-x}$)
   $$ \frac{1}{(1-x)^2} = 1 + 2x + 3x^2 + 4x^3 \dots $$

---

## Important Tips for Closed Forms

- **Shifting Sequence Right (padding initial 0s):**
  If sequence starts with $k$ zeroes like $\langle 0, 0, 1, 1 \dots \rangle$, simply multiply basic $G(x)$ by $x^k$.
  Example: $\langle 0, 0, 1, a, a^2 \dots \rangle \rightarrow$ factor $x^2$, function becomes $x^2 \cdot \frac{1}{1-ax}$.

- **Alternating Zeroes** $\langle 1, 0, 1, 0 \dots \rangle$:
  Average the "all 1s" aur "alternating" series ko:
  $$ \frac{G_{all\_ones} + G_{alternating}}{2} \Rightarrow \frac{1}{1-x^2} $$

- **Linearity:**
  Agar $G(x)$ ke expression me polynomial added hai, like $G(x) = \frac{x^2}{1-x} + (2x - 15)$, then pehle normal infinite sequence base part se nikalo, aur specific indices polynomial degree par jaake adjust kardo ($a_0 = -15, a_1 = 2$). Baki original rahenge.

## Multiplication Tricks
- $\sum nx^n$ banana hai toh $\sum x^n$ ko differentiate karke $x$ se multiply kardo. Limit change hojati hai. Result = $\frac{x}{(1-x)^2}$
- So $(2n+3)$ multiplier banan hai sequence elements pe:
  $2 \cdot \frac{x}{(1-x)^2} + 3 \cdot \frac{1}{1-x}$

---
## Questions for Revision
- **GATE 2022 | Q26** - [Link](https://gateoverflow.in/371910/gate-cse-2022-question-26)
- **GATE 1987 | Q10b** (Fibonacci seq) - [Link](https://gateoverflow.in/82451/gate-cse-1987-question-10b)
- **GATE 2017 (Set-2) | Q47** - [Link](https://gateoverflow.in/118392/gate-cse-2017-set-2-question-47)
