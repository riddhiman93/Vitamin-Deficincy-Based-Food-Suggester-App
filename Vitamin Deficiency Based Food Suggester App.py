from tkinter import *
import tkinter
#Initialization
root=Tk()
root.geometry("800x600")
root.resizable(0,0)
root.title("Vitamin Deficiency Based Food Suggester")
#Functions
def suggestvitamin():
    outframe=LabelFrame(root,width=630,height=300,bg="blue").place(x=75,y=300)
    outlabel=Label(outframe,text="Food Suggestion",fg="yellow",bg="blue",font=('Helvetica', 20, 'bold'),padx=0,pady=0).place(x=90,y=320)
    if vitamin.get()=="Vitamin A":
        Label(outframe,text="Scientific Name :  Retinol",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
        Label(outframe,text="Functions :  Healthy Vision, Boost Immune System",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
        Label(outframe,text="Deficiency Disease :  Xerophthalmia (Night Blindness)",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
        Label(outframe,text="Plant Sources :  Carrots, sweet potatoes, pumpkin, butternut squash, red",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
        Label(outframe,text="bell peppers, Spinach, Mangoes, cantaloupe, apricots, papaya.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
        Label(outframe,text="Animal Sources :  Salmon, sardines, trout, and fish oils, Milk, cheese,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
        Label(outframe,text="yogurt, butter, Egg yolks.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)
    elif vitamin.get()=="Vitamin B":
        Label(outframe,text="Scientific Name :  B-Complex",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
        Label(outframe,text="Functions :  DNA Replication and Production of Red Blood Cells.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
        Label(outframe,text="Deficiency Disease :  Muscle and Body Weakness.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
        Label(outframe,text="Plant Sources :  Leafy greens, potatoes, broccoli, mushrooms, avocado,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
        Label(outframe,text="peas, tomatoes, Bananas, oranges, watermelon, Beans, chickpeas.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
        Label(outframe,text="Animal Sources :  Beef, chicken, turkey, liver, pork, Salmon, tuna,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
        Label(outframe,text="sardines, clams, Milk, cheese, yogurt, eggs.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)
    elif vitamin.get()=="Vitamin C":
        Label(outframe,text="Scientific Name :  Ascorbic Acid",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
        Label(outframe,text="Functions :  Anti-oxidant and Formation of Iron.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
        Label(outframe,text="Deficiency Disease :  Scurvy, Anemia.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
        Label(outframe,text="Plant Sources :  Citrus fruits (oranges, lemons), strawberries, kiwi,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
        Label(outframe,text="bell peppers, broccoli, cantaloupe, and tomatoes.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
        Label(outframe,text="Animal Sources :  While most vitamin C comes from plants,animal",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
        Label(outframe,text="sources like raw liver, fish roe, and some organ meats offer it.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)
    elif vitamin.get()=="Vitamin D":
        Label(outframe,text="Scientific Name :  Calciferol",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
        Label(outframe,text="Functions :  Bone Growth.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
        Label(outframe,text="Deficiency Disease :  Rickets, Osteoporosis.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
        Label(outframe,text="Plant Sources :  Mushrooms (especially those exposed to UV light),",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
        Label(outframe,text="soy milk, almond milk, and rice milk.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
        Label(outframe,text="Animal Sources :  Oily fish such as salmon, sardines, trout, herring,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
        Label(outframe,text="or mackerel, red meat, egg yolks.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)
    elif vitamin.get()=="Vitamin E":
        Label(outframe,text="Scientific Name :  Tocopherol",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
        Label(outframe,text="Functions :  Anti-oxidant and Boost Immune System.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
        Label(outframe,text="Deficiency Disease :  Neuropathy, Anemia.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
        Label(outframe,text="Plant Sources :   Vegetable oils, seeds, nuts, and green leafy vegetables,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
        Label(outframe,text="sunflower seeds, almonds, hazelnuts, peanuts, avocados, mangoes.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
        Label(outframe,text="Animal Sources :  Fish (trout, salmon), eggs (especially yolk), butter,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
        Label(outframe,text="and oysters do provide it, with egg yolk being a good source.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)
    elif vitamin.get()=="Vitamin K":
        Label(outframe,text="Scientific Name :  Phylloquinone",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
        Label(outframe,text="Functions :  Blood Coagulation.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
        Label(outframe,text="Deficiency Disease :  Hemorrhagic Diseases.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
        Label(outframe,text="Plant Sources :  Spinach, lettuce, mustard greens.Broccoli, cabbage,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
        Label(outframe,text="cauliflower, basil, avocado, olive oil.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
        Label(outframe,text="Animal Sources :  Eggs, cheese, liver, meat (chicken, beef, pork),",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
        Label(outframe,text="fatty fish like salmon.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)


#Variables
vitamin=StringVar(value="Select")


#Frames
inframe=LabelFrame(root,width=630,height=150,bg="yellow").place(x=75,y=100)
outframe=LabelFrame(root,width=630,height=300,bg="blue").place(x=75,y=300)

#Labels
headinglbl=Label(root,text="Vitamin Deficiency Based Food Suggester",fg="red",font=('Helvetica', 22, 'bold'),padx=0,pady=0).place(x=100,y=50)
loclabel=Label(inframe,text="You have Deficiency of Which Vitamin ?",fg="blue",bg="yellow",font=('Helvetica', 20, 'bold'),padx=0,pady=0).place(x=120,y=120)
vdmenu=OptionMenu(root, vitamin, *["Vitamin A","Vitamin B","Vitamin C","Vitamin D","Vitamin E","Vitamin K"])
vdmenu.configure(width=16, font=('Helvetica', 14,'bold'),bg="blue",fg="yellow")
vdmenu.place(x=270,y=190)
outlabel=Label(outframe,text="Food Suggestion",fg="yellow",bg="blue",font=('Helvetica', 20, 'bold'),padx=0,pady=0).place(x=90,y=320)



#Button
farmsuggbtn=Button(root,text="Get Food Suggestion",font=('Helvetica',10,'bold'),fg="white",command=suggestvitamin,width=26,bg="red",height=2,padx=0,pady=0).place(x=275,y=255)

root.mainloop()



