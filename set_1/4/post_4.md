# Solution for Question 4

## Question
Construct npda’s that accept the following languages on $\Sigma = \{a, b, c\}$.
$L = \{a^n b^m c^{n+m} : n \ge 0, m \ge 0\}$

## Description
The PDA pushes 'a's and then 'b's onto the stack. For every 'c' encountered, it pops one symbol from the stack. Since 'b's are pushed after 'a's, they are popped first. The total number of 'c's must equal the total number of 'a's and 'b's combined.

- **States**:
  - `q0`: Start. Handles empty string or transitions to pushing states.
  - `q1`: Pushes 'a's.
  - `q2`: Pushes 'b's.
  - `q3`: Pops symbols ('b's then 'a's) for each 'c'.
  - `q4`: Final state.

## Transitions
- $\delta(q0, \lambda, Z) = \{(q4, Z)\}$ (Accept $\epsilon$)
- $\delta(q0, a, Z) = \{(q1, aZ)\}$
- $\delta(q0, b, Z) = \{(q2, bZ)\}$
- $\delta(q1, a, a) = \{(q1, aa)\}$
- $\delta(q1, b, a) = \{(q2, ba)\}$
- $\delta(q1, c, a) = \{(q3, \lambda)\}$
- $\delta(q2, b, b) = \{(q2, bb)\}$
- $\delta(q2, c, b) = \{(q3, \lambda)\}$
- $\delta(q3, c, b) = \{(q3, \lambda)\}$
- $\delta(q3, c, a) = \{(q3, \lambda)\}$
- $\delta(q3, \lambda, Z) = \{(q4, Z)\}$

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `abc` | **Accept** | 1 a + 1 b = 2 c's. |
| `aabbcc` | **Accept** | 2 a + 2 b = 4 c's. |
| `ac` | **Accept** | 1 a + 0 b = 1 c. |
| `bc` | **Accept** | 0 a + 1 b = 1 c. |
| `ab` | **Reject** | Missing c's. |
| `aabc` | **Reject** | 2 a + 1 b != 1 c. |
| `abcc` | **Reject** | 1 a + 1 b != 2 c's. |
