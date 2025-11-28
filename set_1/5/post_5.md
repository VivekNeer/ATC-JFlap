# Solution for Question 5

## Question
Construction of a minimal DFA accepting set of strings over $\{a, b\}$ in which every ‘a’ is never be followed by ‘bb’.

## Description
The DFA rejects any string containing the substring "abb". It accepts all other strings.

- **States**:
  - `q0`: Start. Safe state.
  - `q1`: Just saw 'a'.
  - `q2`: Just saw 'ab'.
  - `q3`: Saw 'abb' (Trap state).

## Transitions
| State | Input a | Input b |
| :--- | :--- | :--- |
| **q0** | q1 | q0 |
| **q1** | q1 | q2 |
| **q2** | q1 | q3 |
| **q3** | q3 | q3 |

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `ab` | **Accept** | 'a' followed by single 'b'. |
| `aba` | **Accept** | 'a' followed by 'b' then 'a'. |
| `bba` | **Accept** | No 'a' before 'bb'. |
| `aab` | **Accept** | 'a' followed by 'a' then 'b'. |
| `abb` | **Reject** | Contains 'abb'. |
| `aabb` | **Reject** | Contains 'abb'. |
| `babb` | **Reject** | Contains 'abb'. |
