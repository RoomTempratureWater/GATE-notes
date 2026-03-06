---
tags:
  - #gate
  - #dm
  - #combinatorics
  - #short
---

# Recurrence Relations (Quick Revision)

Recurrence relation basically ek "recurring relation" hai jahan ek sequence ka term pichle terms pe depend karta hai.
Jaise: $a_n = 2a_{n-1}$ with initial condition $a_0 = 5$.
Isme agar nth term nikalna ho toh loop karna padega $a_0$ se le kar $a_n$ tak. **Discrete Mathematics ka main goal yahan ek direct formula (general solution) nikalna hai taaki bina iterate kiye direct $a_n$ nikal sakein.**

For the example: $a_n = 2^n \cdot a_0$ is the general solution.

**Steps to solve Homogeneous RR using Characteristic Equation:**
1. Put condition into powers of $x$. Example: $a_n = 5a_{n-1} - 6a_{n-2} \Rightarrow x^2 = 5x - 6 \Rightarrow x^2 - 5x + 6 = 0$.
2. Is characteristic equation ke **roots ($r$)** nikalo.
3. Form general solution based on types of roots (see table below).
4. Put **initial conditions** (like $n=0$, $n=1$) on general solution to find constants ($c_1, c_2, \dots$).

---

## Trick / Table for Types of RR Solutions

| Type | Nature of Roots | General Solution Formula ($a_n$) |
| :--- | :--- | :--- |
| **Type 1** | $d$ (Multiplier format) | $a_n = d^n(a_0)$ |
| **Type 2** | Two Distinct ($r_1, r_2$) | $a_n = c_1(r_1)^n + c_2(r_2)^n$ |
| **Type 3** | Two Identical ($r, r$) | $a_n = c_1(r)^n + c_2 \cdot n \cdot r^n$ |
| **Type 4** | Three Distinct ($r_1, r_2, r_3$) | $a_n = c_1(r_1)^n + c_2(r_2)^n + c_3(r_3)^n$ |
| **Type 5** | Three Roots (Two same: $r, r, r_1$) | $a_n = c_1(r)^n + c_2 \cdot n \cdot r^n + c_3(r_1)^n$ |
| **Type 6** | Three Identical ($r, r, r$) | $a_n = c_1(r)^n + c_2 \cdot n \cdot r^n + c_3 \cdot n^2 \cdot r^n$ |

---

## Linked Notes
- [[DM/short/Generating_Functions_Short.md|Generating Functions Quick Notes]]


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
