# Instructions for Question 25

## Question
Design a Turing Machine to accept the language $L=\{ 0^n 1^n 2^n | n \ge 1 \}$.

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Turing Machine** (Single Tape).
3. **Add States**:
   - Create states `q0` to `q6`.
   - Set `q0` as **Initial**.
   - Set `q6` as **Final**.
4. **Define Transitions**:
   - **Start**:
     - `q0` -> `q1`: `(0, X, R)` (Mark '0', move Right)
     - `q0` -> `q5`: `(Y, Y, R)` (If all 0s marked, check for completion)
   - **Find Matching 1**:
     - `q1` -> `q1`: `(0, 0, R)`
     - `q1` -> `q1`: `(Y, Y, R)`
     - `q1` -> `q2`: `(1, Y, R)` (Found '1', mark 'Y', move Right)
   - **Find Matching 2**:
     - `q2` -> `q2`: `(1, 1, R)`
     - `q2` -> `q2`: `(Z, Z, R)`
     - `q2` -> `q3`: `(2, Z, L)` (Found '2', mark 'Z', move Left)
   - **Return to Start**:
     - `q3` -> `q3`: `(0, 0, L)`
     - `q3` -> `q3`: `(1, 1, L)`
     - `q3` -> `q3`: `(2, 2, L)`
     - `q3` -> `q3`: `(Y, Y, L)`
     - `q3` -> `q3`: `(Z, Z, L)`
     - `q3` -> `q0`: `(X, X, R)` (Back to start)
   - **Final Check**:
     - `q5` -> `q5`: `(Y, Y, R)`
     - `q5` -> `q5`: `(Z, Z, R)`
     - `q5` -> `q6`: `(\square, \square, S)` (Accept)
5. **Verify**:
   - Test with `012` (Accept), `001122` (Accept).
   - Test with `01` (Reject), `0122` (Reject), `0012` (Reject).
6. **Save**:
   - Save as `25.jff` in `set_3/25`.
