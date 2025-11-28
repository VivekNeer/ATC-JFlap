# Instructions for Question 26

## Question
Construct a Turing Machine to accept the language $L=\{ w |w \in (0+1)^* \}$ Containing the substring 001.

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Turing Machine** (Single Tape).
3. **Add States**:
   - Create states `q0` to `q3`.
   - Set `q0` as **Initial**.
   - Set `q3` as **Final**.
4. **Define Transitions**:
   - **Scan Right**:
     - `q0` -> `q0`: `(1, 1, R)` (Skip 1s)
     - `q0` -> `q1`: `(0, 0, R)` (Found first '0')
     - `q1` -> `q1`: `(0, 0, R)` (Found second '0', stay in q1/q2 logic) - *Correction*: Better to have distinct states for '0', '00'.
     - Let's refine:
       - `q0` (Start):
         - `1` -> `q0`, R
         - `0` -> `q1`, R
       - `q1` (Saw '0'):
         - `1` -> `q0`, R (Reset)
         - `0` -> `q2`, R (Saw '00')
       - `q2` (Saw '00'):
         - `0` -> `q2`, R (Stay in '00' state, e.g. '000')
         - `1` -> `q3`, R (Saw '001', Accept)
       - `q3` (Accept):
         - `0` -> `q3`, R
         - `1` -> `q3`, R
         - `\square` -> `q3`, S
5. **Verify**:
   - Test with `001` (Accept), `1001` (Accept), `0001` (Accept).
   - Test with `00` (Reject), `01` (Reject), `111` (Reject).
6. **Save**:
   - Save as `26.jff` in `set_3/26`.
