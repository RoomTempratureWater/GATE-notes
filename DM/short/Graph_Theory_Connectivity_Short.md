#gate #dm #short #graphs #connectivity

# Graph Theory - Connectivity (Short Notes)

**Date:** 29/01/2026

## 1. Quick Definitions
- **Walk:** Vertices & Edges CAN repeat. (Bas ghumna hai).
- **Trail:** Vertices YES, Edges **NO** repeat.
- **Path:** Vertices **NO**, Edges **NO** repeat.

## 2. Connectedness
- **Connected:** Path exists between every pair.
- **Component:** Maximal connected subgraph.
- **S1 (False):** $G$ connected $\implies \bar{G}$ connected. (Ex: $\bar{C_4}$ is disconnected).
- **S2 (True):** $G$ disconnected $\implies \bar{G}$ **Connected**.

## 3. Important Theorems
1.  **Min Degree:** If $\delta(G) \ge \frac{n-1}{2} \implies$ Connected.
2.  **Odd Vertices:** If exactly 2 odd degree vertices exist $\implies$ Path exists between them (Same component).

## 4. Edge Ranges
| Graph Type | Min Edges | Max Edges |
| :--- | :--- | :--- |
| **Connected** | $n-1$ (Tree) | $\binom{n}{2}$ ($K_n$) |
| **Disconnected ($k$ comp)** | $n-k$ | $\frac{(n-k)(n-k+1)}{2}$ |

## 5. Cuts & Connectivity
- **Cut Edge (Bridge):** Removal $\to$ Disconnected. (Must NOT be in a cycle).
- **Cut Vertex (Articulation):** Removal $\to$ Disconnected.
- **Inequality Order:**
  $$ \kappa \le \lambda \le \delta \le \text{Avg} \le \Delta \le n-1 $$
  (Vertex Conn $\le$ Edge Conn $\le$ Min Degree)

## 6. Problem Trick: Complement of Join
Question: $(C_3 + W_4)'$ components?
- **Concept:** $\overline{A + B} = \bar{A} \cup \bar{B}$ (Disjoint Union).
- $\bar{C_3}$ ($K_3'$) $\to$ 3 isolated vertices ($\implies$ 3 comp).
- $\bar{W_4}$ ($C_4' \cup K_1'$) $\to 2K_2 \cup K_1$ ($\implies$ 2 + 1 = 3 comp).
- **Total:** $3 + 3 = 6$ Components.


---
## Relevant PYQs (Connectivity)

### GATE1992-04-b
[Discussion Link](https://gateoverflow.in/17407/gate1992-04-b)

A priority encoder accepts three input signals $\text{(A, B and C)}$ and produces a two-bit output $(X_1, X_0 )$ corresponding to the highest priority active input signal. Assume $A$ has the highest priority followed by $B$ and $C$ has the lowest priority. If none of the inputs are active the output should be $00$, design the priority encoder using $4:1$ multiplexers as the main components.

---

### GATE IT 2008 | Question: 85
[Discussion Link](https://gateoverflow.in/3409/gate-it-2008-question-85)

<p>Host $X$ has $IP$ address $192.168.1.97$ and is connected through two routers $R1$ and $R2$ to an­other host $Y$ with $IP$ address $192.168.1.80$. Router $R1$ has $IP$ addresses $192.168.1.135$ and $192.168.1.110$. $R2$ has $IP$ addresses $192.168.1.67$ and $192.168.1.155$. The netmask used in the network is $255.255.255.224$.</p>
<p>Which $IP$ address should $X$ configure its gateway as?</p>
<ol style="list-style-type:upper-alpha">
<li>$192.168.1.67$</li>
<li>$192.168.1.110$</li>
<li>$192.168.1.135$</li>
<li>$192.168.1.155$</li>
</ol>

---

### GATE IT 2008 | Question: 84
[Discussion Link](https://gateoverflow.in/3408/gate-it-2008-question-84)

<p>Host $X$ has IP address $192.168.1.97$ and is connected through two routers $R1$ and $R2$ to an­other host $Y$ with IP address $192.168.1.80$. Router $R1$ has IP addresses $192.168.1.135$ and $192.168.1.110$. $R2$ has IP addresses $192.168.1.67$ and $192.168.1.155$. The netmask used in the network is $255.255.255.224$.</p>
<p>Given the information above, how many distinct subnets are guaranteed to already exist in the network?</p>
<ol style="list-style-type:upper-alpha">
<li>$1$</li>
<li>$2$</li>
<li>$3$</li>
<li>$6$</li>
</ol>

---

### GATE IT 2007 | Question: 63
[Discussion Link](https://gateoverflow.in/3508/gate-it-2007-question-63)

<p>A group of $15$ routers is interconnected in a centralized complete binary tree with a router at each tree node. Router $i$ communicates with router $j$ by sending a message to the root of the tree. The root then sends the message back down to router $j$. The mean number of hops per message, assuming all possible router pairs are equally likely is</p>
<ol style="list-style-type:upper-alpha">
<li>$3$</li>
<li>$4.26$</li>
<li>$4.53$</li>
<li>$5.26$</li>
</ol>

---

### GATE IT 2007 | Question: 45
[Discussion Link](https://gateoverflow.in/3480/gate-it-2007-question-45)

<p>The line $T$ in the following figure is permanently connected to the ground.</p>
<p style="text-align:center"><img alt="" src="https://gateoverflow.in/?qa=blob&amp;qa_blobid=4503860270348278811"/></p>
<p>Which of the following inputs $(X_1 X_2 X_3 X_4)$ will detect the fault ?</p>
<ol style="list-style-type:upper-alpha">
<li>$0000$</li>
<li>$0111$</li>
<li>$1111$</li>
<li>None of these</li>
</ol>

---
