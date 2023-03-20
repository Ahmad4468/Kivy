from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        # Create the title label
        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg="white",
                         fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        # Load the image and create the button
        img1 = Image.open("D:\downloads\images.png")
        img1 = img1.resize((80,80), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=70, y=20)

        #DataFrame
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", fg="darkgreen",
                                   font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        #Button Frame

        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1530, height=65)

        ####Main Button
        btnAddData = Button(ButtonFrame, text="Medicine Add", font=("arial", 12, "bold"), bg="darkgreen", fg="white")
        btnAddData.grid(row=0, column=0)

        btnUpdateMed = Button(ButtonFrame, text="UPDATE", font=("arial", 13, "bold"), width=14, bg="darkgreen",
                              fg="white")
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed = Button(ButtonFrame, text="DELETE", font=("arial", 13, "bold"), width=14, bg="darkgreen",
                              fg="white")
        btnDeleteMed.grid(row=0, column=2)

        btnResetMed = Button(ButtonFrame, text="RESET", font=("arial", 13, "bold"), width=14, bg="darkgreen",
                             fg="white")
        btnResetMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonFrame, text="EXIT", font=("arial", 13, "bold"), width=14, bg="darkgreen",
                            fg="white")
        btnExitMed.grid(row=0, column=4)

        #Search By

        lblSearch = Label(ButtonFrame,font=("arial", 17, "bold"), text="Search By",padx=2,bg="red", fg="white")
        lblSearch.grid(row=0, column=5,sticky=W)

        search_combo=ttk.Combobox(buttonFrame,width=12,font=("arial", 13, "bold"))
        search_combo.grid(row=0,column=6)
        search_combo







if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()