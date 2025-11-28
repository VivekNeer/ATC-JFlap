# Solution for Question 14

## Question
Draw a DFA for the language accepting strings ending with ‘abba’ over input alphabets $\Sigma = \{a, b\}$

## Description
The DFA tracks the suffix 'abba'.

- **States**:
  - `q0`: Start. No prefix matched.
  - `q1`: Matched 'a'.
  - `q2`: Matched 'ab'.
  - `q3`: Matched 'abb'.
  - `q4`: Matched 'abba' (Final).

## Transitions
| State | Input a | Input b |
| :--- | :--- | :--- |
| **q0** | q1 | q0 |
| **q1** | q1 | q2 |
| **q2** | q1 | q3 |
| **q3** | q4 | q0 |
| **q4** | q1 | q2 |

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `abba` | **Accept** | Ends with abba. |
| `aabba` | **Accept** | Ends with abba. |
| `babba` | **Accept** | Ends with abba. |
| `abb` | **Reject** | Incomplete suffix. |
| `abbab` | **Reject** | Ends with b. |
| `abbb` | **Reject** | Ends with bbb. |
