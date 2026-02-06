#gate #dm #long #logic #propositional_logic

# Propositional Logic

**Date:** 03/02/2026
**Youtube Link:** [Lecture](https://www.youtube.com/watch?v=1txRUu-TwsI&list=PL3eEXnCBViH9TTRzwOcwbXtUVK8-NHZrJ&index=10)

---

## Introduction to Logic
In logic, we deal with **statements** (or propositions) that can be clearly classified as **True (T)** or **False (F)**.

Statements can be divided into two types:
1.  **Simple Statements**: A statement that cannot be broken down into smaller statements.
    *   *Example:* "It is raining." ($p$)
2.  **Compound Statements**: A statement formed by combining two or more simple statements using logical connectives.
    *   *Example:* "It is raining AND I will take an umbrella." ($p \land q$)

basically the statements which give us a proposition.

---

## Logical Connectives

Connectives are used to join simple statements to form compound statements. The four main connectives are:

### 1. Conjunction (AND) - $(\land)$
The statement $p \land q$ is True only when **both** $p$ and $q$ are True.

| $p$ | $q$ | $p \land q$ |
| :---: | :---: | :---: |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

### 2. Disjunction (OR) - $(\lor)$
The statement $p \lor q$ is False only when **both** $p$ and $q$ are False. (This is inclusive OR).

| $p$ | $q$ | $p \lor q$ |
| :---: | :---: | :---: |
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

### 3. Single Implication (If... Then) - $(\to)$
The statement $p \to q$ is False **only** when $p$ is True (Antedecent) and $q$ is False (Consequent). In all other cases, it is True.

| $p$ | $q$ | $p \to q$ |
| :---: | :---: | :---: |
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

### 4. Double Implication (If and only if) - $(\leftrightarrow)$
The statement $p \leftrightarrow q$ is True when both $p$ and $q$ have the **same truth value**.

| $p$ | $q$ | $p \leftrightarrow q$ |
| :---: | :---: | :---: |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

---

## Classification of Propositions

### Satisfiable Expression
An expression is **Satisfiable** if the result of the expression is True for **at least one** combination of input values.
*   *Note:* All Tautologies and Contingencies are Satisfiable.

### Tautology (Valid Expression)
An expression is a **Tautology** if the result is **True (T)** for **ALL** possible combinations of input values.
*   *Rule:* All Valids are Satisfiable, but not all Satisfiables are Valid.
*   *Notation:* $\vDash P$

### Contradiction (Unsatisfiable)
An expression is a **Contradiction** if the result is **False (F)** for **ALL** possible combinations of input values.

### Contingency
An expression is a **Contingency** if the result contains a **mixture** of True and False values (neither a Tautology nor a Contradiction).
*   *Rule:* All Contingencies are Satisfiable.

---

## Example Problem: Tautology Check

**Question:** Is the following expression a Tautology?
$$[a \land (a \to b) \land (\neg b \lor c)] \to c$$

**Solution (Proof by Falsification):**
Instead of drawing a full truth table (which would have $2^3 = 8$ rows), we can try to prove the expression is **FALSE**. If we fail to make it False (i.e., we encounter a contradiction in our assumption), then it must be a Tautology.

1.  **Assume the expression is FALSE.**
    For an implication $X \to Y$ to be False, we must have $X$ is True and $Y$ is False.
    *   So, let $c = F$ (False).
    *   And $[a \land (a \to b) \land (\neg b \lor c)]$ must be True.

2.  **Analyze the Left Side (Antecedent):**
    Since it is a conjunction ($AND$), for it to be True, **all** parts must be True:
    *   $a = T$
    *   $(a \to b) = T$
    *   $(\neg b \lor c) = T$

3.  **Evaluate Step-by-Step:**
    *   We already found $c = F$.
    *   Look at $(\neg b \lor c)$. Since $c$ is False, for the OR statement to be True, $\neg b$ must be True.
        *   $\implies \neg b = T \implies b = F$.
    *   We already found $a = T$.
    *   Now check $(a \to b)$ with $a=T$ and $b=F$.
        *   $(T \to F)$ results in **False**.

4.  **Contradiction:**
    We assumed the antecedent was True, which required $(a \to b)$ to be True. However, our derived values ($a=T, b=F$) make $(a \to b)$ False.
    This is a contradiction.

5.  **Conclusion:**
    It is **impossible** to make the expression False. Therefore, the expression is a **Tautology**.

---

## Inference Rules

In an inference rule, the left side of the implication is called the **Premises** (or Antecedent) and the right side is called the **Conclusion** (or Consequent).

We consider the premises as **True**, then check the conclusion:
*   If the conclusion is **True**, it follows the inference rule (Valid).
*   If the conclusion is **False**, it does not follow the inference rule (Invalid).

### Example: Disjunctive Syllogism

**Premises:**
*   $P_1$: Mobile phone is in left OR right pocket. (True)
*   $P_2$: It is NOT in the left pocket. (True)

**Conclusion:**
*   $Q$: It MUST be in the right pocket. (True)

**Logical Form:**
Let $L$ = "Phone is in Left pocket"
Let $R$ = "Phone is in Right pocket"

1.  $P_1: L \lor R$
2.  $P_2: \neg L$
3.  $\therefore R$

**Explanation:**
If we know that at least one of $L$ or $R$ is true ($L \lor R$), and we find out that $L$ is specifically false ($\neg L$), the only remaining possibility for the first statement to hold true is for $R$ to be true. Thus, $R$ is a valid conclusion. This is a standard inference rule known as **Disjunctive Syllogism**.

### Standard Logical Identities and Inference Rules
*(Refer to the image below for visual derivations)*

![[Photos/Pasted image 20260203_propositional_logic.png]]

Some key rules derivation shown in the image (recreated below):

1.  **Modus Ponens**
    $$[a \land (a \to b)] \to b$$
    *   Premise 1: $a \to b$
    *   Premise 2: $a$
    *    Conclusion: $b$

2.  **Modus Tollens**
    $$[(a \to b) \land \neg b] \to \neg a$$ (derived from contrapositive)

3.  **Disjunctive Syllogism**
    $$[(a \lor b) \land \neg a] \to b$$
    *   Premise 1: $a \lor b$
    *   Premise 2: $\neg a$
    *   Conclusion: $b$

4.  **Hypothetical Syllogism**
    $$[(a \to b) \land (b \to c)] \to (a \to c)$$
    *   Premise 1: $a \to b$
    *   Premise 2: $b \to c$
    *   Conclusion: $a \to c$

5.  **Resolution**
    $$[(a \lor b) \land (\neg b \lor c)] \to (a \lor c)$$

---

## Relevant PYQs

### GATE IT 2008 | Question 1
**Question:**
If $A \to BC$ and $A \to B$ then $A \to C$.
Exactly how many of the above implications are valid?
(A) 0
(B) 1
(C) 2
(D) 3

[Discussion Link](https://gateoverflow.in/3222/gate-it-2008-question-1)

---
