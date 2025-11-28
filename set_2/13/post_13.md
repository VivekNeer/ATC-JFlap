# Solution for Question 13

## Question
Draw a DFA for the language accepting strings ending with ‘abb’ over input alphabets $\Sigma = \{a, b\}$

## Description
The DFA tracks the suffix 'abb'.

- **States**:
  - `q0`: Start. No prefix matched.
  - `q1`: Matched 'a'.
  - `q2`: Matched 'ab'.
  - `q3`: Matched 'abb' (Final).

## Transitions
| State | Input a | Input b |
| :--- | :--- | :--- |
| **q0** | q1 | q0 |
| **q1** | q1 | q2 |
| **q2** | q1 | q3 |
| **q3** | q1 | q0 |

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `abb` | **Accept** | Ends with abb. |
| `aabb` | **Accept** | Ends with abb. |
| `babb` | **Accept** | Ends with abb. |
| `ab` | **Reject** | Incomplete suffix. |
| `abba` | **Reject** | Ends with a. |
| `abbb` | **Reject** | Ends with bbb. |
