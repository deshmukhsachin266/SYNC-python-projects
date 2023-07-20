import pyshorteners
from tkinter import *
from tkinter import messagebox

def shorten_url():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        entry1.delete(0, END)
        entry1.insert(0, short_url)
    except pyshorteners.exceptions.ShorteningErrorException:
        messagebox.showerror("Error", "Error occurred while shortening the URL. Please try again later.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

root = Tk()
root.geometry('500x200')
root.title('URL Shortener')

entry = Entry(root, fg='#FF4517', bg='#FFF9C2', bd=1, width=50)
entry.place(x=20, y=50)

entry1 = Entry(root, fg='#FF4517', bg='#FFF9C2', bd=1, width=50)
entry1.place(x=20, y=120)

label = Label(root, text='Enter the URL:')
label.place(x=20, y=20)

label1 = Label(root, text='Short URL:')
label1.place(x=20, y=90)

btn = Button(root, text="Shorten", bd=0, bg='#1061E6', command=shorten_url)
btn.place(x=220, y=180)

root.mainloop()
