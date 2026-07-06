USE LendingClubAnalysis;
GO

SELECT 
    sub_grade,
    grade,
    COUNT(*)                                    AS total_loans,
    ROUND(AVG(int_rate), 2)                     AS avg_int_rate,
    ROUND(AVG(CAST(loan_status AS FLOAT)) * 100, 2)  AS paid_rate_pct,
    ROUND((1 - AVG(CAST(loan_status AS FLOAT))) * 100, 2) AS default_rate_pct
FROM loans
GROUP BY sub_grade, grade
ORDER BY grade, sub_grade;