---
tags:
  - gate
  - dm
  - short
  - relations
---
# Group Theory - Short Notes & Cheat Sheet

**Definition**: A group is a combination of a set and a binary operation `(G, *)`.

## Properties of `(G, *)`
1. **Closure**: $\forall a, b \in G, a * b \in G$
2. **Associativity**: $a * (b * c) = (a * b) * c$
3. **Identity Element**: $\exists e \in G$, such that $a * e = a$ (Identity is **unique**)
4. **Inverse Element**: $\forall a \in G, \exists a^{-1} \in G$, such that $a * a^{-1} = e$
5. **Commutativity**: $a * b = b * a$

## Summary Table

| Structure | Closure | Associativity | Identity | Inverse | Commutative |
|---|:---:|:---:|:---:|:---:|:---:|
| **Groupoid (Magma)** | ✅ | | | | |
| **Semi Group** | ✅ | ✅ | | | |
| **Monoid** | ✅ | ✅ | ✅ | | |
| **Group** | ✅ | ✅ | ✅ | ✅ | |
| **Abelian Group** | ✅ | ✅ | ✅ | ✅ | ✅ |

### Important Points
- **Identity element is unique** for any group.
- **Inverse element is unique** for each particular element in a group.
- Example of a monoid: $(Z, \times)$ because integer multiplication is closed, associative, and has identity $1$, but lacks multiplicative inverse for all elements.
- Example of a group: $(Z, +)$ because addition is closed, associative, has identity $0$, and inverse is $-a$.

See [[DM/long/Group_Theory_Long.md|Long Notes]] for PYQs and deeper intuitive understanding.
