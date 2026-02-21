Found 128 relevant questions.


---
## Relevant PYQs

### GATE IT 2008 | Question: 56
[Discussion Link](https://gateoverflow.in/3366/gate-it-2008-question-56)

<p>Match the following flag bits used in the context of virtual memory management on the left side with the different purposes on the right side of the table below.$$\small \begin{array}{ll|ll} \rlap{\textbf{Name of the bit}} &amp;&amp; \rlap{\textbf{Purpose}} \\\hlineá \text{I.}á &amp;\text{Dirty} &amp; \text{a.}&amp; \text{Page initialization} \\<br/>
\text{II.} &amp; \text{R/W} &amp; \text{b.}&amp; \text{Write-back policy} \\á<br/>
\text{III.} &amp;\text{Referenceá } \quad&amp; \text{c.}&amp; \text{Page protection}á \\<br/>
á\text{IV.} &amp;\text{Valid} &amp; \text{d.}&amp; \text{Page replacement policy}á \\á\end{array}$$</p>
<ol style="list-style-type:upper-alpha">
<li>$\text{I-d, II-a, III-b, IV-c}$á</li>
<li>$\text{I-b, II-c, III-a, IV-d}$</li>
<li>$\text{I-c, II-d, III-a, IV-b}$</li>
<li>$\text{I-b, II-c, III-d, IV-a}$</li>
</ol>

---

### GATE IT 2008 | Question: 21
[Discussion Link](https://gateoverflow.in/3282/gate-it-2008-question-21)

<p>Which of the following first order formulae is logically valid? Here $\alpha(x)$ is a first order formula with $x$ as a free variable, and $\beta$ is a first order formula with no free variable.</p>
<ol style="list-style-type:upper-alpha">
<li>$[\beta \rightarrow (\exists x, \alpha(x))] \rightarrow [\forall x, \beta \rightarrow \alpha(x)]$</li>
<li>$[\exists x, \beta \rightarrow \alpha(x)] \rightarrow [\beta \rightarrow (\forall x, \alpha(x))]$</li>
<li>$[(\exists x, \alpha(x)) \rightarrow \beta] \rightarrow [\forall x, \alpha(x) \rightarrow \beta]$</li>
<li>$[(\forall x, \alpha(x)) \rightarrow \beta] \rightarrow [\forall x, \alpha(x) \rightarrow \beta]$</li>
</ol>

---

### GATE IT 2008 | Question: 1
[Discussion Link](https://gateoverflow.in/3222/gate-it-2008-question-1)

<p>A set of Boolean connectives is functionally complete if all Boolean functions can be synthesized using those. Which of the following sets of connectives is NOT functionally complete?</p>
<ol style="list-style-type:upper-alpha">
<li>EX-NOR</li>
<li>implication, negation</li>
<li>OR, negation</li>
<li>NAND</li>
</ol>

---

### GATE IT 2007 | Question: 67
[Discussion Link](https://gateoverflow.in/3512/gate-it-2007-question-67)

<p>Consider the following implications relating to functional and multivalued dependencies given below, which may or may not be correct.</p>
<ol style="list-style-type:lower-roman">
<li>if $A \rightarrow \rightarrow B$ and $A \rightarrow \rightarrow C$ then $A \rightarrow áBC$</li>
<li>if $A \rightarrow B$ and $A \rightarrowá C$ then $A \rightarrow \rightarrow BC$</li>
<li>if $A \rightarrow \rightarrow BC$ and $A \rightarrowá B$ then $A \rightarrow C$</li>
<li>if $A \rightarrow BC$ and $A \rightarrowá B$ then $A \rightarrow \rightarrow C$</li>
</ol>
<p>Exactly how many of the above implications are valid?</p>
<ol style="list-style-type:upper-alpha">
<li>$0$</li>
<li>$1$</li>
<li>$2$</li>
<li>$3$</li>
</ol>

---

### GATE IT 2007 | Question: 32
[Discussion Link](https://gateoverflow.in/3465/gate-it-2007-question-32)

<p>Consider the following C program:á</p>
<pre class="prettyprint lang-c_cpp">  #include &lt;stdio.h&gt;
           #define EOF -1
           void push (int); /* push the argument on the stack */
           int pop  (void); /* pop the top of the stack */
           void flagError ();
           int main ()
          {         int c, m, n, r;
                     while ((c = getchar ()) != EOF)
                    { if  (isdigit (c) )
                               push (c);
                     else if ((c == '+') || (c == '*'))
                    {          m = pop ();
                                n = pop ();
                                r = (c == '+') ? n + m : n*m;
                                push (r);
                      }
                      else if (c != ' ')
                               flagError ();
             }
              printf("% c", pop ());
}</pre>
<p><br/>
What is the output of the program for the following input?<br/>
$5 \ 2 \ * \ 3 \ 3 \ 2 \ + * +$</p>
<ol style="list-style-type:upper-alpha">
<li>$15$</li>
<li>$25$</li>
<li>$30$</li>
<li>$150$</li>
</ol>

---

