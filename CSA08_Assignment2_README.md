# CSA08 – Python Programming – Assignment 2

## Student Details
- **Name:** Manibala.I
- **Register Number:** 1924260190
- **Course:** CSA08 – Python Programming
- **Assignment:** Assignment 2
- **CO Coverage:** CO2 – Control flow constructs, string operations and functions

## Python Environment
- **Python version:** Python 3.10 or later
- **Libraries:** Python Standard Library only
  - `time` – execution-time measurement
  - `functools` – memoisation with `lru_cache`
  - `sys` – checking the recursion limit
- **External packages:** None
- **requirements.txt:** Not required because no external packages are used.

Check your Python version with:
```bash
python --version
```

## Repository Structure
```text
CSA0809---Assignment-2/
├── README.md
├── Task01/
│   └── q1_decisions.py
├── Task02/
│   └── q2_loops.py
├── Task03/
│   └── q3_vehicle_validator.py
├── Task04/
│   └── q4_string_building.py
├── Task05/
│   └── q5_functions_scope.py
├── Task06/
│   └── q6_recursion.py
└── Task07/
    └── q7_redesign.py
```

## How to Run
Open Anaconda Prompt or a terminal, enter the relevant task folder with `cd`, and run the command below.

| Task | Python file | Command |
|---|---|---|
| Q1 | `q1_decisions.py` | `python q1_decisions.py` |
| Q2 | `q2_loops.py` | `python q2_loops.py` |
| Q3 | `q3_vehicle_validator.py` | `python q3_vehicle_validator.py` |
| Q4 | `q4_string_building.py` | `python q4_string_building.py` |
| Q5 | `q5_functions_scope.py` | `python q5_functions_scope.py` |
| Q6 | `q6_recursion.py` | `python q6_recursion.py` |
| Q7 | `q7_redesign.py` | `python q7_redesign.py` |

Example:
```bash
cd Task01
python q1_decisions.py
```

## Task-wise Description and Result Notes

### Q1 – Decisions with Many Boundaries
**File:** `Task01/q1_decisions.py`
- Compares separate `if` statements with `if-elif-else` for electricity subsidy eligibility.
- Tests eight household cases, including 100, 101, 200 and 201 units.
- Also demonstrates `match-case` and a lookup-loop alternative.
- **Result:** Prints and compares the decisions produced by the different approaches.

### Q2 – Loops that Count Attempts
**File:** `Task02/q2_loops.py`
- Demonstrates OTP attempt counting with `while` and `for range()`.
- Includes `break`, `continue`, `pass`, loop `else`, blank-entry handling and the changed security-question condition.
- Includes a recursive alternative.
- **Result:** Blank entries are skipped without using an attempt; the test cases show verification or account-lock outcomes.

### Q3 – Vehicle Registration Number Validator
**File:** `Task03/q3_vehicle_validator.py`
- Normalises registration text by removing spaces and hyphens and converting it to uppercase.
- Validates the state, district, series and final four digits using string methods and slicing.
- Formats valid registrations for a receipt.
- **Result:** Valid examples are accepted and formatted; invalid examples are rejected.

### Q4 – Building Long Text: `+` or `join()`?
**File:** `Task04/q4_string_building.py`
- Builds text using repeated `+=`, `join()` and f-string-based parts.
- Measures performance for 1,000, 10,000 and 200,000 items.
- Performs three runs per method and reports average times.
- **Result:** Checks whether all methods produce identical text and prints actual timings. Timings vary by computer.

### Q5 – Functions, Parameters and Scope
**File:** `Task05/q5_functions_scope.py`
- Demonstrates the mutable default-list bug and the corrected `None` default.
- Tests separate orders for three customers.
- Demonstrates positional, keyword and default parameters, multiple return values, and local, global and nonlocal scope.
- Includes a closure alternative.
- **Result:** The corrected function creates independent order lists when no list is supplied.

### Q6 – Recursion and Its Limits
**File:** `Task06/q6_recursion.py`
- Compares plain recursion, memoised recursion and an iterative solution for counting stair-climbing ways.
- Displays answers for `n = 1` to `6`, a call-tree illustration, function-call counts and timings.
- Tests memoised recursion at `n = 1,000` and explains a possible recursion-depth error.
- **Result:** Memoisation reduces repeated calls; the iterative solution avoids recursion-depth limitations.

### Q7 – Diagnose, Redesign and Validate
**File:** `Task07/q7_redesign.py`
- Selects the repeated calculations in Q6's plain recursive solution as the bottleneck.
- Redesigns the solution using memoisation.
- Compares results, function-call counts and execution times for the same inputs.
- **Result:** The redesigned version should produce the same answers with fewer repeated function calls; actual measurements are printed by the program.

## Execution Evidence
After running each program:
1. Save an output screenshot in its corresponding task folder.
2. Record the actual timings printed by your computer for Q4, Q6 and Q7.
3. Include actual function-call counts and timing results in the assignment report.
4. Do not use estimated or copied timings in place of your own measurements.

Suggested screenshot filenames:
```text
Task01/output_q1.png
Task02/output_q2.png
Task03/output_q3.png
Task04/output_q4.png
Task05/output_q5.png
Task06/output_q6.png
Task07/output_q7.png
```

## GitHub Submission
- Upload all seven task folders and this `README.md` to the assignment repository.
- Commit progressively, with at least one commit per task as required.
- Add the repository URL to the report cover page and submit it in the course portal.
- Ensure the repository is public or that the course faculty has been added as a collaborator.
