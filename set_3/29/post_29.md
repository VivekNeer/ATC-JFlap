# Solution for Question 29

## Question
Design a Turing machine to accept a palindrome consisting of a’s and b’s of any length.

## Description
The TM matches the first character with the last character, erasing both. It repeats this process until the string is empty or has one character left.

- **States**:
  - `q0`: Start. Reads first char.
  - `q1`: Moves right to find end (after reading 'a').
  - `q2`: Checks last char (expecting 'a').
  - `q3`: Returns to start (moving left).
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
| `aba` | **Accept** | Palindrome. |
| `abba` | **Accept** | Palindrome. |
| `a` | **Accept** | Single char is palindrome. |
| `ab` | **Reject** | Ends don't match. |
| `abb` | **Reject** | Ends don't match. |
