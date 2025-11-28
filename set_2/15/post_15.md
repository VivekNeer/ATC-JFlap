# Solution for Question 15

## Question
Draw a deterministic and non-deterministic finite automata which accept a string containing “the” anywhere in a string of {a-z}.

## Description
The DFA looks for the substring "the". Once found, it enters a final state and stays there.

- **States**:
  - `q0`: Start. No part of "the" matched.
  - `q1`: Matched 't'.
  - `q2`: Matched 'th'.
  - `q3`: Matched "the" (Final).

## Transitions
| State | Input t | Input h | Input e | Other [a-z] |
| :--- | :--- | :--- | :--- | :--- |
| **q0** | q1 | q0 | q0 | q0 |
| **q1** | q1 | q2 | q0 | q0 |
| **q2** | q1 | q0 | q3 | q0 |
| **q3** | q3 | q3 | q3 | q3 |

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `there` | **Accept** | Contains "the". |
| `breathe` | **Accept** | Contains "the". |
| `the` | **Accept** | Is "the". |
| `those` | **Reject** | "tho", not "the". |
| `teh` | **Reject** | "teh", not "the". |
| `th` | **Reject** | Incomplete. |
