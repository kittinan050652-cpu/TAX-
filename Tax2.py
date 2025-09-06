import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณภาษี
def calculate_tax(income):
    if income <= 150000:
        return 0
    elif income <= 300000:
        return (income - 150000) * 0.05
    elif income <= 500000:
        return (150000 * 0.05) + (income - 300000) * 0.10
    elif income <= 750000:
        return (150000 * 0.05) + (200000 * 0.10) + (income - 500000) * 0.15
    elif income <= 1000000:
        return (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (income - 750000) * 0.20
    elif income <= 2000000:
        return (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (income - 1000000) * 0.25
    elif income <= 5000000:
        return (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (1000000 * 0.25) + (income - 2000000) * 0.30
    else:
        return (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (1000000 * 0.25) + (3000000 * 0.30) + (income - 5000000) * 0.35

# ฟังก์ชันเมื่อกดปุ่มคำนวณ
def on_calculate():
    try:
        income = float(entry_income.get())
        tax = calculate_tax(income)
        result_label.config(text=f"คุณต้องจ่ายภาษี: {tax:,.2f} บาท")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้อง")

# ฟังก์ชันปิดโปรแกรม
def on_exit():
    root.destroy()

# สร้างหน้าต่างโปรแกรม
root = tk.Tk()
root.title("โปรแกรมคำนวณภาษี")

# ✅ ทำให้หน้าต่างเต็มหน้าจอ
root.state("zoomed")

# ฟอนต์
main_font = ("TH Sarabun New", 24)
label_font = ("TH Sarabun New", 26, "bold")
small_font = ("TH Sarabun New", 18)

# UI หลัก
tk.Label(root, text="กรุณากรอกรายได้ทั้งปี (บาท):", font=label_font).pack(pady=30)
entry_income = tk.Entry(root, width=30, font=main_font)
entry_income.pack(pady=10)

tk.Button(root, text="คำนวณภาษี", command=on_calculate, font=main_font, width=20, bg="#4CAF50", fg="white").pack(pady=15)

result_label = tk.Label(root, text="", font=label_font, fg="blue")
result_label.pack(pady=20)

tk.Button(root, text="ออกจากโปรแกรม", command=on_exit, font=main_font, width=20, bg="red", fg="white").pack(pady=10)

# รายชื่อด้านล่าง
tk.Label(
    root,
    text="นาย กิตตินันท์ สุขเกลี้ยง เลขที่ 1\nน.ส. บารากัส โกมาลา เลขที่ 10\nน.ส. เบญจมาศ ชูใจ เลขที่ 11",
    font=small_font,
    justify="center"
).pack(side="bottom", pady=20)

# เริ่มต้นโปรแกรม
root.mainloop()
