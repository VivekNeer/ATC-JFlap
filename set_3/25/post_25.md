# Solution for Question 25

## Question
Design a Turing Machine to accept the language $L=\{ 0^n 1^n 2^n | n \ge 1 \}$.

## Description
The TM marks '0' with 'X', finds the first '1' and marks it 'Y', then finds the first '2' and marks it 'Z'. It repeats this cycle.

- **States**:
  - `q0`: Start. Marks next '0'.
  - `q1`: Moves right to find first '1'.
  - `q2`: Moves right to find first '2'.
  - `q3`: Moves left to find last 'X'.
  - `q5`: Checks if any '1's or '2's remain after all '0's are marked.
  - `q6`: Final state (Accept).

## Transitions
- $\delta(q0, 0) = (q1, X, R)$
- $\delta(q1, 1) = (q2, Y, R)$
- $\delta(q2, 2) = (q3, Z, L)$
- ... (See JFLAP file for full set)

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `012` | **Accept** | 1 of each. |
| `001122` | **Accept** | 2 of each. |
| `01` | **Reject** | Missing 2. |
| `0122` | **Reject** | Extra 2. |
