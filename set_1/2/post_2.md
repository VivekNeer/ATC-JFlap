# Solution for Question 2

## Question
Construct a DFA for $L = \{ab^n a^m : n \ge 2, m \ge 3\}$

## Description
The DFA accepts strings starting with a single 'a', followed by at least two 'b's, and ending with at least three 'a's.

- **States**:
  - `q0`: Start. Expects 'a'.
  - `q1`: Expects first 'b'.
  - `q2`: Expects second 'b'.
  - `q3`: Satisfied $n \ge 2$. Loops on 'b'. Expects first 'a' of suffix.
  - `q4`: Expects second 'a'.
  - `q5`: Expects third 'a'.
  - `q6`: Final state. Satisfied $m \ge 3$. Loops on 'a'.

## Transitions
- $\delta(q0, a) = q1$
- $\delta(q1, b) = q2$
- $\delta(q2, b) = q3$
- $\delta(q3, b) = q3$
- $\delta(q3, a) = q4$
- $\delta(q4, a) = q5$
- $\delta(q5, a) = q6$
- $\delta(q6, a) = q6$

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `abbaaa` | **Accept** | Min requirement: 1 a, 2 b's, 3 a's. |
| `abbbaaa` | **Accept** | 3 b's ($n=3$), 3 a's. |
| `abbaaaa` | **Accept** | 2 b's, 4 a's ($m=4$). |
| `abaaa` | **Reject** | Only 1 b ($n=1 < 2$). |
| `abbaa` | **Reject** | Only 2 a's ($m=2 < 3$). |
| `bbaaa` | **Reject** | Starts with b. |
| `abbaaba` | **Reject** | 'b' after 'a's. |
