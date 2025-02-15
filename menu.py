from tkinter import *
from tkinter import ttk

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

def load_content(root):
    return 0

root = Tk()
root.title("Постинг в Untitled team")
root.geometry("700x400")

label = ttk.Label(text="Hello boba team")
root.protocol("WM_DELETE_WINDOW", finish)
# label.place(x=20, y=30)
# label.place(relx=0.15, rely=0.15)

for c in range(0,4): root.columnconfigure(index=c, weight=1)
for r in range(0,10): root.rowconfigure(index=r, weight=1)

label.grid(row=1, column=1, sticky=NSEW)
btn = ttk.Button(text="Загрузить", command=load_content(root))
btn["state"] = ["disabled"]
# btn.pack(anchor="nw", padx=20, pady=30)
btn.grid(row=3, column=1, columnspan=2, sticky=NSEW)

root.mainloop()