---
tags:
  - gate
  - dm
  - combinatorics
  - long
---
# Combinatorics: Combinations with Repetitions

## Introduction
When dealing with combinations where we can select elements multiple times (with replacement), standard combination formulas ($\binom{n}{r}$) and permutation formulas ($n^r$) fall short. This is because **order does not matter**, only the **count** of each selected item matters.

### Why not $n^r$?
If we have $n$ types of items and want to select $r$ items, we might think of $n^r$. However, $n^r$ treats selections as an ordered sequence. For example, selecting 2 Apples and 2 Oranges could be counted multiple times (e.g., AOOA, AAOO, OAOA, etc.), but in our case, they all represent the same selection: exactly 2 Apples and 2 Oranges.
Stars & Bars avoids this by thinking in counts, not sequences.

## The Stars and Bars Method

To correctly count the number of combinations when repetitions are allowed, we reframe the problem using the **Stars and Bars** technique.

### Example 1: Selecting 1 element from a set $\{a,b,c\}$
In how many ways can we select one element from a set of 3?
Answer: $\binom{3}{1} = 3$ ways (choose one from 3).
Either we take $a$, $b$, or $c$.

Visually, we can represent this using dividers (bars `|`) and items (spaces `_`).
If we want to select 1 element from 3 choices, we need 2 dividers to separate the 3 categories.
- `_ | | ` represents selecting $a$
- ` | _ | ` represents selecting $b$
- ` | | _ ` represents selecting $c$

Selecting one element is the same as shifting one star among the valid places separated by the bars. Placing a star in a slot combination is essentially a choice.

### Example 2: Selecting 4 fruits from 3 types
In a mall, there are 3 containers with infinite supplies of Apple (A), Papaya (P), and Orange (O). How many ways can we select 4 fruits?

Manual enumeration:
- 4A, 4P, 4O (3 ways)
- 3A 1O, 3A 1P, 3O 1A, 3O 1P, 3P 1A, 3P 1O (6 ways)
- 2A 2O, 2A 2P, 2O 2P (3 ways)
- 2A 1O 1P, 2O 1A 1P, 2P 1A 1O (3 ways)

So total = 15 possibilities.

**Stars and Bars logic:**
Instead of picking fruits, reframe the problem:
- Represent the 4 fruits as **stars**: $\star \star \star \star$
- Use **bars** (`|`) to split them into the 3 categories (Apple | Papaya | Orange). To split into 3 groups, we need $3 - 1 = 2$ dividers.

Examples:
- $\star \star | \star | \star \rightarrow$ 2 Apples, 1 Papaya, 1 Orange.
- $\star \star \star | | \star \rightarrow$ 3 Apples, 0 Papayas, 1 Orange.
- $| | \star \star \star \star \rightarrow$ 0 Apples, 0 Papayas, 4 Oranges.

Now the question becomes: 
"In how many ways can I arrange 4 stars and 2 dividers?"

You have a total of $4 + 2 = 6$ positions. You just need to choose 2 positions for the dividers.
Number of ways = $\binom{6}{2} = 15$.

### General Formula

To select $r$ items from $n$ types (allowing repetitions):
**Number of ways = $\binom{n + r - 1}{r} = \binom{n + r - 1}{n - 1}$**

**In Example 2:**
- $n = 3$ (types: Apple, Papaya, Orange)
- $r = 4$ (items to select)
- Formula evaluates to: $\binom{3 + 4 - 1}{4} = \binom{6}{4} = \binom{6}{2} = 15$

---
## Relevant PYQs

### GATE CSE 2022 | Question: 22
[Discussion Link](https://gateoverflow.in/371914/gate-cse-2022-question-22)

The number of arrangements of six identical balls in three identical bins is _____________ .

*(Note on the question above: The question explicitly specifies **identical bins**. Standard Stars and bars is used when distributing identical objects into **distinct bins** (like types of fruits). For identical bins, it becomes an integer partition problem, not strictly a Stars and Bars counting problem, but it belongs to the same combinatorics umbrella.)*
