# Graph Theory Basics

## 1. Introduction
Graph Theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects.

**Definitions:**
- **Vertex (Point/Join):** Represents an object or node. Denoted by $V$.
- **Edge (Line/Branch):** Represents a connection between two vertices. Denoted by $E$.
- **Graph ($G$):** A graph is defined as an ordered pair $G = (V, E)$, where $V$ is a set of vertices and $E$ is a set of edges. 
    - Each edge is associated with an unordered pair of vertices $\{u, v\}$.

---

## 2. Degree of a Vertex
The **degree** (or **valency**) of a vertex $v$, denoted as $d(v)$, is the number of edge ends connecting to it.
- **Unofficial definition:** Number of "welding points" at a vertex.

**Example:**
Consider a graph with vertices $V = \{v_1, v_2, v_3\}$ and edges $E = \{e_1, e_2\}$ where $v_2$ is connected to $v_1$ and $v_3$.
- $d(v_1) = 1$
- $d(v_2) = 2$
- $d(v_3) = 1$

Sum of degrees: $1 + 2 + 1 = 4$.
Number of edges ($|E|$) = 2.
Notice that $4 = 2 \times 2$.

### Handshaking Lemma (First Theorem of Graph Theory)
The sum of degrees of all vertices in a graph is equal to twice the number of edges.
$$ \sum_{i=1}^{n} d(v_i) = 2|E| $$
**Consequence:** The sum of degrees is always **even**.

### Theorem 2: Odd Degree Vertices
Since $\sum d(v_i)$ is always even:
$$ \sum d_{odd} + \sum d_{even} = \text{Even} $$
Since the sum of even degrees is obviously even, the sum of odd degrees must also be even. This is only possible if the **number of odd-degree vertices is even**.

---

## 3. Simple Graph
A **Simple Graph** is a graph that has:
1.  **No self-loops** (an edge connecting a vertex to itself).
2.  **No parallel/multiple edges** (multiple edges between the same pair of vertices).

### Properties of Simple Graphs

**1. Maximum Degree:**
In a simple graph with $n$ vertices, a vertex can be connected to at most all other $n-1$ vertices.
$$ \Delta(G) \le n-1 $$

**2. Maximum Number of Edges:**
Since the maximum degree is $n-1$, if we sum the max degrees: $\sum d(v_i) = n(n-1)$.
Using the Handshaking Lemma $2|E| = \sum d(v_i)$:
$$ 2|E|_{max} = n(n-1) $$
$$ |E|_{max} = \frac{n(n-1)}{2} $$
This is equivalent to choosing 2 vertices out of $n$ to form an edge: $\binom{n}{2}$.

**3. Average Degree:**
$$ \text{Avg Degree} = \frac{\sum d(v_i)}{n} = \frac{2|E|}{n} $$

**4. Degree Inequalities (Theorem 5):**
$$ \delta(G) \le \frac{2|E|}{n} \le \Delta(G) \le n-1 $$
Where $\delta(G)$ is the minimum degree and $\Delta(G)$ is the maximum degree.

---

## 4. Degree Sequence
 A **degree sequence** is the list of degrees of all vertices in the graph, usually written in non-increasing or non-decreasing order.
 
 **Graphical Sequence:** A sequence of numbers is called *graphical* if there exists a simple graph with that degree sequence.

### Havel-Hakimi Algorithm
A procedure to determine if a sequence is graphical.
**Steps:**
1.  Sort the sequence in descending order.
2.  Remove the first element, say $k$.
3.  Subtract 1 from the next $k$ elements in the sequence.
4.  If negative numbers appear, it's not graphical.
5.  If we reach all zeros, it is graphical.
6.  Sort again and repeat.

**Example from notes:**
Sequence: `7, 6, 5, 4, 4, 3, 2, 1`
1. Remove 7. Subtract 1 from next 7 elements:
   `5, 4, 3, 3, 2, 1, 0`
2. Remove 5. Subtract 1 from next 5 elements:
   `3, 2, 2, 1, 0, 0` (and `0` at end)
3. Remove 3. Subtract 1 from next 3 elements:
   `1, 1, 0, 0, 0, 0`
4. Remove 1. Subtract 1 from next 1 element:
   `0, 0, 0, 0, 0`
   
**Result:** All zeros -> The sequence is **Graphical**.

---

## 5. Counting Graphs
Total number of possible simple graphs with $n$ vertices.
Since the maximum number of edges is $N = \frac{n(n-1)}{2}$, and each edge has 2 possibilities (exists or doesn't exist):
$$ \text{Total Simple Graphs} = 2^{N} = 2^{\frac{n(n-1)}{2}} $$

*(Note provided example: $2^6$ likely refers to a case where max edges = 6, i.e., n=4)*
---

## 6. Special Types of Graphs

### 6.1 Complete Graph ($K_n$)
A simple graph where every pair of distinct vertices is connected by a unique edge.
- **Degree:** Every vertex has degree $n-1$.
- **Number of Edges:** Since every vertex connects to every other:
  $$ |E| = \binom{n}{2} = \frac{n(n-1)}{2} $$

### 6.2 Regular Graph
A graph where every vertex has the same degree $k$. Such a graph is called **$k$-regular**.
- **Properties:**
  - $\delta(G) = \Delta(G) = k$
  - From Handshaking Lemma: $n \times k = 2|E| \implies |E| = \frac{nk}{2}$
- **Examples:**
  - $K_n$ is $(n-1)$-regular.
  - Cycle graph $C_n$ is 2-regular.
  - Null graph $N_n$ is 0-regular.

### 6.3 Cycle Graph ($C_n$)
A graph with $n$ vertices ($n \ge 3$) containing a single cycle through all vertices.
- **Structure:** Closed loop.
- **Regularity:** It is always 2-regular.
- **Edges:** Number of edges = Number of vertices = $n$.

### 6.4 Wheel Graph ($W_n$)
Constructed by taking a Cycle Graph $C_{n-1}$ and adding a new vertex (Hub) connected to all vertices of the cycle.
- **Vertices:** $n$ (where $n-1$ are on the rim, 1 is center). note: $n \ge 4$.
- **Edges:** 
  - Rim edges ($C_{n-1}$): $n-1$
  - Spoke edges (Hub to Rim): $n-1$
  - Total Edges: $2(n-1)$
- **Degrees:**
  - Degree of Hub: $n-1$
  - Degree of Rim vertices: 3

### 6.5 Bipartite Graph
A graph where the vertex set $V$ can be partitioned into two disjoint sets $V_1$ and $V_2$ such that every edge connects a vertex in $V_1$ to one in $V_2$.
- **No Internal Edges:** No edge connects two vertices within the same set ($V_1$ or $V_2$).
- **Theorem:** A graph is bipartite if and only if it contains **no odd length cycles**.
- **Complete Bipartite Graph ($K_{m,n}$):**
  - Every vertex in $V_1$ (size $m$) is connected to every vertex in $V_2$ (size $n$).
  - Total Vertices: $m+n$
  - Total Edges: $m \times n$

### 6.6 Hypercube Graph ($Q_n$)
Also known as an $n$-cube.
- **Vertices:** $2^n$ vertices, each labeled with a distinct $n$-bit binary string.
- **Edges:** Two vertices are connected if their binary strings differ by exactly one bit.
- **Properties:**
  - **Regularity:** It is $n$-regular (each vertex has $n$ neighbors).
  - **Edges:** using Handshaking Lemma: $2|E| = V \times \text{degree} = 2^n \times n \implies |E| = n 2^{n-1}$.
  - **Bipartite:** All hypercubes are bipartite graphs.

### 6.7 Complement Graph ($\bar{G}$)
The complement of a graph $G$ has the same vertex set as $G$. Two vertices are adjacent in $\bar{G}$ if and only if they are **not** adjacent in $G$.
- **Union:** $G \cup \bar{G} = K_n$ (Complete Graph).
- **Edges:** $|E(G)| + |E(\bar{G})| = \frac{n(n-1)}{2}$.

### 6.8 Self-Complement Graph
A graph that is isomorphic to its own complement ($G \cong \bar{G}$).
- **Edge Count:**
  $$ |E(G)| = |E(\bar{G})| \implies 2|E| = \frac{n(n-1)}{2} \implies |E| = \frac{n(n-1)}{4} $$
- **Existence Condition:** For a self-complement graph to exist, the number of vertices $n$ must satisfy $n \equiv 0 \pmod 4$ or $n \equiv 1 \pmod 4$.

### 6.9 Line Graph $L(G)$
The line graph $L(G)$ of a graph $G$ is a graph where:
- Each vertex of $L(G)$ represents an edge of $G$.
- Two vertices of $L(G)$ are adjacent if their corresponding edges in $G$ share a common endpoint (are incident).
