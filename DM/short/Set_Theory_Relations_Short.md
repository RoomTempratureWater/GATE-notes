---
tags:
  - gate
  - dm
  - relations
  - short
---

# Set Theory - Relations (Short Notes)

[[DM/long/Set_Theory_Relations.md|Long Notes]]

## Basics

**Relation**: Subset of $A \times B$.
Total Relations from $A$ to $B$ ($|A|=m, |B|=n$): **$2^{mn}$**
Total Relations on $A$ ($|A|=n$): **$2^{n^2}$**

---

## Types of Relations & Counting

| Type | Definition | Counting Formula |
| :--- | :--- | :--- |
| **Reflexive** | $\forall a, (a,a) \in R$ | $2^{n^2 - n}$ |
| **Symmetric** | $(a,b) \in R \implies (b,a) \in R$ | $2^{\frac{n(n+1)}{2}}$ |
| **Anti-Symmetric** | $(a,b) \in R \land (b,a) \in R \implies a=b$ | $2^n \cdot 3^{\frac{n(n-1)}{2}}$ |
| **Asymmetric** | $(a,b) \in R \implies (b,a) \notin R$ | $3^{\frac{n(n-1)}{2}}$ |
| **Reflexive & Symmetric** | Both | $2^{\frac{n(n-1)}{2}}$ |

---

## Key Points (Hinglish)

- **Reflexive**: Sab elements ka khud se relation hona chahiye (diagonal elements must be present). E.g., $(1,1), (2,2), (3,3)$.
- **Symmetric**: Agar ek pair hai $(a,b)$, toh uska ulta $(b,a)$ bhi hona chahiye. Check karne ke liye pair ko flip karo, agar set same rahe toh symmetric hai.
- **Anti-Symmetric**: Agar $(a,b)$ aur $(b,a)$ dono hain, toh $a=b$ hona chahiye. Basically, $a \neq b$ ke liye sirf ek direction allow hai ya koi nahi. Dono direction allow nahi hain except diagonal.
- **Operations**:
    - Union/Intersection of **Symmetric** is also **Symmetric**.
    - Union/Intersection of **Reflexive** is also **Reflexive**.
    - Intersection of **Anti-Symmetric** is **Anti-Symmetric** (Union is NOT guaranteed).

---

## Important Formulas Derivation Logic

- **Reflexive**: Diagonal fixed (1 choice). Remaining $n^2 - n$ pairs independent (2 choices).
- **Symmetric**: Diagonal independent (2 choices). Upper triangle ($\frac{n^2-n}{2}$) entries independent. Lower triangle fixed based on upper. Total $n + \frac{n^2-n}{2} = \frac{n(n+1)}{2}$ independent choices.
- **Anti-Symmetric**: Diagonal independent (2 choices). Each off-diagonal pair $\{(a,b), (b,a)\}$ has 3 choices: only $(a,b)$, only $(b,a)$, or neither. Total $2^n \cdot 3^{\frac{n(n-1)}{2}}$.
