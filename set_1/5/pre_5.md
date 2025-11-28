# Instructions for Question 5

## Question
Construction of a minimal DFA accepting set of strings over $\{a, b\}$ in which every ‘a’ is never be followed by ‘bb’.

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0`, `q1`, `q2`, `q3`.
   - Set `q0` as **Initial**.
   - Set `q0`, `q1`, `q2` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q0`: `b` (Leading 'b's are fine)
   - `q0` -> `q1`: `a` (Found an 'a', start checking)
   - `q1` -> `q1`: `a` (Another 'a', reset check)
   - `q1` -> `q2`: `b` (Found 'ab', warning)
   - `q2` -> `q1`: `a` (Found 'aba', safe, reset check)
   - `q2` -> `q3`: `b` (Found 'abb', Reject)
   - `q3` -> `q3`: `a` (Trap)
   - `q3` -> `q3`: `b` (Trap)
5. **Verify**:
   - Test with `ab` (Accept), `aba` (Accept), `bba` (Accept), `aab` (Accept).
   - Test with `abb` (Reject), `aabb` (Reject), `babb` (Reject).
6. **Save**:
   - Save as `5.jff` in `set_1/5`.
