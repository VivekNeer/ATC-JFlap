# Instructions for Question 1

## Question
Design a non deterministic PDA for accepting the language $L = \{a^n b^n | n \ge 1\}$

## JFLAP Instructions
1. Open JFLAP.
2. Click on **Pushdown Automaton**.
3. **Add States**:
   - Click the **State Creator** tool (circle icon).
   - Click on the canvas to create 4 states: `q0`, `q1`, `q2`, `q3`.
   - Right-click `q0` and select **Initial**.
   - Right-click `q3` and select **Final**.
4. **Define Transitions**:
   - Click the **Transition Creator** tool (arrow icon).
   - Create the following transitions (Input, Pop, Push):
     - `q0` -> `q1`: `(a, Z, aZ)` (Push 'a' on 'Z')
     - `q1` -> `q1`: `(a, a, aa)` (Push 'a' on 'a')
     - `q1` -> `q2`: `(b, a, λ)` (Pop 'a' on 'b')
     - `q2` -> `q2`: `(b, a, λ)` (Pop 'a' on 'b')
     - `q2` -> `q3`: `(λ, Z, Z)` (Accept if stack is empty of 'a's)
5. **Verify**:
   - Go to **Input** -> **Step with Closure** or **Fast Run**.
   - Test with `aabb` (Accept), `ab` (Accept), `a` (Reject), `b` (Reject).
6. **Save**:
   - Save the file as `1.jff` in the `set_1/1` folder.
