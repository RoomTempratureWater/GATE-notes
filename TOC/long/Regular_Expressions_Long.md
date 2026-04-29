# Regular Expressions
*Tags: #toc #automata #regular_expression #long*

## Introduction
Operators and operands together form an **expression**. Operands can also be expressions. In Theory of Computation, regular expressions are used to represent regular sets (regular languages).

## Operators
To represent a regular set, we use four main operators:
- **Unary Operators**: Kleene Star ($R^*$) and Kleene Plus ($R^+$)
- **Binary Operators**: OR/Union ($R_1 + R_2$) and Concatenation ($R_1 \cdot R_2$)

### 1. OR (+)
The OR operator means either $R_1$ or $R_2$.
Example: $a + b$ generates $\{a, b\}$ (but not $ab, aa$, or $bb$).
$(aa + ab) + (a + \epsilon) = \epsilon + a + aa + ab$

### 2. Concatenation ($\cdot$)
$a \cdot b$ means $a$ followed by $b$ (order matters). It generates $\{ab\}$. It is not equivalent to $b \cdot a$.

> [!NOTE]
> **Difference between $\epsilon$ (epsilon) and $\emptyset$ (phi)**
> - **$\epsilon$ (epsilon)**: The empty string (a string of length 0), i.e., $\{ "" \}$
> - **$\emptyset$ (phi)**: The empty language (a set with no strings), i.e., $\{ \}$
> 
> **Key distinction**: $\epsilon$ is a valid string, whereas $\emptyset$ contains no strings at all.
> **Examples**:
> - $a \cdot \epsilon = a$ (concatenation with $\epsilon$ does nothing)
> - $a + \epsilon = \{ "a", "" \}$ (adds empty string as a choice)
> - $a + \emptyset = \{ "a" \}$ (adds nothing)

### Properties of OR (+) and Concatenation ($\cdot$)

| Property | OR ($+$) | Concatenation ($\cdot$) |
| :--- | :--- | :--- |
| **Identity** | $R + \emptyset = R$ (Identity is $\emptyset$) | $R \cdot \epsilon = R$ (Identity is $\epsilon$) |
| **Associative** | $(R_1 + R_2) + R_3 = R_1 + (R_2 + R_3)$ <br> e.g., $\{a, b\} + c = a + \{b, c\}$ | $(ab) \cdot c = a \cdot (bc) \implies \{abc\} = \{abc\}$ |
| **Commutative** | $a + b = b + a \implies \{a, b\} = \{b, a\}$ | $a \cdot b \neq b \cdot a$ (Not commutative) |
| **Annihilator / Dominator** | $R + \Sigma^* = \Sigma^*$ (since $R \subseteq \Sigma^*$) | $R \cdot \emptyset = \emptyset$ |
| **Distributive** | OR is *not* distributive over Concat: <br> $a + b \cdot c \neq (a+b) \cdot (a+c)$ | Concat is distributive over OR: <br> $a \cdot (b+c) = (a \cdot b) + (a \cdot c)$ |

### 3. Kleene Star ($R^*$)
Represents zero or more occurrences.
$a^* = a^0 + a^1 + a^2 + \dots = \{\epsilon, a, aa, aaa, \dots\}$
$(a+b)^* = \{\epsilon, a, b, aa, bb, ab, ba, aaa, \dots\}$

### 4. Kleene Plus ($R^+$)
Represents one or more occurrences.
$a^+ = a^1 + a^2 + a^3 + \dots$
$(ab)^+ = \{ab, abab, ababab, \dots\}$

Relation between Star and Plus:
$R^* = R^+ + \epsilon$
Note: $R^+ = R^*$ is possible in some cases (e.g., if $\epsilon \in R$).

### Quick Equivalences
- $a + \emptyset = a$
- $a^* + \epsilon = a^*$
- $(a+\epsilon)^+ = a^*$
- $\emptyset^+ = \emptyset$
- $\emptyset^* = \epsilon$
- $\epsilon^+ = \epsilon$

### Operations involving Star and Plus
- $(a^+)^+ = a^+$
- $(a^+)^* = a^*$
- $(a^*)^+ = a^*$
- $(a^*)^* = a^*$
- $a^+ + a^+ = a^+$
- $a^+ + a^* = a^*$
- $a^+ \cdot a^* = a^+$
- $a^* \cdot a^* = a^*$
- $a^+ \cdot a^+ = aa^+$

### Important Expressions for Exams
1. $aa^*$ : Set of all strings of 'a's with length $\ge 1$.
2. $(a + \epsilon)^+$ : Equivalently $a^*$.
3. $(a+b)^*$ : Universal language over $\{a, b\}$.
4. $a(a + b)^*$ : All strings starting with 'a'.
5. $(a+b)^*a$ : All strings ending with 'a'.
6. $(a+b)^*a(a+b)^*$ : All strings containing at least one 'a'.

### Special Cases
- $a^* + b^* = \{\epsilon, a, aa, aaa \dots, b, bb, bbbb \dots\}$
- $a^*b^* = \{\epsilon, a, b, ab, aab, aaab, abb, abbb, \dots\}$ (Cannot generate strings starting with 'b' followed by 'a')
Note that $a^*b^* \neq b^*a^*$ but $(a^*b^*)^* = (b^*a^*)^*$ (which is $(a+b)^*$).

## Answers to Questions
**Q: Write the regular expression for $L = \{w \mid w \in \{0, 1\}^*, |w| \ge 2\}$.**
A: A string of length at least 2 means it must have any two characters from $\{0, 1\}$, followed by any sequence of characters from $\{0, 1\}^*$.
Regular Expression: $(0+1)(0+1)(0+1)^*$



---
## Relevant PYQs

### GATE IT 2008 | Question: 5
[Discussion Link](https://gateoverflow.in/3265/gate-it-2008-question-5)

<p>Which of the following regular expressions describes the language over$\{0, 1\}$ consisting of strings that contain exactly two $1$'s?</p>
<ol style="list-style-type:upper-alpha">
<li>$(0 + 1)^ * \ 11(0 + 1) ^*$</li>
<li>$0 ^* \ 110 ^*$</li>
<li>$0 ^* 10 ^* 10 ^*$</li>
<li>$(0 + 1) ^* 1(0 + 1) ^* 1 (0 + 1) ^*$</li>
</ol>

---

### GATE IT 2008 | Question: 32
[Discussion Link](https://gateoverflow.in/3342/gate-it-2008-question-32)

<p>If the final states and non-final states in the DFA below are interchanged, then which of the following languages over the alphabet $\{a, b\}$ will be accepted by the new DFA?</p>
<p style="text-align:center"><img alt="" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=6965556390260869954"/></p>
<ol style="list-style-type:upper-alpha">
<li>Set of all strings that do not end with $ab$</li>
<li>Set of all strings that begin with either an $a$ or $a \ b$</li>
<li>Set of all strings that do not contain the substring $ab$,</li>
<li>The set described by the regular expression $b^*aa^*(ba)^*b^*$</li>
</ol>

---

### GATE IT 2007 | Question: 73
[Discussion Link](https://gateoverflow.in/3525/gate-it-2007-question-73)

<p>Consider the regular expression $R = (a + b)^* \ (aa + bb) \ (a + b)^*$</p>
<p>Which one of the regular expressions given below defines the same language as defined by the regular expression $R$ ?</p>
<ol style="list-style-type:upper-alpha">
<li>$(a(ba)^* + b(ab)^*)(a + b)^+$</li>
<li>$(a(ba)^* + b(ab)^*)^*(a + b)^*$</li>
<li>$(a(ba)^* (a + bb) + b(ab)^*(b + aa))(a + b)^*$</li>
<li>$(a(ba)^* (a + bb) + b(ab)^*(b + aa))(a + b)^+$</li>
</ol>

---

### GATE IT 2007 | Question: 72
[Discussion Link](https://gateoverflow.in/3524/gate-it-2007-question-72)

<p>Consider the regular expression $R = (a + b)^* (aa + bb) (a + b)^*$</p>
<p>Which deterministic finite automaton accepts the language represented by the regular expression $R$?</p>
<ol class="shrink-inline-options2" style="list-style-type:upper-alpha">
<li><img alt="" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=4084850553518558507" width="305"/></li>
<li><img alt="" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=11679686363708204198" width="305"/></li>
<li><img alt="" height="258" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=11949589107834012596" width="350"/></li>
<li><img alt="" height="263" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=9562195758838204990" width="356"/></li>
</ol>

---

### GATE IT 2007 | Question: 71
[Discussion Link](https://gateoverflow.in/3523/gate-it-2007-question-71)

<p>Consider the regular expression $R = (a + b)^* (aa + bb) (a + b)^*$</p>
<p>Which of the following non-deterministic finite automata recognizes the language defined by the regular expression $R$? Edges labeled $\lambda $ denote transitions on the empty string.</p>
<ol class="shrink-inline-options2" style="list-style-type:upper-alpha">
<li><br/>
<img alt="" height="279" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=16554358242410702602" width="316"/></li>
<li><br/>
<img alt="" height="396" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=8774152576908859544" width="323"/></li>
<li><br/>
<img alt="" height="413" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=5748350196593249481" width="336"/></li>
<li><br/>
<img alt="" height="414" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=15788213930690656023" width="335"/></li>
</ol>

---
