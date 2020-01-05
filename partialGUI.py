from tkinter import*
import random
import time

root = Tk()
root.geometry("890x580+0+0")
root.title("CASH BALANCING SYSTEM")

Tops = Frame(root,width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="SALES CALCULATOR",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="Black",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------------------------------------------------------------------------------
rand = StringVar()
n1000 = StringVar()
n500 = StringVar()
n200 = StringVar()
n100 = StringVar()
n50 = StringVar()
n20 = StringVar()
n10 = StringVar()
n5 = StringVar()
n1 = StringVar()
Total = StringVar()





lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Name: ",fg="red",bd=20,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="white" ,justify='right')
txtreference.grid(row=0,column=1)

lbln1000 = Label(f1, font=( 'aria' ,16, 'bold' ),text=" No. of 1000: ",fg="black",bd=10,anchor='w')
lbln1000.grid(row=1,column=0)
txtn1000 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n1000, bd=6,insertwidth=4,bg="white" ,justify='right')
txtn1000.grid(row=1,column=1)

lbln500 = Label(f1, font=( 'aria' ,16, 'bold' ),text=" No. of 500: ",fg="black",bd=10,anchor='w')
lbln500.grid(row=2,column=0)
txtn500 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n500 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn500.grid(row=2,column=1)

lbln200 = Label(f1, font=( 'aria' ,16, 'bold' ),text="No. of 200: ",fg="black",bd=10,anchor='w')
lbln200.grid(row=3,column=0)
txtn200 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n200 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn200.grid(row=3,column=1)


lbln100 = Label(f1, font=( 'aria' ,16, 'bold' ),text="No. of 100: ",fg="black",bd=10,anchor='w')
lbln100.grid(row=4,column=0)
txtn100 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n100 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn100.grid(row=4,column=1)

lbln50 = Label(f1, font=( 'aria' ,16, 'bold' ),text="No. of 50: ",fg="black",bd=10,anchor='w')
lbln50.grid(row=5,column=0)
txtn50 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n50 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn50.grid(row=5,column=1)

lbln20 = Label(f1, font=( 'aria' ,16, 'bold' ),text="No. of 20: ",fg="black",bd=10,anchor='w')
lbln20.grid(row=6,column=0)
txtn20 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n20 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn20.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lbln10 = Label(f1, font=( 'aria' ,16, 'bold' ),text="No. of 10: ",fg="black",bd=10,anchor='w')
lbln10.grid(row=2,column=2)
txtn10 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n10 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn10.grid(row=2,column=3)

lbln5 = Label(f1, font=( 'aria' ,16, 'bold' ),text="No. of 5: ",fg="black",bd=10,anchor='w')
lbln5.grid(row=3,column=2)
txtn5 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n5 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn5.grid(row=3,column=3)

lbln1 = Label(f1, font=( 'aria' ,16, 'bold' ),text="No. of 1: ",fg="black",bd=10,anchor='w')
lbln1.grid(row=4,column=2)
txtn1 = Entry(f1,font=('ariel' ,16,'bold'), textvariable=n1 , bd=6,insertwidth=4,bg="white" ,justify='right')
txtn1.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="green",bd=10,anchor='w')
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtTotal.grid(row=6,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red")
btnTotal.grid(row=8, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="red")
btnreset.grid(row=8, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red")
btnexit.grid(row=8, column=3)


root.mainloop()