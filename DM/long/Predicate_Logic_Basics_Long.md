# Predicate Logic Basics

**Date**: 06/02/2026
#gate/dm/long/first_order_logic
**YouTube Link**: [Lecture 9](https://www.youtube.com/watch?v=YQnAXv1UImg&list=PL3eEXnCBViH9TTRzwOcwbXtUVK8-NHZrJ&index=9)

---

## 1. Introduction
**Open Statements**: Statements that contain variables. Their truth value depends on the value assigned to the variables.
*   *Example*: $x$ is an even number. (Truth value depends on $x$)

**Propositional Statements**: Statements with a fixed truth value (True or False).
*   *Example*: $2$ is an even number. (True)

**Predicate Variable**:
A symbol (like $P, Q, R$) used to represent a property or a relation. 
In $P(x)$, $P$ is the predicate denoting the property (e.g., "is even") and $x$ is the subject. The predicate remains constant while the subject varies.

**Domain / Universe of Discourse ($D$)**:
The set of all possible values that the variable can take.
*   *Example*: $D = \{0, 1, 2\}$, $P(x) = x \text{ is even}$.
    *   $P(0) \to T$
    *   $P(1) \to F$
    *   $P(2) \to T$

---

## 2. Quantifiers

Quantifiers are tools used to define the truth value of an open statement over a domain in terms of quantity.

### 2.1 Universal Quantifier ($\forall$)
*   Symbol: $\forall$ (For all, for every, for each)
*   **Definition**: The statement $\forall x P(x)$ is True if and only if $P(x)$ is true for **every** element in the domain.
*   It is False if there is **at least one** element for which $P(x)$ is false (Counterexample).
*   **Logical Equivalence**: $\forall x P(x) \equiv P(x_1) \land P(x_2) \land \dots \land P(x_n)$ (AND relation).

### 2.2 Existential Quantifier ($\exists$)
*   Symbol: $\exists$ (There exists, for some, at least one)
*   **Definition**: The statement $\exists x P(x)$ is True if $P(x)$ is true for **at least one** element in the domain.
*   It is False if $P(x)$ is false for **all** elements.
*   **Logical Equivalence**: $\exists x P(x) \equiv P(x_1) \lor P(x_2) \lor \dots \lor P(x_n)$ (OR relation).

---

## 3. Practice Questions (Truth Values)

**Q1. Domain $D: \mathbb{Z}$ (Integers)**
$\forall x (x^2 \ge 0)$
*   **Answer**: **TRUE**. Square of any integer is non-negative.

**Q2. Domain $D: \{1, 2, 3\}$**
$\exists x (x^2 = 4)$
*   **Answer**: **TRUE**. For $x=2$, $2^2=4$.

**Q3. Domain $D: \{1, 2, 3\}$**
$\forall x (x^2 = 4)$
*   **Answer**: **FALSE**. For $x=1$, $1^2 \ne 4$.

**Q4. Domain $D: \mathbb{Z}$**
$\exists n (n^2 \le 10)$
*   **Answer**: **TRUE**. For $n=1, 2, 3$, it holds.

**Q5. Domain $D: \mathbb{Z}$**
$\forall x (x^2 \le x)$
*   **Answer**: **FALSE**. For $x=2$, $4 \le 2$ is False.

**Q6. Domain $D: \mathbb{N}$ (Natural Numbers)**
$\forall x (x + 1 > x)$
*   **Answer**: **TRUE**.

**Q7. Domain $D: \mathbb{R}$ (Real Numbers)**
$\exists x (x^2 = -1)$
*   **Answer**: **FALSE**. No real number squared is negative.

---

## 4. Logical Distributivity & Implications

We can analyze the relationship between operands ($\land, \lor$) and quantifiers.

### 4.1 Existential over AND ($\exists$ and $\land$)

**Statement**: $\exists x [P(x) \land Q(x)] \implies \exists x P(x) \land \exists x Q(x)$
*   **Validity**: **TRUE**
*   **Proof**:
    Let LHS be True. Then there exists some $c \in D$ such that $P(c) \land Q(c)$ is True.
    This implies $P(c)$ is True $\implies \exists x P(x)$ is True.
    Also $Q(c)$ is True $\implies \exists x Q(x)$ is True.
    Thus, RHS is True.

**Statement**: $\exists x P(x) \land \exists x Q(x) \implies \exists x [P(x) \land Q(x)]$
*   **Validity**: **FALSE**
*   **Counterexample**:
    $D = \{1, 2\}$
    $P(x): x = 1$
    $Q(x): x = 2$
    $\exists x P(x)$ is True (at $x=1$).
    $\exists x Q(x)$ is True (at $x=2$).
    LHS is True.
    $P(x) \land Q(x)$ is False for $x=1$ and False for $x=2$.
    So $\exists x [P(x) \land Q(x)]$ is False.
    $T \implies F$ is False.

### 4.2 Universal over AND ($\forall$ and $\land$)

**Statement**: $\forall x [P(x) \land Q(x)] \iff \forall x P(x) \land \forall x Q(x)$
*   **Validity**: **TRUE** (Both directions hold)
*   **Intuition**: "Everyone likes Apples AND Oranges" is same as "Everyone likes Apples AND Everyone likes Oranges".

### 4.3 Existential over OR ($\exists$ and $\lor$)

**Statement**: $\exists x [P(x) \lor Q(x)] \iff \exists x P(x) \lor \exists x Q(x)$
*   **Validity**: **TRUE** (Both directions hold)

### 4.4 Universal over OR ($\forall$ and $\lor$)

**Statement**: $\forall x P(x) \lor \forall x Q(x) \implies \forall x [P(x) \lor Q(x)]$
*   **Validity**: **TRUE**
*   **Proof**:
    If All are P or All are Q, then definitely for any specific element, it is P or Q.

**Statement**: $\forall x [P(x) \lor Q(x)] \implies \forall x P(x) \lor \forall x Q(x)$
*   **Validity**: **FALSE**
*   **Counterexample**:
    $D = \{1, 2\}$
    $P(x): x=1$, $Q(x): x=2$
    For $x=1$: $P(1) \lor Q(1)$ is $T \lor F = T$.
    For $x=2$: $P(2) \lor Q(2)$ is $F \lor T = T$.
    LHS is True.
    $\forall x P(x)$ is False. $\forall x Q(x)$ is False.
    RHS is False.

---

## 5. Relevant PYQs

### GATE CSE 2023 | Question: 16
**Geetha's Conjecture**: $\forall x(P(x) \implies \exists y Q(x, y))$
Which options imply Geetha's conjecture?
*   (A) $\exists x(P(x) \land \forall y Q(x, y))$
*   (B) $\forall x \forall y Q(x, y)$
*   (C) $\exists y \forall x(P(x) \implies Q(x, y))$
*   (D) $\exists x(P(x) \land \exists y Q(x, y))$

[Link to Discussion](https://gateoverflow.in/399295/gate-cse-2023-question-16)

---
### GATE IT 2008 | Question: 22
Which of the following is the negation of $[ \forall x, \alpha \to (\exists y, \beta \to (\forall u, \exists v, y)) ]$?
(Note: $\alpha, \beta, y$ in question likely refer to predicates or logical structure, need to parse carefully from source if ambiguous, but standard negation rules apply).

[Link to Discussion](https://gateoverflow.in/3283/gate-it-2008-question-22)
