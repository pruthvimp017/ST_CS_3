import re
import tkinter as tk
from tkinter import ttk

def check_strength():
    password = entry.get()
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• At least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add a lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("• Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Add a special character")

    # Convert score (0–5) to percentage
    percent = (score / 5) * 100
    progress['value'] = percent

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    result_label.config(text=f"Strength: {strength}", fg=color)

    if feedback:
        feedback_label.config(text="\n".join(feedback))
    else:
        feedback_label.config(text="✔ Password meets all criteria", fg="green")


# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x330")
root.resizable(False, False)

tk.Label(root, text="Enter Password", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)

progress = ttk.Progressbar(root, length=300, mode='determinate', maximum=100)
progress.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

feedback_label = tk.Label(root, text="", fg="gray", justify="left")
feedback_label.pack(pady=10)

root.mainloop()
