---
tags:
  - gate
  - dm
  - combinatorics
  - short
---
# Combinations with Repetitions (Short Notes)

Agar $n$ types of elements given ho aur $r$ items select karne ho (with repetition allowed), toh standard selection ($n^r$) kaam nahi aata. Yahan **order matter nahi karta**, sirf har item ka **count matter karta hai** (e.g., AOOA aur AAOO dono hi 2A and 2O hain).

## The Stars and Bars Method

Is problem ko simplify karne ke liye Stars and Bars method lagate hain:
- Jo items select/distribute karne hain unhe **stars** ($\star$) maan lo. $r$ stars chahiye.
- Alag-alag types (groups) ko alag karne ke liye **dividers/bars** ($|$) use karo. Agar $n$ types hain, toh $n-1$ bars lagenge.
- Equation banti hai: "Total symbols me se positions choose karo."
- Total slots = stars + bars = $r + (n - 1)$

**General Formula:**
$\binom{n+r-1}{r} = \binom{n+r-1}{n-1}$

### Example: Mal me 3 type fruits (A, P, O) hain, usme se 4 fruit lene hain.
- Stars ($r$) = 4
- Bars ($n-1$) = $3 - 1 = 2$
- Total symbols = $4 + 2 = 6$
- Ans: $\binom{6}{2} = 15$ ways.
- Ek valid arrangement: $\star \star | \star | \star \rightarrow$ 2 Apples, 1 Papaya, 1 Orange.

---
## Relevant PYQs

### GATE CSE 2022 | Question: 22
[Discussion Link](https://gateoverflow.in/371914/gate-cse-2022-question-22)
The number of arrangements of six identical balls in three identical bins is _____________ .

*(Important Note: Question me **identical bins** bola hai. "Stars and bars" tab lagta hai jab bins/groups **distinct** ho (jaise Apple vs Papaya). Is PYQ ke liye integer partition formula lagega, but topic same combinatorics sequence ka hai.)*
