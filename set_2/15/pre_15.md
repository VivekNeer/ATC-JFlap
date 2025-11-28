# Instructions for Question 15

## Question
Draw a deterministic and non-deterministic finite automata which accept a string containing “the” anywhere in a string of {a-z}, e.g., “there” but not “those”.

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0` to `q3`.
   - Set `q0` as **Initial**.
   - Set `q3` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `t`
   - `q0` -> `q0`: `[a-z] - {t}` (Any other letter)
   - `q1` -> `q2`: `h`
   - `q1` -> `q1`: `t` (Stay on 't')
   - `q1` -> `q0`: `[a-z] - {t, h}` (Reset)
   - `q2` -> `q3`: `e` (Found "the")
   - `q2` -> `q1`: `t` (Back to 't')
   - `q2` -> `q0`: `[a-z] - {t, e}` (Reset)
   - `q3` -> `q3`: `[a-z]` (Loop forever once found)
5. **Verify**:
   - Test with `there` (Accept), `breathe` (Accept), `the` (Accept).
   - Test with `those` (Reject), `teh` (Reject), `th` (Reject).
6. **Save**:
   - Save as `15.jff` in `set_2/15`.
