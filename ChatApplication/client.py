import socket
import threading
import tkinter as tk
from tkinter import simpledialog

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

window = tk.Tk()
window.title("Chat Room")
window.geometry("420x550")
window.configure(bg="#e5ddd5")

username = simpledialog.askstring("Username", "Enter your name", parent=window)
client.send(username.encode())


# ===== Chat Area =====
canvas = tk.Canvas(window, bg="#e5ddd5")
frame = tk.Frame(canvas, bg="#e5ddd5")
scrollbar = tk.Scrollbar(window, command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)
canvas.create_window((0, 0), window=frame, anchor="nw")


def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)


# ===== Message Bubble =====
def add_message(text, sender):
    bubble = tk.Label(
        frame,
        text=text,
        wraplength=250,
        font=("Segoe UI", 10),
        padx=10,
        pady=6
    )

    if sender == username:
        bubble.configure(bg="#dcf8c6", anchor="e")
        bubble.pack(anchor="e", pady=4, padx=10)
    elif sender == "system":
        bubble.configure(bg="#e5ddd5", fg="gray")
        bubble.pack(pady=5)
    else:
        bubble.configure(bg="white", anchor="w")
        bubble.pack(anchor="w", pady=4, padx=10)

    canvas.update_idletasks()
    canvas.yview_moveto(1)


# ===== Receive =====
def receive():
    while True:
        try:
            msg = client.recv(1024).decode().strip()

            if msg.startswith("🟢") or msg.startswith("🔴"):
                add_message(msg, "system")
            else:
                sender, message = msg.split(":", 1)
                add_message(f"{sender}:{message}", sender)

        except:
            break


# ===== Send =====
def send():
    msg = entry.get()
    if msg:
        full_msg = f"{username}: {msg}"
        client.send(full_msg.encode())
        add_message(msg, username)
        entry.delete(0, tk.END)


# ===== Input Area =====
bottom = tk.Frame(window, bg="#f0f0f0")
bottom.pack(fill="x")

entry = tk.Entry(bottom, font=("Segoe UI", 11))
entry.pack(side="left", fill="x", expand=True, padx=8, pady=8)

send_btn = tk.Button(
    bottom, text="Send",
    font=("Segoe UI", 11, "bold"),
    bg="#128c7e", fg="white",
    command=send
)
send_btn.pack(side="right", padx=8, pady=8)


thread = threading.Thread(target=receive)
thread.start()

window.mainloop()

