---
tags:
  - gate
  - dm
  - relations
  - equivalence_relation
  - short
---

# Relations, Equivalence, and Posets (Short Notes)

[[DM/long/Relations_Equivalence_Posets.md|Long Notes]]

## 1. Transitivity (Tricky Case)

$R$ is transitive agar $(a,b) \in R$ aur $(b,c) \in R$ toh $(a,c) \in R$ hona chahiye.

**Not Transitive ka common example:**
$R_6 = \{(a,b) \mid a + b \le 3\}$
- $a = 2, b = 1, c = 2$ agar le lo.
- $(2, 1)$ aayega (kyunki $2+1 \le 3$).
- $(1, 2)$ aayega (kyunki $1+2 \le 3$).
- Lekin $(2, 2)$ **Nahi aayega** (kyunki $2+2=4 \not\le 3$). Toh transitivity break ho gayi. 

_**Note:** Empty relation $\emptyset$ aur single element ka relation jaise $\{(1,1)\}$ dono he transitive hote hain._

---

## 2. Equivalence vs Partial Order Relation

| Feature | Equivalence Relation (RST) | Partial Order Relation (RAT) |
| :--- | :--- | :--- |
| **Logic** | Reflexive + **Symmetric** + Transitive | Reflexive + **Anti-Symmetric** + Transitive |
| **Flipping** | Allowed (pairs opposite direction mein allowed hai $\implies (a,b)$ and $(b,a)$) | Not Allowed (except single element self-loops like $(a,a)$) |
| **Example** | Congruence Modulo (divisible by $k$) | Divisibility ($a$ divides $b$) |

---

## 3. Posets (Partially Ordered Sets)

Poset ek combination hai **(Set, Relation)** jisme Relation **Partial Order** (RAT) honi chahiye.

### Hasse Diagram Steps:
1. Pura relation ka graph banao.
2. Self-loops hta do (Reflexivity assume hoti hai).
3. Transitive edges hta do (Direct jumps remove kar do).
4. Sirf un-directed jaisi lines rakho, direction humesha bottom se top assume hoti hai.

*(Divisors of 12 $D_{12}$ ka Hasse Diagram normal tree/diamond shape banta hai with 1 at bottom, 12 at top).*

---

## 4. Bounds (LUB & GLB)

Agar subset $B$ diya hai kisi poset $(A, R)$ se:
- **Upper Bound**: $A$ ka element jo $B$ ke sab elements ke "upar" ho (related ho). (Ex: Common Multiple)
- **Lower Bound**: $A$ ka element jisse $B$ ke sab elements "upar" ho. (Ex: Common Divisor)

**Main Points:**
- **Least Upper Bound (LUB)**: Sabhi upper bounds mein se sabse chota. Jisko **Supremum** bhi kehte hain. (Think: LCM)
- **Greatest Lower Bound (GLB)**: Sabhi lower bounds mein se sabse bada. Jisko **Infimum** bhi kehte hain. (Think: GCD)

---

## 5. Lattices

**Definition**: Agar ek poset mein **har pair** (every two elements) ka **LUB** aur **GLB** dono exist karte hain toh wo Poset ek **Lattice** ban jata hai.
- Ex: $(D_{12}, |)$ ek lattice hai kyunki koi bhi do divisors ka LCM aur GCD exist karta hai aur usi set mein hai.
