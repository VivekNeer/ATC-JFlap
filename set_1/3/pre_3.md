# Instructions for Question 3

## Question
Draw a DFA for the language accepting strings ending with ‘0011’ over input alphabets $\Sigma = \{0, 1\}$

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0` to `q4`.
   - Set `q0` as **Initial**.
   - Set `q4` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `0` (First '0')
   - `q0` -> `q0`: `1` (Reset)
   - `q1` -> `q2`: `0` (Second '0')
   - `q1` -> `q0`: `1` (Reset)
   - `q2` -> `q3`: `1` (First '1')
   - `q2` -> `q2`: `0` (Stay on '00')
   - `q3` -> `q4`: `1` (Second '1' - Accept)
   - `q3` -> `q1`: `0` (Back to '0')
   - `q4` -> `q1`: `0` (Back to '0')
   - `q4` -> `q0`: `1` (Reset)
5. **Verify**:
   - Test with `0011` (Accept), `10011` (Accept), `00011` (Accept).
   - Test with `001` (Reject), `011` (Reject), `00110` (Reject).
6. **Save**:
   - Save as `3.jff` in `set_1/3`.
