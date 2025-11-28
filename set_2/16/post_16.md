# Solution for Question 16

## Question
Draw a deterministic and non-deterministic finite automata which accept a string containing “ing” at the end of a string in a string of {a-z}.

## Description
The DFA tracks the suffix "ing". It is similar to seeking a substring, but if any character follows "ing", it must reset or partially reset to ensure "ing" is the *very last* thing.

- **States**:
  - `q0`: Start. No prefix matched.
  - `q1`: Matched 'i'.
  - `q2`: Matched 'in'.
  - `q3`: Matched "ing" (Final).

## Transitions
| State | Input i | Input n | Input g | Other [a-z] |
| :--- | :--- | :--- | :--- | :--- |
| **q0** | q1 | q0 | q0 | q0 |
| **q1** | q1 | q2 | q0 | q0 |
| **q2** | q1 | q0 | q3 | q0 |
| **q3** | q1 | q0 | q0 | q0 |

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `anything` | **Accept** | Ends with "ing". |
| `sing` | **Accept** | Ends with "ing". |
| `going` | **Accept** | Ends with "ing". |
| `anywhere` | **Reject** | Ends with "ere". |
| `singer` | **Reject** | Ends with "er". |
| `in` | **Reject** | Incomplete. |
