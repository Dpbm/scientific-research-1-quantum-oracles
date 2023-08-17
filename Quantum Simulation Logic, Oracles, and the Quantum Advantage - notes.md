## Classical Turing machines
* keep track of probabilities for each possible configuration of the machine
* classically it only needs to keep track the actual configuration
* the probabilities for each state are additive

## Quantum Turing machines
* we need to keep track probabilities and phases
* because of that we need to keep track more information than classical turing machines


## Classical Oracles
* A machine that computes f(x) at unit cost (counted as just one step)
* to be uncomputable, you have to provide a query x and a bit b that will carry the answer from the oracle (the answer is added to that bit modulo two)
* the query registers remain unchanged all the time
* there are some ways to think about it. We could think an oracle as a black box, which we just can see the inputs and the outputs. There's also the grey box, where you can see some part of the internal system/function/running machine, but not the whole thing. Finally, the white box, which is the most permissive one, in the white box you can see everything, inputs, outputs, the whole function and you also have access for where is it running.

## query complexity
* how many times is needed to call the oracle
* each call is counted as one operation

## preparation 
* measurement of an unknown state followed by an unitary transformation that depends on the measurement outcome

---

$HXH = Z$ 

---

## Quantum oracle
* is a quantum version of the classical oracle that implements a reversible logical function into it using a computational basis.
* It needs to be reversible in all possible ways, since its ancillas as its relative phases
* the most powerful thing about quantum oracles are the phases. In contrast with the classical oracle, using the phase is possible to carry much more information and, consequently, can give us a speed up
* In most part of the algorithms, just doing a quantum circuit by itself could be extremely hard and, in some cases, give wrong results
* the construction of different functions in an oracle modifies the phase behavior

