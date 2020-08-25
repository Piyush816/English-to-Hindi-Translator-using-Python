from googletrans import Translator
from tkinter import *
bg = "deep sky blue"
font = "lucida 13 bold underline"
def translator(word):
    translator = Translator()
    translation = translator.translate(word,dest="hindi")
    return translation.text

def translate():
    wor = word.get()
    ans = translator(wor)
    answer.delete(0,END)
    answer.insert(0,ans)
    
def refresh():
    word.delete(0,END)
    answer.delete(0,END)

    
root = Tk()
root.geometry("250x350")
root.title("Translator")
root.configure(bg = bg)
Label(text = "English to Hindi Translator",font = font,pady = 10,bg = bg,fg = "white").pack()
Label(text = "Enter word",font = font,pady = 10,bg = bg,fg = "white").pack()
word = Entry(font = "arial 12")
word.pack()
Button(text = "Translate",font = "arial 12",bg = "snow",command = translate).pack(pady = 25)
Button(text = "Refresh",font = "arial 12",bg = "snow",command = refresh).pack()
Label(text = "Answer",font = font,pady = 10,bg = bg,fg = "white").pack()
answer = Entry(font = "arial 12")
answer.pack()



root.mainloop()
