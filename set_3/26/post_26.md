# Solution for Question 26

## Question
Construct a Turing Machine to accept the language $L=\{ w |w \in (0+1)^* \}$ Containing the substring 001.

## Description
The TM scans the tape from left to right looking for the sequence '001'. Once found, it enters a final state and halts (or loops in final state).

- **States**:
  - `q0`: Start. No part of '001' matched.
  - `q1`: Matched '0'.
  - `q2`: Matched '00'.
  - `q3`: Matched '001' (Final).

## Transitions
- $\delta(q0, 1) = (q0, 1, R)$
- $\delta(q0, 0) = (q1, 0, R)$
- $\delta(q1, 1) = (q0, 1, R)$
- $\delta(q1, 0) = (q2, 0, R)$
- $\delta(q2, 0) = (q2, 0, R)$
- $\delta(q2, 1) = (q3, 1, R)$
- $\delta(q3, 0/1) = (q3, 0/1, R)$

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `001` | **Accept** | Contains 001. |
| `1001` | **Accept** | Contains 001. |
| `0001` | **Accept** | Contains 001. |
| `01` | **Reject** | No 001. |
| `00` | **Reject** | Incomplete. |
