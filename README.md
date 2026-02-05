# UTIP Corrective Report Analysis

Sistem otomatis untuk monitoring, analisis, dan pelaporan temuan audit UTIP (Unit Temuan Internal Program).

## 📋 Deskripsi Project

Project ini mengotomatisasi proses monitoring temuan audit dengan fitur-fitur:
- **Data Retrieval**: Mengambil data temuan audit dari sistem (API atau database)
- **Automated Flagging**: Mendeteksi temuan yang sudah melewati batas waktu (overdue)
- **Root Cause Analysis**: Mengkategorikan akar penyebab masalah secara otomatis
- **Reporting**: Menghasilkan laporan Excel untuk distribusi kepada stakeholder

## 🎯 Fitur Utama

### 1. Status Flagging
Sistem secara otomatis memberikan flag pada setiap temuan:
- 🔴 **OVERDUE - URGENT**: Temuan belum selesai namun sudah melewati target date
- 🟡 **MONITORING - HIGH RISK**: Temuan dengan severity tinggi yang masih in progress
- 🟢 **ON TRACK**: Temuan yang sesuai jadwal

### 2. Root Cause Categorization
Otomatis mengklasifikasikan temuan berdasarkan deskripsi:
- **System Issue**: Masalah teknis/sistem (e.g., Altea performance)
- **Pricing/Human Error**: Kesalahan pricing atau SDM
- **General Compliance**: Masalah compliance umum

### 3. Excel Report Generation
Output otomatis dalam format Excel dengan kolom:
- Finding ID
- Description
- Severity
- Target Date
- Status
- UTIP Flagging
- Root Cause Category

## 🛠️ Teknologi yang Digunakan

- **Python 3.7+**
- **pandas**: Data manipulation dan analysis
- **numpy**: Numeric computing
- **openpyxl**: Export ke Excel

## 📦 Instalasi

1. Clone atau download project ini
2. Install dependencies:
```bash
pip install pandas numpy openpyxl
```

3. Jalankan script:
```bash
python analisis_data.py
```

## 📊 Output

Script akan generate file `UTIP_Corrective_Report.xlsx` yang berisi:
- Daftar lengkap temuan dengan semua detail
- Flag status untuk setiap temuan
- Kategori akar penyebab
- Siap untuk didistribusikan ke stakeholder

## 🔄 Cara Menggunakan

### Development Mode
Untuk mengembangkan lebih lanjut, file dapat dimodifikasi untuk:
1. Mengintegrasikan dengan API real (mengganti hardcoded data)
2. Menambahkan filter atau dashboard interaktif
3. Menambahkan alert sistem untuk temuan overdue

### Production Mode
Untuk production: 
- Integrasi dengan database yang sebenarnya
- Implementasi request API ke sistem audit
- Schedule script dengan cron job atau task scheduler

## 📝 Data Structure

```
data_audit {
    finding_id: ID unik temuan (e.g., UTIP-001)
    description: Deskripsi singkat temuan
    severity: High, Medium, Low
    target_date: Tanggal target penyelesaian
    status: Open, In Progress, Completed
}
```

## 🚀 Enhancement Ideas

- [ ] Dashboard interaktif dengan Streamlit
- [ ] Email notification untuk temuan overdue
- [ ] Database integration untuk data persistence
- [ ] API integration dengan sistem audit
- [ ] SLA tracking dan metrics
- [ ] Historical trend analysis

## 📄 Lisensi

Internal Use Only

## 👤 Author

Generated for audit monitoring purposes

---

**Last Updated**: February 5, 2026
