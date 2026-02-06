#gate #dm #short #graphs

# Adjacency Matrix (Short Notes)

**Link to Long Notes:** [[Graph_Theory_Adjacency_Matrix]]

## Basics
- **Adjacency Matrix $A$**: $n \times n$ matrix. $A_{ij} = 1$ agar edge hai $i$ aur $j$ ke beech, else $0$ (for simple unweighted graphs).
- **Symmetric**: Undirected graphs ke liye $A$ symmetric hota hai ($A_{ij} = A_{ji}$).
- **Principal Diagonal**: All $0$s agar self-loops nahi hain.

## Properties (Important for GATE)

1. **Degree Calculation**:
   - Row ya Column ka sum $=$ Vertex ki degree.
   - $\sum A_{ij} = \text{deg}(v_i)$.

2. **Powers of Matrix ($A^k$)**:
   - $(A^k)_{ij} =$ Number of walks of length $k$ from $i$ to $j$.
   - **$A^2$ (Square)**:
     - Diagonal entry $(A^2)_{ii} =$ Degree of vertex $i$.
     - $\text{Trace}(A^2) = 2 \times |E|$ (Sum of degrees).
   - **$A^3$ (Cube)**:
     - Diagonal entry $(A^3)_{ii}$ relates to triangles.
     - $\text{Trace}(A^3) = 6 \times (\text{Number of Triangles})$.

3. **Eigenvalues (Spectrum)**:
   - Sum of Eigenvalues ($\sum \lambda_i$) = $0$ (Trace is 0).
   - Sum of Squares ($\sum \lambda_i^2$) = $2 \times |E|$.
   - Sum of Cubes ($\sum \lambda_i^3$) = $6 \times \text{Triangles}$.

## Connectivity & Matrix
- Agar graph Connected hai, toh $(I+A)^{n-1}$ ke saare entries **positive** honge.
- Reasoning: Walks of all lengths up to $n-1$ cover ho jate hain.

## Generating Function Analogy
- Jaise $\frac{1}{1-x} = 1 + x + x^2 + \dots$
- Waise hi $(I-A)^{-1}$ connects to walks of all lengths.
- $(I+A)^{n-1}$ ensures connectivity check efficiently.

---
**Fun Fact (Eigenvalues):**
Think of Matrix as a machine.
- **Eigenvectors** = Arrow directions jo turn nahi hote (sirf stretch/shrink hote hain).
- **Eigenvalues** = Wo stretch/shrink factor.

---
## Relevant PYQs
- **GATE IT 2005**: Matrix properties vs Connectivity.
- **GATE CSE 2022**: Connected components and Eigenvalues.


