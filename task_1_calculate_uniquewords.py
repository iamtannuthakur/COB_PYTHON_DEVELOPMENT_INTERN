from tkinter import *
from tkinter import messagebox, filedialog


root = Tk()
def close():
   root.quit()


def select_files():
    type = (
        ('text files', '*txt'),
        ('All files', '*.*')
    )

    file_path = filedialog.askopenfilename(title="Select a location", filetypes=type)
    open_file = open(file_path, 'r')
    text = open_file.read()
    text = text.lower()
    words = text.split()

    unique = []
    co = 0
    for word in words:
        if word not in unique and words.count(word)==1:
           unique.append(word)
           unique.sort()
           co += 1

    messagebox.showinfo("Unique Words : ", f"Unique Words: {unique}\n\n Number of occurrence : {co}")
    root.quit()

    # Print
    print(unique)

root.geometry("950x600")
root.title('Calculating Unique words')
root.resizable(width=True, height=True)
root.configure(bg='pink')
Label(text="COUNTING UNIQUE WORDS IN A FILE ", font="impact 35 bold", bg="green",width=100, height=2).pack(pady=2)

Exit_Btn = Button(root, text="Exit", font=("Kokila", 20, 'bold'), bg="dodger blue", fg="black", width=20,
                  command=close).place(x=650,y=300)

fileButton = Button(root, text="Select File", font=("Kokila 30 bold"), bg="blue", width=30,
                            command=select_files)
# fileButton.place(x=200, y=500)
fileButton.pack(pady=40)

root.mainloop()
