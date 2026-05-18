# Finite Automata (FA) Short Notes

**Tags:** #gate #toc #automata #dfa #short

## Basics
- **FA** ek acceptor/recognizer hai. String $W$ ko process karta hai, agar string $L$ mein valid hai toh **final state** pe halt karta hai, warna **non-final state** pe.
- FA humesha halt karta hai.
- **Components:** $FA = (Q, \Sigma, \delta, q_0, F)$
- FA ke 2 types hote hain: **DFA** aur **NFA** (with or without $\epsilon$ moves).
- DFA aur NFA dono ki power **equivalent** hoti hai.

## DFA (Deterministic Finite Automata)
- **Transition Function:** $\delta: Q \times \Sigma \to Q$
- Har state se, har input symbol ke liye exactly ek transition hota hai.
- Agar DFA ki saari states final hain $\rightarrow L = \Sigma^*$
- Agar DFA ki saari states non-final hain $\rightarrow L = \emptyset$ (Empty set)
- **Dead State:** Aisi state jahan se final state tak jaane ka koi rasta nahi hota.
- Kisi bhi regular language ke liye ek unique **minimal DFA** hota hai.

## Common DFA Patterns
1. **Starts with 'x':** Initial state se 'x' pe final state mein jayenge, doosre inputs dead state mein jayenge.
2. **Ends with 'x':** State transition is tarah hoga ki last read symbol 'x' hone pe machine final state mein ho.
3. **Contains 'x':** Ek baar 'x' read kar liya toh hamesha final state mein rahega (Self-loop in final state).
4. **Length = n:** $n+1$ states hongi linear sequence mein, baaki dead state mein.
5. **Even number of 'x':** 2 states (even and odd). Even state will be final. Toggle on 'x', self-loop on other inputs.


---
### Extracted Diagrams
![[extracted_img_1_X11.png]]
![[extracted_img_2_X14.png]]
![[extracted_img_3_X18.png]]
![[extracted_img_4_X22.png]]
![[extracted_img_5_X27.png]]
![[extracted_img_6_X29.png]]
![[extracted_img_7_X33.png]]
![[extracted_img_8_X35.png]]
![[extracted_img_9_X39.png]]
![[extracted_img_10_X41.png]]

## Relevant PYQs

### GATE CSE 2011 | Question: 8
[Discussion Link](https://gateoverflow.in/2110/gate-cse-2011-question-8)

<p>Which of the following pairs have <strong>DIFFERENT </strong>expressive power?</p>
<ol style="list-style-type: upper-alpha;">
<li>Deterministic finite automata (DFA) and Non-deterministic finite automata (NFA)</li>
<li>Deterministic push down automata (DPDA) and Non-deterministic push down automata (NPDA)</li>
<li>Deterministic single tape Turing machine and Non-deterministic single tape Turing machine</li>
<li>Single tape Turing machine and multi-tape Turing machine</li>
</ol>

---

### GATE IT 2008 | Question: 6
[Discussion Link](https://gateoverflow.in/3266/gate-it-2008-question-6)

<p>Let $N$ be an NFA with $n$ states and let $M$ be the minimized DFA with m states recogniz­ing the same language. Which of the following in NECESSARILY true?</p>
<ol style="list-style-type:upper-alpha">
<li>$m \leq 2^n$</li>
<li>$n \leq m$</li>
<li>$M$ has one accept state</li>
<li>$m = 2^n$</li>
</ol>

---

### GATE CSE 2018 | Question: 6
[Discussion Link](https://gateoverflow.in/204080/gate-cse-2018-question-6)

<p>Let $N$ be an NFA with $n$ states. Let $k$ be the number of states of a minimal DFA which is equivalent to $N$. Which one of the following is necessarily true?</p>
<ol style="list-style-type:upper-alpha">
<li>$k \geq 2^n$</li>
<li>$k \geq n$</li>
<li>$k \leq n^2$</li>
<li>$k \leq 2^n$</li>
</ol>

---

### GATE CSE 2013 | Question: 41
[Discussion Link](https://gateoverflow.in/1553/gate-cse-2013-question-41)

<p>Which of the following is/are undecidable?</p>
<ol>
<li>$G$ is a CFG. Is $L(G) = \phi$?</li>
<li>$G$ is a CFG. Is $L(G) = \Sigma^*$?</li>
<li>$M$ is a Turing machine. Is $L(M)$ regular?</li>
<li>$A$ is a DFA and $N$ is an NFA. Is $L(A) = L(N)$?</li>
</ol>
<ol style="list-style-type:upper-alpha">
<li>$3$ only      </li>
<li>$3$ and $4$ only      </li>
<li>$1, 2$ and $3$ only      </li>
<li>$2$ and $3$ only</li>
</ol>

---

### GATE CSE 2009 | Question: 16, ISRO2017-12
[Discussion Link](https://gateoverflow.in/1308/gate-cse-2009-question-16-isro2017-12)

<p>Which one of the following is FALSE?</p>
<ol style="list-style-type:upper-alpha">
<li>
<p>There is a unique minimal DFA for every regular language</p>
</li>
<li>
<p>Every NFA can be converted to an equivalent PDA.</p>
</li>
<li>
<p>Complement of every context-free language is recursive.</p>
</li>
<li>
<p>Every nondeterministic PDA can be converted to an equivalent deterministic PDA.</p>
</li>
</ol>

---
