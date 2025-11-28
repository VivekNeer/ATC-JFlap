# Solution for Question 1

## Question
Design a non deterministic PDA for accepting the language $L = \{a^n b^n | n \ge 1\}$

## Description
The PDA works by pushing 'a's onto the stack. When the first 'b' is encountered, it switches state and begins popping 'a's for each 'b'. If the stack is empty (only bottom marker Z remains) after processing all input, the string is accepted.

- **States**:
  - `q0`: Start state. Transitions to `q1` on first 'a'.
  - `q1`: Pushes 'a's.
  - `q2`: Pops 'a's on 'b's.
  - `q3`: Final state (Accept).

## Transitions
- $\delta(q0, a, Z) = \{(q1, aZ)\}$
- $\delta(q1, a, a) = \{(q1, aa)\}$
- $\delta(q1, b, a) = \{(q2, \lambda)\}$
- $\delta(q2, b, a) = \{(q2, \lambda)\}$
- $\delta(q2, \lambda, Z) = \{(q3, Z)\}$

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `ab` | **Accept** | 1 'a', 1 'b'. Stack matches. |
| `aabb` | **Accept** | 2 'a's, 2 'b's. |
| `aaabbb` | **Accept** | 3 'a's, 3 'b's. |
| `a` | **Reject** | Missing 'b'. |
| `b` | **Reject** | Missing 'a'. |
| `aabbb` | **Reject** | More 'b's than 'a's. |
| `aaabb` | **Reject** | More 'a's than 'b's. |
