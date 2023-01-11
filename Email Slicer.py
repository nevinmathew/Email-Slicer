from tkinter import *

def save_mail():
    mail=emailA.get()
    userLabel.config(text="", bg="#BF8A6B")
    try:
        mailA=mail.strip().split('@')
        user=mailA[0].replace(" ","")
        domain=mailA[1].replace(" ","")
        emailServiceProvider = mail[mail.index('@') + 1:mail.index('.')].capitalize()
        # domain = email[email.index('@') + 1:]

        userLabel.config(text="The username is "+ user + "\n The domain is "+ domain + "\n The email service provider is " + emailServiceProvider, bg="#96bf6b")   
        emailA.delete(0, END)

    except:
        userLabel.config(text="Insert a valid adress", bg="#BF8A6B")     
        emailA.delete(0, END)
        return


root=Tk()
root.title("Email Slicer")
root.geometry('550x300')
root.config(bg="#dfedf0")
root.resizable(0,0)

your=Label(root,text="Enter your email address:", bg="#dfedf0")
your.grid(row=1,column=0, pady=10)

emailA=Entry(root, width=85)
emailA.grid(row=2,column=0,padx=20)

enter=Button(root, text="Enter", padx=10, pady=2, bg="#6493fa", command=save_mail,)
enter.grid(row=3,column=0,pady=20)

userLabel=Label(root, text="")
userLabel.grid(row=4, column=0, pady=10)

root.mainloop()
