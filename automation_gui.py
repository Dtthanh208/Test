import customtkinter as ctk
from tkinter import messagebox
import pyautogui
import keyboard
import time

def start_automation():
    try:
        repeats = int(entry_repeats.get())
        interval = float(entry_interval.get())
        message = entry_message.get()

        # Hiển thị thông báo hướng dẫn người dùng
        messagebox.showinfo("Hướng dẫn", "Di chuyển chuột đến vị trí cần nhập và nhấn phím F8 để bắt đầu.")

        # Đợi người dùng nhấn phím F8 để bắt đầu
        keyboard.wait('F8')

        for i in range(repeats):
            pyautogui.write(f'{message} {i+1}', interval=interval)
            pyautogui.press('enter')
            time.sleep(interval)
        
        messagebox.showinfo("Hoàn thành", "Đã hoàn thành tự động nhập liệu.")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Tạo cửa sổ chính
root = ctk.CTk()
root.title("Tự Động Nhập Liệu")
root.geometry("400x500")

# Tạo một frame để chứa các widget
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Nhãn tiêu đề
title_label = ctk.CTkLabel(frame, text="Chương Trình Tự Động Nhập Liệu", font=("Arial", 20))
title_label.pack(pady=10)

# Nhãn và ô nhập cho số lần lặp
label_repeats = ctk.CTkLabel(frame, text="Số lần lặp:")
label_repeats.pack(pady=10)
entry_repeats = ctk.CTkEntry(frame)
entry_repeats.pack(pady=10)

# Nhãn và ô nhập cho khoảng thời gian giữa các lần nhập
label_interval = ctk.CTkLabel(frame, text="Khoảng thời gian giữa các lần nhập (giây):")
label_interval.pack(pady=10)
entry_interval = ctk.CTkEntry(frame)
entry_interval.pack(pady=10)

# Nhãn và ô nhập cho thông điệp
label_message = ctk.CTkLabel(frame, text="Thông điệp:")
label_message.pack(pady=10)
entry_message = ctk.CTkEntry(frame)
entry_message.pack(pady=10)

# Nút bắt đầu tự động nhập liệu
button_start = ctk.CTkButton(frame, text="Bắt đầu", command=start_automation)
button_start.pack(pady=20)

# Chạy vòng lặp chính của tkinter
root.mainloop()
