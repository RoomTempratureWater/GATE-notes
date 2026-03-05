---
tags:
  - "#dm"
  - "#combinatorics"
  - "#long"
  - "#gate"
---

# Generating Functions & Power Series

## Intuitive Explanation for GATE Perspective
Generating functions act as a bridge between **discrete mathematics** (sequences, combinatorics, recurrences) and **continuous mathematics** (calculus, functions). 

Instead of manipulating an infinite sequence of numbers $\langle a_0, a_1, a_2, \dots \rangle$ element by element, we "encode" the entire sequence as the coefficients of a formal polynomial or power series:
$$ G(x) = a_0 x^0 + a_1 x^1 + a_2 x^2 + \dots = \sum_{i=0}^{\infty} a_i x^i $$

**Why is this useful for GATE?**
1. **Solving Recurrence Relations:** It converts complex linear recurrence relations into straightforward algebraic equations involving $G(x)$.
2. **Combinatorics:** Generating polynomials allows us to multiply combinations easily (e.g., finding the coefficient of $x^n$ when selecting items with constraints).
3. **Sequence Operations:** Shifting a sequence right (adding leading zeros) simply means multiplying $G(x)$ by $x^k$. Adding two sequences is simply adding their generating functions!

---

## Power Series Formulas

The foundation of most generating functions in our CSE syllabus is the infinite geometric progression formula:

$$ \frac{1}{1-ax} = 1 + ax + (ax)^2 + (ax)^3 + \dots $$
*(Assuming $|ax| < 1$ for convergence, though in formal power series, convergence isn't strictly necessary.)*

Setting $a=1$:
$$ \frac{1}{1-x} = 1 + x + x^2 + x^3 + \dots $$

If we have a positive sign in the denominator:
$$ \frac{1}{1+ax} = \frac{1}{1 - (-ax)} = 1 + (-ax) + (-ax)^2 + (-ax)^3 + \dots $$
Which yields an alternating sequence:
$$ \frac{1}{1+ax} = 1 - ax + a^2x^2 - a^3x^3 + \dots $$

### Derivation of $(1-x)^{-2}$ (IMPORTANT)
To find the generating function for the sequence $\langle 1, 2, 3, 4, \dots \rangle$, we use differentiation.
1. Start with the standard power series:
   $$ \frac{1}{1-x} = 1 + x + x^2 + x^3 + x^4 + \dots $$
2. Differentiate both sides with respect to $x$:
   $$ \frac{d}{dx} \left( (1-x)^{-1} \right) = \frac{d}{dx} \left( 1 + x + x^2 + x^3 + \dots \right) $$
3. Apply chain rule on LHS and power rule on RHS:
   $$ -1 \cdot (1-x)^{-2} \cdot (-1) = 0 + 1 + 2x + 3x^2 + 4x^3 + \dots $$
4. Simplify:
   $$ \frac{1}{(1-x)^2} = 1 + 2x + 3x^2 + 4x^3 + \dots $$

---

## Closed Form of Sequences (Examples)

Let's find the closed-form generating function $G(x)$ for various sequences.

### Example 1: $\langle 1, -1, 1, -1, \dots \rangle$
$$ G(x) = 1x^0 + (-1)x^1 + 1x^2 + (-1)x^3 \dots $$
$$ G(x) = 1 - x + x^2 - x^3 \dots $$
This matches the alternating power series where $a=1$:
$$ G(x) = \frac{1}{1+x} $$

### Example 2: $\langle 6, 6, 6, 6, \dots \rangle$
$$ G(x) = 6 + 6x + 6x^2 + 6x^3 \dots $$
Take 6 common:
$$ G(x) = 6(1 + x + x^2 + x^3 \dots) $$
$$ G(x) = \frac{6}{1-x} $$

### Example 3: $\langle 1, 0, 1, 0, 1, 0, \dots \rangle$
Direct Expansion:
$$ G(x) = 1 + x^2 + x^4 + x^6 + \dots $$
Let's solve this using average of two known sequences:
- We know sequence for all 1s: $\langle 1, 1, 1, 1, \dots \rangle \rightarrow G_1(x) = \frac{1}{1-x}$
- We know alternating sequence: $\langle 1, -1, 1, -1, \dots \rangle \rightarrow G_2(x) = \frac{1}{1+x}$

If we add these two sequences element by element, the odd powers cancel out!
Adding: $\langle 2, 0, 2, 0, 2, \dots \rangle = G_1(x) + G_2(x) = \frac{1}{1-x} + \frac{1}{1+x}$

To get our target sequence of $\langle 1, 0, 1, 0 \dots \rangle$, divide by 2:
$$ G(x) = \frac{1}{2} \left[ \frac{1}{1-x} + \frac{1}{1+x} \right] $$
$$ G(x) = \frac{1}{2} \left[ \frac{1+x + 1-x}{(1-x)(1+x)} \right] $$
$$ G(x) = \frac{1}{2} \left[ \frac{2}{1-x^2} \right] = \frac{1}{1-x^2} $$

### Example 4: $\langle 0, 0, 1, a, a^2, a^3, \dots \rangle$
$$ G(x) = x^2 + ax^3 + a^2x^4 \dots $$
Factor out $x^2$:
$$ G(x) = x^2(1 + ax + a^2x^2 + a^3x^3 \dots) $$
Substitute the standard power series for $(1-ax)^{-1}$:
$$ G(x) = x^2 \left( \frac{1}{1-ax} \right) = \frac{x^2}{1-ax} $$

### Example 5: $\langle 0, 0, 0, 6, -6, 6, -6, \dots \rangle$
$$ G(x) = 6x^3 - 6x^4 + 6x^5 - 6x^6 \dots $$
Take $-1$ or just factor logically:
$$ G(x) = 6x^3(1 - x + x^2 - x^3 \dots) $$
$$ G(x) = 6x^3 \left( \frac{1}{1+x} \right) = \frac{6x^3}{1+x} $$

---

## Extracting Sequence from Generating Function

### Problem 1: $G(x) = \frac{x^4}{1-x}$
Factor it:
$$ G(x) = x^4 \left( \frac{1}{1-x} \right) $$
$$ G(x) = x^4(1 + x + x^2 + x^3 \dots) $$
$$ G(x) = x^4 + x^5 + x^6 + x^7 \dots $$
The coefficients are $0$ up to $x^3$, and $1$ afterwards.
Sequence: $\langle 0, 0, 0, 0, 1, 1, 1, \dots \rangle$

### Problem 2: $G(x) = \frac{x^2}{1-x} + [2x + 3x^{10} - 15]$
We split this into an infinite part and a polynomial part.
Part 1: $\frac{x^2}{1-x} = x^2 + x^3 + x^4 + \dots$
Sequence 1: $\langle 0, 0, 1, 1, 1, 1, \dots \rangle$

Part 2: $-15 + 2x^1 + 3x^{10}$
Sequence 2: $\langle -15, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, \dots \rangle$

Adding both sequences element by element:
- $a_0 = 0 - 15 = -15$
- $a_1 = 0 + 2 = 2$
- $a_2 = 1 + 0 = 1$
- $a_{10} = 1 + 3 = 4$
- For all other $n \ge 2$, $a_n = 1$

Resulting sequence: $\langle -15, 2, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, \dots \rangle$

### Problem 3: $G(x) = \sum_{n=0}^{\infty} (2n+3)x^n$
By linearity, split the summation:
$$ G(x) = \sum_{n=0}^{\infty} 2n \cdot x^n + \sum_{n=0}^{\infty} 3 \cdot x^n $$
$$ G(x) = 2 \left( \sum_{n=0}^{\infty} n x^n \right) + 3 \left( \sum_{n=0}^{\infty} x^n \right) $$

We already know $\sum x^n = \frac{1}{1-x}$.
How to find $\sum n x^n$?
Let's take the sequence $\langle 0, 1, 2, 3 \dots \rangle$ which has generating function $x + 2x^2 + 3x^3 \dots$
Factor $x$: $x(1 + 2x + 3x^2 \dots)$
Substitute the derived identity: $x \left( \frac{1}{(1-x)^2} \right) = \frac{x}{(1-x)^2}$

Now substitute both back:
$$ G(x) = 2 \left( \frac{x}{(1-x)^2} \right) + 3 \left( \frac{1}{1-x} \right) $$
$$ G(x) = \frac{2x}{(1-x)^2} + \frac{3(1-x)}{(1-x)^2} = \frac{3 - x}{(1-x)^2} $$

---
## Relevant Reference Questions

- **GATE CSE 2022 | Question 26**: Generating function properties with differences. [Link](https://gateoverflow.in/371910/gate-cse-2022-question-26)
- **GATE CSE 1987 | Question 10b**: Finding generating function for Fibonacci sequence. [Link](https://gateoverflow.in/82451/gate-cse-1987-question-10b)
- **GATE CSE 2017 Set 2 | Question 47**: Applications of generating functions in discrete math problems. [Link](https://gateoverflow.in/118392/gate-cse-2017-set-2-question-47)

---
*Linked Notes:*
- [[DM/long/Combinatorics_Combinations_Repetitions_Long.md|Combinations With Repetitions]]
- [[DM/long/Set_Theory_Relations.md|Relations]]
