# Instructions for Question 24

## Question
Design a Turing Machine to accept the language $L=\{ 0^n 1^n | n \ge 1 \}$.

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Turing Machine** (Single Tape).
3. **Add States**:
   - Create states `q0` to `q4`.
   - Set `q0` as **Initial**.
   - Set `q4` as **Final**.
4. **Define Transitions**:
   - **Start**:
     - `q0` -> `q1`: `(0, X, R)` (Mark '0' with 'X', move Right)
     - `q0` -> `q4`: `(Y, Y, R)` (If all 0s marked, check for completion)
   - **Find Matching 1**:
     - `q1` -> `q1`: `(0, 0, R)` (Skip 0s)
     - `q1` -> `q1`: `(Y, Y, R)` (Skip Ys)
     - `q1` -> `q2`: `(1, Y, L)` (Found matching '1', mark with 'Y', move Left)
   - **Return to Start**:
     - `q2` -> `q2`: `(0, 0, L)`
     - `q2` -> `q2`: `(Y, Y, L)`
     - `q2` -> `q0`: `(X, X, R)` (Back to start after X)
   - **Final Check**:
     - `q0` -> `q3`: `(Y, Y, R)` (All 0s handled, ensure no extra 1s)
     - `q3` -> `q3`: `(Y, Y, R)`
     - `q3` -> `q4`: `(\square, \square, S)` (Accept)
5. **Verify**:
   - Test with `01` (Accept), `0011` (Accept), `000111` (Accept).
   - Test with `001` (Reject), `011` (Reject), `0` (Reject), `1` (Reject).
6. **Save**:
   - Save as `24.jff` in `set_3/24`.
