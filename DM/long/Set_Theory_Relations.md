---
tags:
  - gate
  - dm
  - relations
  - sets
  - long
---

# Set Theory - Relations Basics

[[DM/short/Set_Theory_Relations_Short.md|Short Notes]]

## Introduction

In Set Theory, a **Relation** is a way to describe a connection between elements of sets.

Given two sets $A$ and $B$, the **Cartesian Product** $A \times B$ is the set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$.
$$A \times B = \{(a, b) \mid a \in A, b \in B\}$$

A **Relation** $R$ from set $A$ to set $B$ is a subset of the Cartesian product $A \times B$.
$$R \subseteq A \times B$$

If $(a, b) \in R$, we say "$a$ is related to $b$" and denote it as $a R b$.

### Relations on a Single Set
Most often, we talk about a relation on a single set $A$, which means $R \subseteq A \times A$.

---

## Counting Relations

### Total Number of Relations from A to B
Let $|A| = m$ and $|B| = n$.
The number of elements in $A \times B$ is $|A \times B| = m \cdot n$.
Since a relation is any subset of $A \times B$, the total number of possible relations is the number of subsets of $A \times B$, which is the power set size.

$$\text{Total Relations} = 2^{|A \times B|} = 2^{mn}$$

### Total Number of Relations on A
Let $|A| = n$.
Then $|A \times A| = n^2$.
Total number of relations on $A$ is:
$$\text{Total Relations} = 2^{n^2}$$

---

## Types of Relations

### 1. Reflexive Relation
A relation $R$ on set $A$ is **Reflexive** if every element of $A$ is related to itself.
$$\forall a \in A, (a, a) \in R$$

**Example:**
$A = \{1, 2, 3\}$
$R = \{(1, 1), (2, 2), (3, 3), (1, 2)\}$ is Reflexive because $(1,1), (2,2), (3,3)$ are all present.
$R' = \{(1, 1), (2, 2)\}$ is **Not Reflexive** because $(3, 3) \notin R'$.

**Counting Reflexive Relations:**
To form a reflexive relation, all $n$ diagonal elements $\{(a,a) \mid a \in A\}$ **must** be included.
The remaining $n^2 - n$ off-diagonal elements can either be in the set or not (2 choices each).

$$\text{Number of Reflexive Relations} = 1^n \cdot 2^{n^2 - n} = 2^{n^2 - n}$$

### 2. Symmetric Relation
A relation $R$ is **Symmetric** if for every pair $(a, b) \in R$, the pair $(b, a)$ is also in $R$.
$$\forall a, b \in A, ((a, b) \in R \implies (b, a) \in R)$$

**Informal check:** If you flip every pair in the relation, you should get the same set of pairs back.

**Example:**
$A = \{1, 2, 3\}$
$R = \{(1, 2), (2, 1), (3, 3)\}$ is Symmetric.
$R' = \{(1, 2)\}$ is **Not Symmetric** because $(2, 1) \notin R'$.

**Counting Symmetric Relations:**
- Diagonal elements $(a, a)$: We have $n$ such elements. Each can be present or absent (2 choices). Total $2^n$ ways.
- Off-diagonal pairs $\{(a, b), (b, a)\}$ with $a \neq b$: There are $n^2 - n$ off-diagonal elements, forming $\frac{n^2 - n}{2}$ pairs. For symmetry, if $(a, b)$ is chosen, $(b, a)$ **must** be chosen. So for each pair, we have 2 choices (both present or both absent).
- Total ways = $2^n \cdot 2^{\frac{n^2 - n}{2}} = 2^{\frac{2n + n^2 - n}{2}} = 2^{\frac{n^2 + n}{2}}$.

$$\text{Number of Symmetric Relations} = 2^{\frac{n(n+1)}{2}}$$

### 3. Anti-symmetric Relation
A relation $R$ is **Anti-symmetric** if no two distinct elements are related to each other in both directions.
$$\forall a, b \in A, ((a, b) \in R \land (b, a) \in R \implies a = b)$$

Allowed: $(a, b)$ only, $(b, a)$ only, or neither.
Not Allowed: Both $(a, b)$ and $(b, a)$ if $a \neq b$.
Diagonal elements $(a, a)$ are always allowed.

**Example:**
$A = \{1, 2, 3\}$
$R = \{(1, 2), (2, 3)\}$ is Anti-symmetric.
$R' = \{(1, 2), (2, 1)\}$ is **Not Anti-symmetric**.

**Counting Anti-symmetric Relations:**
- Diagonal elements $(a, a)$: $n$ elements, 2 choices each (present/absent). Total $2^n$.
- Off-diagonal pairs $\{(a, b), (b, a)\}$: There are $\frac{n^2 - n}{2}$ such pairs. For each pair, we have 3 allowed choices:
    1. Only $(a, b)$ is in $R$.
    2. Only $(b, a)$ is in $R$.
    3. Neither is in $R$.
    - Note: We cannot have both.
- Total ways = $2^n \cdot 3^{\frac{n^2 - n}{2}}$.

$$\text{Number of Anti-symmetric Relations} = 2^n \cdot 3^{\frac{n^2 - n}{2}}$$

---

## Operations on Relations

| Property | Union ($R_1 \cup R_2$) | Intersection ($R_1 \cap R_2$) |
| :--- | :--- | :--- |
| **Reflexive** | Reflexive | Reflexive |
| **Symmetric** | Symmetric | Symmetric |
| **Anti-symmetric** | Not Guaranteed | Anti-symmetric |

> **Note on Reflexive Intersection:** If $R_1$ and $R_2$ are reflexive, then for all $a$, $(a,a) \in R_1$ and $(a,a) \in R_2$. Thus $(a,a) \in R_1 \cap R_2$. So the intersection is **always** reflexive.

> **Note on Anti-symmetric Union:** If $R_1 = \{(1, 2)\}$ and $R_2 = \{(2, 1)\}$, both are anti-symmetric. But $R_1 \cup R_2 = \{(1, 2), (2, 1)\}$ which is **not** anti-symmetric.

---

## Detailed Derivations & Explanations

### Why $2^{n^2}$ relations?
Think of the relation as an $n \times n$ adjacency matrix (0 or 1).
A relation can be represented by a matrix $M$ where $M_{ij} = 1$ if $(i, j) \in R$ and $0$ otherwise.
There are $n^2$ entries in the matrix. Each entry can be 0 or 1 (2 choices).
Total possibilities = $\underbrace{2 \times 2 \times \dots \times 2}_{n^2 \text{ times}} = 2^{n^2}$.

### Why Reflexive is $2^{n^2 - n}$?
For a matrix to represent a reflexive relation, the main diagonal (entries $M_{ii}$) **must** all be 1.
- Diagonal entries: 1 choice each (must be 1).
- Off-diagonal entries: $n^2 - n$ entries remaining. Each has 2 choices (0 or 1).
Total = $1^n \times 2^{n^2 - n} = 2^{n^2 - n}$.

### Why Symmetric is $2^{(n^2 + n)/2}$?
For a symmetric matrix, $M_{ij} = M_{ji}$.
- The diagonal entries $M_{ii}$ are independent (2 choices each). Total $n$.
- The upper triangle entries determine the lower triangle. There are $\frac{n^2 - n}{2}$ entries in the upper triangle.
- Once you choose the upper triangle and diagonal, the relation is fixed.
- Total independent choices = $n$ (diagonal) + $\frac{n^2 - n}{2}$ (upper triangle) = $\frac{2n + n^2 - n}{2} = \frac{n^2 + n}{2}$.
- Total relations = $2^{\frac{n(n+1)}{2}}$.

### Why Reflexive AND Symmetric is $2^{(n^2 - n)/2}$?
- Reflexive: Diagonal is fixed to 1 (1 choice).
- Symmetric: Upper triangle determines lower triangle.
- Upper triangle entries: $\frac{n^2 - n}{2}$ entries, 2 choices each.
- Total = $1^n \times 2^{\frac{n^2 - n}{2}} = 2^{\frac{n^2 - n}{2}}$.

---

## Relevant PYQs

### GATE CSE 2021 Set 1 | Question: 43
[Discussion Link](https://gateoverflow.in/357408/gate-cse-2021-set-1-question-43)

<p>A relation $R$ is said to be circular if $a\text{R}b$ and $b\text{R}c$ together imply $c\text{R}a$.</p>
<p>Which of the following options is/are correct?</p>
<ol start="1" style="list-style-type:upper-alpha">
<li>If a relation $S$ is reflexive and symmetric, then $S$ is an equivalence relation.</li>
<li>If a relation $S$ is circular and symmetric, then $S$ is an equivalence relation.</li>
<li>If a relation $S$ is reflexive and circular, then $S$ is an equivalence relation.</li>
<li>If a relation $S$ is transitive and circular, then $S$ is an equivalence relation.</li>
</ol>

**Analysis:**
- An **Equivalence Relation** is Reflexive, Symmetric, and Transitive.
- This question tests properties like circularity combined with others.
- (C) If Reflexive ($aRa$) and Circular ($aRb \land bRc \implies cRa$), we can prove Symmetry and Transitivity.
    - Symmetry: $aRa \land aRb \implies bRa$ (using circular with $c=a$). So Reflexive + Circular $\implies$ Symmetric.
    - Transitivity: $aRb \land bRc \implies cRa$. Since Symmetric, $cRa \implies aRc$. So $aRb \land bRc \implies aRc$. Transitive.
    - Thus Reflexive + Circular $\implies$ Equivalence. Correct.

---
