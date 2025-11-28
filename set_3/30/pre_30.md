# Instructions for Question 30

## Question
Construct a TM to accept the language $L=\{ww^R |w \in (a+b)^*\}$

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Turing Machine** (Single Tape).
3. **Add States**:
   - Create states `q0` to `q6`.
   - Set `q0` as **Initial**.
   - Set `q6` as **Final**.
4. **Define Transitions**:
   - This is essentially the same as the even-length palindrome logic, but strictly $ww^R$ implies even length.
   - **Start**:
     - `q0` -> `q1`: `(a, \square, R)`
     - `q0` -> `q4`: `(b, \square, R)`
     - `q0` -> `q6`: `(\square, \square, S)` (Empty string is $ww^R$ where $w=\epsilon$)
   - **Move Right (after 'a')**:
     - `q1` -> `q1`: `(a, a, R)`
     - `q1` -> `q1`: `(b, b, R)`
     - `q1` -> `q2`: `(\square, \square, L)`
   - **Match End (for 'a')**:
     - `q2` -> `q3`: `(a, \square, L)`
   - **Return Left**:
     - `q3` -> `q3`: `(a, a, L)`
     - `q3` -> `q3`: `(b, b, L)`
     - `q3` -> `q0`: `(\square, \square, R)`
   - **Move Right (after 'b')**:
     - `q4` -> `q4`: `(a, a, R)`
     - `q4` -> `q4`: `(b, b, R)`
     - `q4` -> `q5`: `(\square, \square, L)`
   - **Match End (for 'b')**:
     - `q5` -> `q3`: `(b, \square, L)`
5. **Verify**:
   - Test with `abba` (Accept), `aaaa` (Accept), `bbaabb` (Accept).
   - Test with `aba` (Reject - odd length), `ab` (Reject), `a` (Reject).
6. **Save**:
   - Save as `30.jff` in `set_3/30`.
