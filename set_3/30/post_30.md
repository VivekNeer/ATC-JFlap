# Solution for Question 30

## Question
Construct a TM to accept the language $L=\{ww^R |w \in (a+b)^*\}$

## Description
This language represents even-length palindromes. The TM matches the first and last characters, erasing them, and repeats. It rejects odd-length strings (unlike the general palindrome TM which accepts the last single character).

- **States**:
  - `q0`: Start. Reads first char.
  - `q1`: Moves right to find end (after reading 'a').
  - `q2`: Checks last char (expecting 'a').
  - `q3`: Returns to start.
  - `q4`: Moves right to find end (after reading 'b').
  - `q5`: Checks last char (expecting 'b').
  - `q6`: Final state (Accept).

## Transitions
- $\delta(q0, a) = (q1, \square, R)$
- $\delta(q0, b) = (q4, \square, R)$
- $\delta(q0, \square) = (q6, \square, S)$
- ... (See JFLAP file for full set)

## Test Strings
| String | Result | Explanation |
| :--- | :--- | :--- |
| `abba` | **Accept** | $w=ab, w^R=ba$. |
| `aaaa` | **Accept** | $w=aa, w^R=aa$. |
| `aba` | **Reject** | Odd length. |
| `ab` | **Reject** | Not a palindrome. |
