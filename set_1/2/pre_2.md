# Instructions for Question 2

## Question
Construct a DFA for $L = \{ab^n a^m : n \ge 2, m \ge 3\}$

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Finite Automaton**.
3. **Add States**:
   - Create states `q0` to `q6`.
   - Set `q0` as **Initial**.
   - Set `q6` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `a`
   - `q1` -> `q2`: `b`
   - `q2` -> `q3`: `b`
   - `q3` -> `q3`: `b` (Loop for $n > 2$)
   - `q3` -> `q4`: `a`
   - `q4` -> `q5`: `a`
   - `q5` -> `q6`: `a`
   - `q6` -> `q6`: `a` (Loop for $m > 3$)
5. **Verify**:
   - Test with `abbaaa` (Accept), `abbbaaa` (Accept), `abbaaaa` (Accept).
   - Test with `abaaa` (Reject - only 1 b), `abbaa` (Reject - only 2 a's).
6. **Save**:
   - Save as `2.jff` in `set_1/2`.
