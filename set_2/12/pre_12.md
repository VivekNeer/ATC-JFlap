# Instructions for Question 12

## Question
Construct an NFA that accepts the language $\{ab, abc\}^*$. This is the set of strings where ab and abc may be repeated. Example strings include abcab, ababcab, abcabcabc, and the empty string.

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0` to `q4`.
   - Set `q0` as **Initial** and **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `a` (Start of 'ab' or 'abc')
   - `q1` -> `q0`: `b` (Completes 'ab', back to start)
   - `q1` -> `q2`: `b` (Part of 'abc')
   - `q2` -> `q0`: `c` (Completes 'abc', back to start)
5. **Verify**:
   - Test with `ab` (Accept), `abc` (Accept), `abab` (Accept), `abcab` (Accept), `ababc` (Accept).
   - Test with `a` (Reject), `ac` (Reject), `abb` (Reject), `abca` (Reject).
6. **Save**:
   - Save as `12.jff` in `set_2/12`.
