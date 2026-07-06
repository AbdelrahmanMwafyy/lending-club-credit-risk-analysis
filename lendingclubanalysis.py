import pandas as pd
import pyodbc

# Load CSV
print("Loading CSV...")
df = pd.read_csv(r'C:\Mwafy\work-data\Data analysis\Lendingclubanalysis\train_lending_club.csv')

# Fix date column
df['issue_d'] = pd.to_datetime(df['issue_d'])

# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=mwafy;'
    'DATABASE=LendingClubAnalysis;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Load rows in batches
print(f"Loading {len(df)} rows...")
batch_size = 1000

for i in range(0, len(df), batch_size):
    batch = df.iloc[i:i+batch_size]
    for _, row in batch.iterrows():
        cursor.execute("""
            INSERT INTO loans (
                id, issue_d, sub_grade, term, home_ownership,
                fico_range_low, fico_range_high, total_acc, pub_rec,
                revol_util, annual_inc, int_rate, dti, purpose,
                mort_acc, loan_amnt, application_type, installment,
                verification_status, pub_rec_bankruptcies, addr_state,
                initial_list_status, revol_bal, open_acc, emp_length,
                loan_status, time_to_earliest_cr_line
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, 
        row['id'], row['issue_d'], row['sub_grade'], row['term'],
        row['home_ownership'], row['fico_range_low'], row['fico_range_high'],
        row['total_acc'], row['pub_rec'], row['revol_util'], row['annual_inc'],
        row['int_rate'], row['dti'], row['purpose'], row['mort_acc'],
        row['loan_amnt'], row['application_type'], row['installment'],
        row['verification_status'], row['pub_rec_bankruptcies'], row['addr_state'],
        row['initial_list_status'], row['revol_bal'], row['open_acc'],
        row['emp_length'], row['loan_status'], row['time_to_earliest_cr_line']
        )
    conn.commit()
    print(f"  Inserted rows {i} to {min(i+batch_size, len(df))}")

print("Done.")
conn.close()