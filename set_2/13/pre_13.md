# Instructions for Question 13

## Question
Draw a DFA for the language accepting strings ending with ‘abb’ over input alphabets $\Sigma = \{a, b\}$

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0` to `q3`.
   - Set `q0` as **Initial**.
   - Set `q3` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `a` (First 'a')
   - `q0` -> `q0`: `b` (Reset)
   - `q1` -> `q2`: `b` (First 'b')
   - `q1` -> `q1`: `a` (Stay on 'a')
   - `q2` -> `q3`: `b` (Second 'b' - Accept)
   - `q2` -> `q1`: `a` (Back to 'a')
   - `q3` -> `q0`: `b` (Reset)
   - `q3` -> `q1`: `a` (Back to 'a')
5. **Verify**:
   - Test with `abb` (Accept), `aabb` (Accept), `babb` (Accept).
   - Test with `ab` (Reject), `ba` (Reject), `abba` (Reject).
6. **Save**:
   - Save as `13.jff` in `set_2/13`.
