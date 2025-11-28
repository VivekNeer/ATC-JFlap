# Instructions for Question 4

## Question
Construct npda’s that accept the following languages on $\Sigma = \{a, b, c\}$.
$L = \{a^n b^m c^{n+m} : n \ge 0, m \ge 0\}$

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Pushdown Automaton**.
3. **Add States**:
   - Create states `q0` to `q4`.
   - Set `q0` as **Initial**.
   - Set `q4` as **Final**.
4. **Define Transitions**:
   - `q0` -> `q1`: `(a, Z, aZ)` (Push first 'a')
   - `q0` -> `q2`: `(b, Z, bZ)` (Push first 'b' if no 'a's)
   - `q0` -> `q4`: `(λ, Z, Z)` (Accept empty string)
   - `q1` -> `q1`: `(a, a, aa)` (Push 'a's)
   - `q1` -> `q2`: `(b, a, ba)` (Push first 'b' on 'a')
   - `q1` -> `q3`: `(c, a, λ)` (Pop 'a' for 'c' if no 'b's)
   - `q2` -> `q2`: `(b, b, bb)` (Push 'b's)
   - `q2` -> `q3`: `(c, b, λ)` (Pop 'b' for 'c')
   - `q3` -> `q3`: `(c, b, λ)` (Pop 'b's)
   - `q3` -> `q3`: `(c, a, λ)` (Pop 'a's after 'b's are gone)
   - `q3` -> `q4`: `(λ, Z, Z)` (Accept if stack empty)
5. **Verify**:
   - Test with `abc` (Accept), `aabbcc` (Accept), `ac` (Accept), `bc` (Accept).
   - Test with `ab` (Reject), `abc` (Accept), `abcc` (Reject - too many c's), `aabc` (Reject - too few c's).
6. **Save**:
   - Save as `4.jff` in `set_1/4`.
