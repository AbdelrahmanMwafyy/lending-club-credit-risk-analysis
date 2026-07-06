# lending-club-credit-risk-analysis
 Credit risk analysis dashboard — SQL Server, Python, Power BI | Pricing gap analysis across 236K loans
# Lending Club Credit Risk Analysis

## Business Question
Are Lending Club borrowers charged interest rates proportional to their actual default risk?

## Key Findings
- **Small business loans**: 10.78pp pricing gap (default 27.48% vs rate 16.70%)
- **D-grade High DTI borrowers**: default at 39% vs 25% for Low DTI — same interest rate
- **Verification paradox**: Not Verified borrowers default less than Verified across all grades
- **Portfolio gap**: overall default rate (16.84%) exceeds avg interest rate (12.60%) by 4.24pp

## Stack
Excel · Python (pandas, pyodbc) · SQL Server 2022 · Power BI Desktop · DAX

## Files
- `load_loans.py` — Python pipeline loading 236,846 rows into SQL Server
- `01_baseline_subgrade.sql` — Default rate and interest rate by sub-grade
- `02_pricing_gap.sql` — Pricing gap ranked by sub-grade
- `03_dti_analysis.sql` — DTI bucket impact within grades
- `04_verification_analysis.sql` — Verification status paradox analysis
- `05_purpose_pricing_gap.sql` — Purpose-level pricing mismatch
- `lending_club_credit_risk_memo.pdf` — Full analytical memo with recommendations

## Dashboard Preview

### Page 1 — Executive Summary
![Executive Summary](screenshots/01_executive_summary.png)

### Page 2 — Pricing Gap Analysis
![Pricing Gap](screenshots/02_pricing_gap.png)

### Page 3 — Borrower Segments
![Borrower Segments](screenshots/03_borrower_segments.png)

### Page 4 — Loan Purpose Analysis
![Loan Purpose](screenshots/04_loan_purpose.png)
