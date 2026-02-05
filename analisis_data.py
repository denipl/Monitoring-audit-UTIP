import pandas as pd
import numpy as np
from datetime import datetime

# 1. Simulasi Interaksi API (Data Retrieval)
# Dalam proyek nyata, kamu akan menggunakan: requests.get(url)
data_audit = {
    'finding_id': ['UTIP-001', 'UTIP-002', 'UTIP-003', 'UTIP-004'],
    'description': ['System lag in Altea', 'Ticket price mismatch', 'Baggage rule error', 'Missing documentation'],
    'severity': ['High', 'Medium', 'High', 'Low'],
    'target_date': ['2026-01-15', '2026-02-10', '2026-01-01', '2026-03-01'],
    'status': ['In Progress', 'In Progress', 'Open', 'Completed']
}

df = pd.DataFrame(data_audit)
df['target_date'] = pd.to_datetime(df['target_date'])

# 2. Automated Data Flagging Logic
# Menentukan apakah temuan sudah melewati batas waktu (Overdue)
today = datetime.now()

def check_flagging(row):
    if row['status'] != 'Completed' and row['target_date'] < today:
        return '🔴 OVERDUE - URGENT'
    elif row['severity'] == 'High' and row['status'] != 'Completed':
        return '🟡 MONITORING - HIGH RISK'
    else:
        return '🟢 ON TRACK'

df['utip_flagging'] = df.apply(check_flagging, axis=1)

# 3. Root Cause Analysis (Categorization)
# Mencari kata kunci untuk mengelompokkan masalah
def categorize_cause(desc):
    desc = desc.lower()
    if 'system' in desc or 'altea' in desc:
        return 'System Issue'
    elif 'price' in desc or 'fare' in desc:
        return 'Pricing/Human Error'
    else:
        return 'General Compliance'

df['root_cause_category'] = df['description'].apply(categorize_cause)

# 4. Export to Excel (Reporting)
df.to_excel('UTIP_Corrective_Report.xlsx', index=False)

print("Proses Monitoring Selesai. Laporan 'UTIP_Corrective_Report.xlsx' telah dibuat.")
print(df[['finding_id', 'utip_flagging', 'root_cause_category']])