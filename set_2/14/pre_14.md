# Instructions for Question 14

## Question
Draw a DFA for the language accepting strings ending with ‘abba’ over input alphabets $\Sigma = \{a, b\}$

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0` to `q4`.
   - Set `q0` as **Initial**.
   - Set `q4` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `a` (First 'a')
   - `q0` -> `q0`: `b` (Reset)
   - `q1` -> `q2`: `b` (First 'b')
   - `q1` -> `q1`: `a` (Stay on 'a')
   - `q2` -> `q3`: `b` (Second 'b')
   - `q2` -> `q1`: `a` (Back to 'a')
   - `q3` -> `q4`: `a` (Second 'a' - Accept)
   - `q3` -> `q0`: `b` (Reset)
   - `q4` -> `q1`: `a` (Overlap 'a')
   - `q4` -> `q2`: `b` (Overlap 'ab')
5. **Verify**:
   - Test with `abba` (Accept), `aabba` (Accept), `babba` (Accept).
   - Test with `abb` (Reject), `aba` (Reject), `abbab` (Reject).
6. **Save**:
   - Save as `14.jff` in `set_2/14`.
