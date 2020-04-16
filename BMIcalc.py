from tkinter import *

def bmicalculator():
    global bmi
    bmi_num=StringVar()
    weight1=float(weight.get())
    height1=float(height.get())
    bmi.set(float(weight1/((height1)**2)*10000))
    vk=float(bmi.get())
    print(type(vk))
    if vk <18.5:
        bmitext.set("You are underweight")
    if vk >=18.5 and vk<=24.9:
        bmitext.set("You have ideal weight")
    if vk >=25:
        bmitext.set("you are Overweight")
    

bmicalc=Tk()
height=StringVar()
weight=StringVar()

bmicalc.title(" BMI calculator")
lab1=Label(bmicalc,width=20, text="Enter the Height in cms")
lab1.grid(row=2,column=1)
ent1=Entry(bmicalc, width=20, bg="grey",textvariable = height)
ent1.grid(row=2, column=2)

lab2=Label(bmicalc,width=20, text="Enter the Weight in Kgs")
lab2.grid(row=3,column=1)
ent2=Entry(bmicalc, width=20, bg="grey",textvariable = weight)
ent2.grid(row=3, column=2)

but1=Button(bmicalc,width=20, text="Calculate",command=bmicalculator)
but1.grid(row=4, columnspan=4)

lab3=Label(bmicalc,width=20,text="BMI number is:").grid(row=5,column=1)
bmi=StringVar()
lab3=Label(bmicalc,width=20,textvariable=bmi).grid(row=5, column=2)
bmitext=StringVar()
lab3=Label(bmicalc,width=20,textvariable=bmitext).grid(row=6, columnspan=4)


bmicalc.mainloop()
