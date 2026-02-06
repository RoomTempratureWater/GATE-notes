# Predicate Logic (Revision)

**Topic**: DM
**Subtopic**: Predicate Logic

---

### Key Concepts

*   **P(x)**: Open Statement (Logic depend on x).
*   **Universe/Domain (D)**: Set of all values x can take.

### Quantifiers

1.  **Universal ($\forall$) - "For All"**
    *   True iff $P(x)$ is True for **every** $x \in D$.
    *   Like a big **AND**: $P(1) \land P(2) \land \dots$
    *   To prove False: Find **1 counterexample**.

2.  **Existential ($\exists$) - "There Exists"**
    *   True iff $P(x)$ is True for **at least one** $x \in D$.
    *   Like a big **OR**: $P(1) \lor P(2) \lor \dots$
    *   To prove False: Show it is never true.

### Rules of Distribution

| Statement | Equivalent Split? | Status | Note |
| :--- | :--- | :--- | :--- |
| $\forall x (P(x) \land Q(x))$ | $\forall x P(x) \land \forall x Q(x)$ | **Valid** | $\forall$ distributes over $\land$ |
| $\forall x (P(x) \lor Q(x))$ | $\forall x P(x) \lor \forall x Q(x)$ | **Invalid** | LHS can be mixed, RHS needs all P or all Q |
| $\exists x (P(x) \lor Q(x))$ | $\exists x P(x) \lor \exists x Q(x)$ | **Valid** | $\exists$ distributes over $\lor$ |
| $\exists x (P(x) \land Q(x))$ | $\exists x P(x) \land \exists x Q(x)$ | **Invalid** | LHS needs same x, RHS can have diff x |

### Important Implications (Valid Directions)
*   $\forall x P(x) \lor \forall x Q(x) \implies \forall x (P(x) \lor Q(x))$
*   $\exists x (P(x) \land Q(x)) \implies \exists x P(x) \land \exists x Q(x)$

### Negation Rules (De Morgan's for Logic)
*   $\neg (\forall x P(x)) \equiv \exists x (\neg P(x))$
*   $\neg (\exists x P(x)) \equiv \forall x (\neg P(x))$

### Quick Questions
1. D={1,2,3}, $\forall x(x^2=4)$ -> **False** (fails for 1)
2. D=Z, $\exists n(n^2 \le 10)$ -> **True** (e.g., n=1)
3. $\neg [\forall x P(x)]$ -> $\exists x \neg P(x)$
