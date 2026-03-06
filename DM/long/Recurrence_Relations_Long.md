---
tags:
  - #gate
  - #dm
  - #combinatorics
  - #discrete_mathematics
---

# Recurrence Relations

A **Recurrence Relation** is an equation that recursively defines a sequence, where the next term is a function of the previous terms. 

For example, consider the sequence:
- $a_0 = 5$ (Initial condition)
- $a_1 = 2a_0$
- $a_2 = 2a_1$
- $\dots$
- $a_n = 2a_{n-1}$

In discrete mathematics, the goal is to find a **general solution** (closed-form expression) to calculate $a_n$ directly from $a_0$ instead of having to loop through all previous terms.

For the above example, we can derive the general solution as:
$$ a_n = 2^n \cdot a_0 $$

---

## Solving Linear Homogeneous Recurrence Relations

When solving recurrence relations, we use **Characteristic Equations** to find the roots and then substitute the initial conditions to find the constants.

### Type 1: Single Dependency
Equation: $a_n = d \cdot a_{n-1}$
Initial Condition: $a_0$

**General Solution:**
$$a_n = d^n(a_0)$$

---

### Type 2: Dependent on 2 Previous Elements (Distinct Roots)
Equation: $a_n = Xa_{n-1} + Ya_{n-2}$

**Example:**
Solve $a_n = 5a_{n-1} - 6a_{n-2}$ given $a_0 = 2, a_1 = 4$.

1. **Form the Characteristic Equation:**
   Assume $a_n = x^n$. We can re-write the equation as powers of $x$:
   $$x^2 = 5x - 6 \Rightarrow x^2 - 5x + 6 = 0$$
   
2. **Find the roots:**
   Solving $x^2 - 5x + 6 = 0$, we get $r_1 = 2$ and $r_2 = 3$.

3. **Write the General Solution:**
   $$a_n = c_1(2)^n + c_2(3)^n$$

4. **Solve for Constants ($c_1, c_2$) using Initial Conditions:**
   - Put $n = 0$: $2 = c_1(2)^0 + c_2(3)^0 \Rightarrow c_1 + c_2 = 2$
   - Put $n = 1$: $4 = c_1(2)^1 + c_2(3)^1 \Rightarrow 2c_1 + 3c_2 = 4$
   
   Solving these two equations:
   $$c_1 = 2$$
   $$c_2 = 0$$

5. **Final Solution:**
   Substitute back the constants:
   $$a_n = 2 \cdot 2^n + 0 \cdot 3^n \Rightarrow a_n = 2^{n+1}$$

---

### Type 3: Two Identical Roots
If the characteristic equation yields repeated roots ($r, r$), the solution takes the form:
$$a_n = c_1 \cdot r^n + c_2 \cdot n \cdot r^n$$

---

### Type 4: Dependent on 3 Elements (Distinct Roots)
Equation: $a_n = Xa_{n-1} + Ya_{n-2} + Za_{n-3}$
Roots: $r_1, r_2, r_3$ (All distinct)

**General Solution:**
$$a_n = c_1(r_1)^n + c_2(r_2)^n + c_3(r_3)^n$$

---

### Type 5: 3 Roots, where 2 are Identical
Roots: $r, r, r_1$ (Two roots are the same)

**General Solution:**
$$a_n = c_1 \cdot r^n + c_2 \cdot n \cdot r^n + c_3 \cdot r_1^n$$

---

### Type 6: 3 Identical Roots
Roots: $r, r, r$ (All three roots are the same)

**General Solution:**
$$a_n = c_1 \cdot r^n + c_2 \cdot n \cdot r^n + c_3 \cdot n^2 \cdot r^n$$

---

<!-- Insert diagram showing the mapping of roots to the general solution form for characteristic equations -->

## Linked Notes
- [[DM/long/Generating_Functions_Long.md|Generating Functions]]
- [[DM/long/Combinatorics_Combinations_Repetitions_Long.md|Combinatorics]]


---
## Relevant PYQs

### GATE IT 2008 | Question: 44
[Discussion Link](https://gateoverflow.in/3354/gate-it-2008-question-44)

<p>When $n = 2^{2k}$ for some $k \geqslant 0$, the recurrence relation</p>
<p>$T(n) = √(2) T(n/2) + √n$, $T(1) = 1$</p>
<p>evaluates to :</p>
<ol style="list-style-type:upper-alpha">
<li>$√(n) (\log n + 1)$</li>
<li>$√(n) \log n$</li>
<li>$√(n) \log √(n)$</li>
<li>$n \log √n$</li>
</ol>

---

### GATE IT 2007 | Question: 76
[Discussion Link](https://gateoverflow.in/3528/gate-it-2007-question-76)

<p>Consider the sequence $\langle x_n \rangle , \: n \geq 0$ defined by the recurrence relation $x_{n+1} = c . x^2_n -2$, where $c &gt; 0$.</p>
<p>Suppose there exists a <strong><em>non-empty, open</em></strong> interval $(a, b)$ such that for all $x_0$ satisfying $a &lt; x_0 &lt; b$, the sequence converges to a limit. The sequence converges to the value?</p>
<ol style="list-style-type:upper-alpha">
<li>$\frac{1+\sqrt{1+8c}}{2c}$</li>
<li>$\frac{1-\sqrt{1+8c}}{2c}$</li>
<li>$2$</li>
<li>$\frac{2}{2c-1}$</li>
</ol>

---

### GATE IT 2005 | Question: 51
[Discussion Link](https://gateoverflow.in/3812/gate-it-2005-question-51)

<p>Let $T(n)$ be a function defined by the recurrence</p>
<p>$T(n) = 2T(n/2) + \sqrt n$ for $n \geq 2$ and<br/>
$T(1) = 1$</p>
<p>Which of the following statements is <strong>TRUE</strong>?</p>
<ol style="list-style-type:upper-alpha">
<li>$T(n) = \Theta(\log n)$</li>
<li>$T(n) = \Theta(\sqrt n)$</li>
<li>$T(n) = \Theta(n)$</li>
<li>$T(n) = \Theta(n \log n)$</li>
</ol>

---

### GATE IT 2004 | Question: 57
[Discussion Link](https://gateoverflow.in/3700/gate-it-2004-question-57)

<p>Consider a list of recursive algorithms and a list of recurrence relations as shown below. Each recurrence relation corresponds to exactly one algorithm and is used to derive the time complexity of the algorithm.</p>
<p>$$\begin{array}{|l|l|l|l|}\hline \text{}  &amp;  \textbf{Recursive Algorithm } &amp; \text{} &amp; \textbf{Recurrence Relation} \\\hline  \text{P} &amp; \text{Binary search} &amp; \text{l.} &amp; \text{$T(n) = T(n-k) +T(k) +cn$} \\\hline  \text{Q.} &amp; \text{Merge sort} &amp;\text{ll.}  &amp;  \text{$T(n) = 2T(n-1) + 1$ }\\\hline\text{R.}  &amp;  \text{Quick sort}&amp; \text{lll.}  &amp;  \text{$T(n) = 2T(n/2) + cn$}\\\hline \text{S.}  &amp;  \text{Tower of Hanoi} &amp; \text{lV.}  &amp;  \text{$T(n) = T(n/2) + 1$} \\\hline \end{array}$$</p>
<p>Which of the following is the correct match between the algorithms and their recurrence relations?</p>
<ol style="list-style-type:upper-alpha">
<li>$\text{P-II, Q-III, R-IV, S-I}$</li>
<li>$\text{P-IV, Q-III, R-I, S-II}$</li>
<li>$\text{P-III, Q-II, R-IV, S-I}$</li>
<li>$\text{P-IV, Q-II, R-I, S-III}$</li>
</ol>

---

### GATE CSE 2023 | Question: 5
[Discussion Link](https://gateoverflow.in/399307/gate-cse-2023-question-5)

<p>The Lucas sequence $L_{n}$ is defined by the recurrence relation:<br/>
\[<br/>
L_{n}=L_{n-1}+L_{n-2}, \quad \text { for } \quad n \geq 3,<br/>
\]<br/>
with $L_{1}=1$ and $L_{2}=3$.</p>
<p>Which one of the options given is TRUE?</p>
<ol style="list-style-type:upper-alpha">
<li>$L_{n}=\left(\frac{1+\sqrt{5}}{2}\right)^{n}+\left(\frac{1-\sqrt{5}}{2}\right)^{n}$</li>
<li>$L_{n}=\left(\frac{1+\sqrt{5}}{2}\right)^{n}-\left(\frac{1-\sqrt{5}}{3}\right)^{n}$</li>
<li>$L_{n}=\left(\frac{1+\sqrt{5}}{2}\right)^{n}+\left(\frac{1-\sqrt{5}}{3}\right)^{n}$</li>
<li>$L_{n}=\left(\frac{1+\sqrt{5}}{2}\right)^{n}-\left(\frac{1-\sqrt{5}}{2}\right)^{n}$</li>
</ol>

---
