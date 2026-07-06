SELECT 
    grade,
    dti_bucket,
    COUNT(*)                                                        AS total_loans,
    ROUND(AVG(int_rate), 2)                                         AS avg_int_rate,
    ROUND((1 - AVG(CAST(loan_status AS FLOAT))) * 100, 2)           AS default_rate_pct
FROM loans
GROUP BY grade, dti_bucket
ORDER BY grade, dti_bucket;