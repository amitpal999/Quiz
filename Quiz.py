from tkinter import *

def select(event):
    b=event.widget
    value=b["text"]
    for i in range (3):
     if value==correct_answer[i]:    
                               
            question_area.delete(1.0,END)
            question_area.insert(END,question[i+1])

            option_btn1.config(text=first_option[i+1])
            option_btn2.config(text=second_option[i+1])
            option_btn3.config(text=third_option[i+1])
            option_btn4.config(text=fourth_option[i+1])

     if value not in correct_answer:
        def close():
           obj2.destroy()
           obj.destroy()  
                
        obj2=Toplevel()
        obj2.config(bg="Light Blue")
        obj2.geometry("300x200")
        obj2.overrideredirect(True)

        img_Label=Label(obj2,text="You Won Zero Points",font=("arial",15,"bold"),bg="Light Blue",fg="black")
        img_Label.pack(pady=30)

        lose_label=Label(obj2,text="You Lose",font=("arial",15,"bold"),bg="Light Blue",fg="black")
        lose_label.pack()

        close_btn=Button(obj2,text="Close",font=("arial",20,"bold"),bg="light green",activebackground="yellow",cursor="hand2",command=close)
        close_btn.pack(pady=10)
        
        obj2.mainloop()
        obj2.resizable(0,0)
        break

correct_answer=["Haryana","Himachal","UP"]

question =["Q.1 Where is Sonipat ?",
           "Q.2 Where is CUHP ?",
           "Q.3 Where is BBAU ?",
           "     You Win The Game"]

first_option =["Haryana","Goa","Delhi","You"]
second_option =["Kerla","Kerla","Mumbai","Win"]
third_option =["Mumbai","Haryana","Kolkata","The"]
fourth_option =["Karnatak","Himachal","UP","Game"]

obj=Tk()
obj.geometry("300x350")
obj.title("Fantastic Quiz")
obj.config(bg="Light Blue")
 
question_area=Text(font=("arial",18,"bold"),width=30,height=0,bg="light green")
question_area.place(x=0,y=30)
question_area.insert(END,question[0])

label_A=Label(text=("A"),font=("arial",15,"bold"),width=4,height=2,bg="light green")
label_A.place(x=7,y=90)
option_btn1=Button(text=first_option[0],font=("arial",15,"bold"),width=10,height=0,bg="light green",activebackground="yellow",cursor="hand2")
option_btn1.place(x=90,y=95)

label_B=Label(text=("B"),font=("arial",15,"bold"),width=4,height=2,bg="light green")
label_B.place(x=7,y=150)
option_btn2=Button(text=second_option[0],font=("arial",15,"bold"),width=10,height=0,bg="light green",activebackground="yellow",cursor="hand2")
option_btn2.place(x=90,y=155)

label_C=Label(text=("C"),font=("arial",15,"bold"),width=4,height=2,bg="light green")
label_C.place(x=7,y=210)
option_btn3=Button(text=third_option[0],font=("arial",15,"bold"),width=10,height=0,bg="light green",activebackground="yellow",cursor="hand2")
option_btn3.place(x=90,y=215)

label_D=Label(text=("D"),font=("arial",15,"bold"),width=4,height=2,bg="light green")
label_D.place(x=7,y=270)
option_btn4=Button(text=fourth_option[0],font=("arial",15,"bold"),width=10,height=0,bg="light green",activebackground="yellow",cursor="hand2")
option_btn4.place(x=90,y=275)

option_btn1.bind("<Button-1>",select)
option_btn2.bind("<Button-1>",select)
option_btn3.bind("<Button-1>",select)
option_btn4.bind("<Button-1>",select)

obj.resizable(0,0)
obj.mainloop()