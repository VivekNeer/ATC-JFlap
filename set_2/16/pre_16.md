# Instructions for Question 16

## Question
Draw a deterministic and non-deterministic finite automata which accept a string containing “ing” at the end of a string in a string of {a-z}, e.g., “anything” but not “anywhere”.

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0` to `q3`.
   - Set `q0` as **Initial**.
   - Set `q3` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `i`
   - `q0` -> `q0`: `[a-z] - {i}` (Reset)
   - `q1` -> `q2`: `n`
   - `q1` -> `q1`: `i` (Stay on 'i')
   - `q1` -> `q0`: `[a-z] - {i, n}` (Reset)
   - `q2` -> `q3`: `g` (Found "ing" at end)
   - `q2` -> `q1`: `i` (Back to 'i')
   - `q2` -> `q0`: `[a-z] - {i, g}` (Reset)
   - `q3` -> `q1`: `i` (Overlap 'i')
   - `q3` -> `q0`: `[a-z] - {i}` (Reset, since it must be at the end)
5. **Verify**:
   - Test with `anything` (Accept), `sing` (Accept), `going` (Accept).
   - Test with `anywhere` (Reject), `in` (Reject), `singer` (Reject - 'ing' is not at end).
6. **Save**:
   - Save as `16.jff` in `set_2/16`.
