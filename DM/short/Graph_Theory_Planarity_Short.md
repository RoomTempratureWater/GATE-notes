#gate #dm #short #graphs

# Planarity (Short Notes)

## Basic Concepts
- **Planar Graph**: Graph jo draw kiya ja sake bina edges cross kiye.
- **Bounded Region**: Finite area enclosed by edges.
- **Unbounded Region**: Outer infinite area (Always 1).
- **Standard Non-Planar Graphs**:
    - **$K_5$**: Smallest non-planar by vertices ($n=5$).
    - **$K_{3,3}$**: Smallest non-planar by edges ($e=9$).

> [!NOTE]
> $K_5$ aur $K_{3,3}$ dono regular graphs hain. Dono non-planar hain par **ek edge remove karne se planar ban jate hain**.

---

## Formulas & Theorems

### 1. Euler's Formula
For connected planar graph:
$$ n - e + f = 2 $$
For disconnected ($k$ components):
$$ n - e + f = k + 1 $$

### 2. Sum of Region Degrees
$$ \sum d(R_i) = 2e $$
Har edge 2 regions mein count hoti hai (ya same region mein 2 baar).

### 3. Edge Inequalities (Necessary Conditions)
Agar ye fail hui to graph **Non-Planar** hai.
1. **General Graph**:
   $$ e \le 3n - 6 $$
2. **Triangle-Free Graph (No 3-cycle)**:
   $$ e \le 2n - 4 $$
   (Example: Bipartite graphs, $K_{3,3}$).

### 4. Minimum Degree
 Planar graph mein minimum degree $\delta(G) \le 5$.
 (Always average degree $< 6$).

---

## Relevant PYQs

### GATE CSE 2014
**Q:** 10 vertices, each face has 3 edges. Find $e$.
**Sol:**
$3f = 2e \implies f = 2e/3$.
$10 - e + 2e/3 = 2 \implies e = 24$.

### Kuratowski's Theorem
A graph is non-planar if and only if it contains a subgraph homeomorphic to $K_5$ or $K_{3,3}$.
