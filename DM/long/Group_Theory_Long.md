---
tags:
  - gate
  - dm
  - long
  - relations
---
# Group Theory - Comprehensive Notes

## Introduction to Algebraic Structures
An algebraic structure is a combination of a non-empty set and one or more binary operations defined on it. It is usually denoted as `(S, *)`, where `S` is the set and `*` is the binary operation.

For a set `G` and an operation `*`, a **Group** is formed when certain properties are satisfied. Let's delve into the properties that build up to a group.

## Properties of Algebraic Structures

1. **Closure**:
   For any $a, b \in G$, the result of the operation $a * b$ must also belong to $G$. 
   If this holds, the set `G` is said to be *closed* under the operation `*`.

2. **Associativity**:
   For any $a, b, c \in G$, the equation $a * (b * c) = (a * b) * c$ must hold true. The order of applying the operation does not change the final result.

3. **Identity Element**:
   There must exist an element $e \in G$ such that for any $a \in G$:
   $$a * e = e * a = a$$
   > **Note**: The identity element is always unique for a given set and operation.

4. **Inverse Element**:
   For each element $a \in G$, there must exist an element $a^{-1} \in G$ such that:
   $$a * a^{-1} = a^{-1} * a = e$$
   Where $e$ is the identity element.

5. **Commutativity**:
   For any $a, b \in G$, the equation $a * b = b * a$ holds true.

---

## Types of Algebraic Structures (Hierarchy)

Depending on which of the above properties are satisfied, the algebraic structure `(G, *)` is classified as follows:

| Algebraic Structure | Closure | Associativity | Identity | Inverse | Commutativity |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Groupoid / Magma** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Semi Group** | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Monoid** | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Group** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Abelian Group** | ✅ | ✅ | ✅ | ✅ | ✅ |

### Intuitive Explanations
- **Semi Group**: "It's a closed system where chaining operations together doesn't depend on how you bracket them." Examples: String concatenation is a semi group (closed and associative, but no inverse).
- **Monoid**: "It's a semi group that has a 'do nothing' element." Example: Multiplication on Integers, where $1$ is the identity element.
- **Group**: "It's a monoid where every action can be completely completely 'undone'." Example: Addition on Integers. (0 is identity, $-a$ is inverse of $a$).
- **Abelian Group**: "It's a group where the order in which you combine two elements doesn't matter at all." Example: Addition on Integers ($a+b = b+a$).

---

## Relevant PYQs (Previous Year Questions)

### Question 1: GATE CSE 1997 | Question 3.1
[Discussion Link](https://gateoverflow.in/2232/gate-cse-1997-question-3-1)
Let $\left(Z, *\right)$ be an algebraic structure where $Z$ is the set of integers and the operation $*$ is defined by $n*m = \max(n,m)$. Which of the following statements is true for $\left(Z, *\right)$?
A. $\left(Z, *\right)$ is a monoid
B. $\left(Z, *\right)$ is an Abelian group
C. $\left(Z, *\right)$ is a group
D. None of the above

### Question 2: GATE CSE 1995 | Question 2.17
[Discussion Link](https://gateoverflow.in/2629/gate-cse-1995-question-2-17)
Let $A$ be the set of all non-singular matrices over real number and let $*$ be the matrix multiplication operation. Then
A. $A$ is closed under $*$ but $\langle A, *\rangle$ is not a semigroup.
B. $\langle A, *\rangle$ is a semigroup but not a monoid.
C. $\langle A, * \rangle$ is a monoid but not a group.
D. $\langle A, *\rangle$ is a group but not an abelian group.

### Question 3: GATE CSE 1990 | Question 2-x
[Discussion Link](https://gateoverflow.in/84039/gate-cse-1990-question-2-x)
Match the pairs in the following questions:
(a) Groups -> (p) Associativity
(b) Semigroups -> (q) Identity
(c) Monoids -> (r) Commutativity
(d) Abelian groups -> (s) Left inverse

### Question 4: GATE CSE 2005 | Question 46
[Discussion Link](https://gateoverflow.in/1171/gate-cse-2005-question-46)
Consider the set $H$ of all $3 * 3$ matrices of the type given in the question where $a,b,c,d,e,f$ are real numbers and $abc \neq 0$. Under the matrix multiplication operation, the set $H$ is:
A. a group
B. a monoid but not a group
C. a semi group but not a monoid
D. neither a group nor a semi group
