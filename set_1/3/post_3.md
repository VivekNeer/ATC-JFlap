# Solution for Question 3

## Question
Draw a DFA for the language accepting strings ending with ‘0011’ over input alphabets $\Sigma = \{0, 1\}$

## Description
The DFA tracks the progress towards the suffix '0011'. Any interruption resets the state to the appropriate prefix match.

- **States**:
  - `q0`: Start. No prefix matched.
  - `q1`: Matched '0'.
  - `q2`: Matched '00'.
  - `q3`: Matched '001'.
  - `q4`: Matched '0011' (Final).

## Transitions
| State | Input 0 | Input 1 |
| :--- | :--- | :--- |
| **q0** | q1 | q0 |
| **q1** | q2 | q0 |
| **q2** | q2 | q3 |
| **q3** | q1 | q4 |
| **q4** | q1 | q0 |

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `0011` | **Accept** | Ends with 0011. |
| `110011` | **Accept** | Ends with 0011. |
| `00011` | **Accept** | Ends with 0011. |
| `001` | **Reject** | Incomplete suffix. |
| `00110` | **Reject** | Ends with 0, not 1. |
| `011` | **Reject** | Missing leading 0s. |
