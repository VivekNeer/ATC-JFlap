# Solution for Question 24

## Question
Design a Turing Machine to accept the language $L=\{ 0^n 1^n | n \ge 1 \}$.

## Description
The TM marks '0's with 'X' and corresponding '1's with 'Y'. It zig-zags between the beginning of the 0s and the beginning of the 1s.

- **States**:
  - `q0`: Start. Marks next '0'.
  - `q1`: Moves right to find first '1'.
  - `q2`: Moves left to find last 'X'.
  - `q3`: Checks if any '1's remain after all '0's are marked.
  - `q4`: Final state (Accept).

## Transitions
- $\delta(q0, 0) = (q1, X, R)$
- $\delta(q1, 1) = (q2, Y, L)$
- ... (See JFLAP file for full set)

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `01` | **Accept** | 1 zero, 1 one. |
| `0011` | **Accept** | 2 zeros, 2 ones. |
| `001` | **Reject** | More zeros. |
| `011` | **Reject** | More ones. |
