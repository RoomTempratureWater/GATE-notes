# Propositional Logic (Short Notes)

**Date:** 03/02/2026

---

## Quick Concepts (Hinglish)

### 1. Types of Statements
*   **Simple Statement**: Jisko aur tod nahi sakte. Ex: "It is raining" (p).
*   **Compound Statement**: Jisme connectives (AND, OR) use hote hain. Ex: "It is raining AND I am happy".

### 2. Connectives & Truth Table Shortcuts

| Connective | Symbol | Hint (Hinglish) |
| :--- | :---: | :--- |
| **AND** | $\land$ | True tabhi hoga jab **dono** True honge. (Sab sahi hona chahiye). |
| **OR** | $\lor$ | False tabhi hoga jab **dono** False honge. (Ek bhi sahi toh sab sahi). |
| **Implication** | $\to$ | **Only False case:** $T \to F$ is **FALSE**. Baaki sab True. (Pehle wala sahi, doosra galat = Galat). |
| **Bi-Implication** | $\leftrightarrow$ | Agar dono ki value **SAME** hai ($T \leftrightarrow T$ ya $F \leftrightarrow F$) toh True. Different hai toh False. |

---

## Definitions (Yaad rakho)

1.  **Satisfiable**: Jaldi se check karo ki kya *kam se kam ek* baar True aa raha hai? Agar haan, toh wo Satisfiable hai. (Tautology bhi satisfiable hoti hai).
2.  **Tautology (Valid)**: Agar **SAARE** cases (combinations) mein result **True** hai.
    *   *Tip:* Prove karne ke liye ulta socho. Try karo expression ko **False** prove karne ki. Agar fail ho gaye (contradiction mili), toh wo Tautology hai.
3.  **Contradiction**: Agar **SAARE** cases mein result **False** hai.
4.  **Contingency**: Mixed result. Kabhi True, kabhi False.

---

## Inference Rule Check

Premise ko **True** maano, aur check karo ki Conclusion bhi **True** aa raha hai ya nahi.

**Example (Phone wala):**
*   $P_1$: Phone Left ya Right pocket mein hai ($L \lor R$).
*   $P_2$: Phone Left mein nahi hai ($\neg L$).
*   **Result**: Toh pakka Right mein hoga ($R$).
*   Yeh **Valid** hai. (Disjunctive Syllogism).

---

## Important Rules

![Logic Rules](../../Photos/Pasted%20image%2020260203_propositional_logic.png)

1.  **Modus Ponens**: $a \to b$ aur $a$ diya hai -> toh $b$ true hoga.
2.  **Modus Tollens**: $a \to b$ aur $\neg b$ diya hai -> toh $\neg a$ true hoga.
3.  **Hypothetical Syllogism**: Chain rule. $a \to b$ aur $b \to c$ -> toh $a \to c$.

---
