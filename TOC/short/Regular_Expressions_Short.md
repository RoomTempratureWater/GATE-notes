# Regular Expressions (Short Notes)
*Tags: #toc #automata #regular_expression #short*

Regular expressions (regex) operators operands ke saath use hote hai regular sets (languages) ko represent karne ke liye.

## 4 Main Operators
1. **OR (+)**: $a + b$ matlab ya toh 'a' ya 'b'. $\implies \{a, b\}$
2. **Concatenation ($\cdot$)**: $a \cdot b$ matlab 'a' ke baad 'b'. $\implies \{ab\}$. Note: $a \cdot b \neq b \cdot a$.
3. **Kleene Star ($*$):** Zero or more occurrences. $a^* = \{\epsilon, a, aa, aaa \dots\}$
4. **Kleene Plus ($+$):** One or more occurrences. $a^+ = \{a, aa, aaa \dots\}$

$R^* = R^+ + \epsilon$

> [!NOTE]
> **Difference: $\epsilon$ vs $\emptyset$**
> - **$\epsilon$ (Epsilon):** Empty string (length 0). It's a valid string.
> - **$\emptyset$ (Phi):** Empty language (no strings at all).
> - **Trick:** $a \cdot \epsilon = a$ (identity for concat), $a + \emptyset = a$ (identity for OR).

## Properties Table

| Property | OR ($+$) | Concatenation ($\cdot$) |
| :--- | :--- | :--- |
| **Identity** | $\emptyset$ ($a + \emptyset = a$) | $\epsilon$ ($a \cdot \epsilon = a$) |
| **Commutative** | Yes ($a+b = b+a$) | No ($ab \neq ba$) |
| **Associative** | Yes | Yes |
| **Dominator** | $\Sigma^*$ ($a + \Sigma^* = \Sigma^*$) | $\emptyset$ ($a \cdot \emptyset = \emptyset$) |
| **Distributive**| No | Yes (Concat distributes over OR) |

## Quick Hacks / Simplifications
- $\emptyset^* = \epsilon$
- $\emptyset^+ = \emptyset$
- $\epsilon^+ = \epsilon$
- $(a+\epsilon)^+ = a^*$
- $(a^*)^* = a^*$
- $(a^+)^* = (a^*)^+ = a^*$
- $a^+ \cdot a^* = a^+$
- $a^* \cdot a^* = a^*$

## Standard Regex
- Starts with 'a': $a(a+b)^*$
- Ends with 'a': $(a+b)^*a$
- Contains 'a': $(a+b)^*a(a+b)^*$
- $(a^*b^*)^* = (a+b)^*$

**Problem:** $L = \{w \mid w \in \{0, 1\}^*, |w| \ge 2\}$
**Regex:** $(0+1)(0+1)(0+1)^*$



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
