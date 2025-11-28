# Solution for Question 12

## Question
Construct an NFA that accepts the language $\{ab, abc\}^*$.

## Description
The NFA accepts strings formed by concatenating 'ab' and 'abc' any number of times. The start state is also the final state to accept the empty string.

- **States**:
  - `q0`: Start/Final state. Ready to process next 'ab' or 'abc'.
  - `q1`: Saw 'a'. Could be start of 'ab' or 'abc'.
  - `q2`: Saw 'ab' (as prefix of 'abc').

## Transitions
- $\delta(q0, a) = \{q1\}$
- $\delta(q1, b) = \{q0, q2\}$ (Nondeterminism here: return to q0 for 'ab', or go to q2 for 'abc')
- $\delta(q2, c) = \{q0\}$

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `ab` | **Accept** | Matches 'ab'. |
| `abc` | **Accept** | Matches 'abc'. |
| `abcab` | **Accept** | Matches 'abc' then 'ab'. |
| `ababc` | **Accept** | Matches 'ab' then 'abc'. |
| `a` | **Reject** | Incomplete. |
| `ac` | **Reject** | Invalid sequence. |
| `abb` | **Reject** | 'ab' followed by 'b' is invalid. |
