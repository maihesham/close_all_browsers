import os
import webbrowser
import time
import tkinter
import tkinter.messagebox
#class user will make every thin 
class user:
   def __init__(self, name, cycle):
        self.name = name
        self.cycle = cycle
   def close_all_tabs(self):
       with open('webbroswrs.txt', "r") as ins:
           for line in ins:
                if line==" ":
                  continue
                os.system("taskkill /f /im "+line)
   def open_video(self,line):
       webbrowser.open(line, new=1, autoraise=True)
   def display_attentions(self):
           tkinter.messagebox.showinfo( "Attention", "after 2 sec will close every thing")
           time.sleep(2)    
   def start_cycle(self):
       while True:
           file = open('linkes.txt', "r")
           for line in file:
             #if end of file , will call function again  
             if line== " ":
                self.start_cycle() 
             time.sleep(self.cycle)
             self.display_attentions()
             self.close_all_tabs()
             self.open_video(line)
             time.sleep(8*60)
class true2:
    def __init__(self,name,cycle, t):
            name_of_APP="Cycle Break"
            nothind=" "
            self.t=t
            self.name=name
            self.cycle=cycle
            t.minsize(width=500, height=500)
            self.Label1 = tkinter.Label(t,text=nothind)
            self.Label1.grid(row=0, column=0)
            #name of app
            self.Label2 = tkinter.Label(t,fg="black",text=name_of_APP)
            self.Label2.grid(row=1, column=3)
            self.Label2.config(font=("Courier", 30))
            #for space
            self.Label3 = tkinter.Label(t,text=nothind)
            self.Label3.grid(row=2, column=0)
            # description of App
            self.appruels = tkinter.Button(t, text="About App",fg="aqua",bg="black",bd=0,font=3, width=10, command=self.display_rules)
            self.appruels.grid(row=3, column=3)
            #just space
            self.Label4 = tkinter.Label(t,text=nothind)
            self.Label4.grid(row=4, column=0)
            #take data
            self.appruels = tkinter.Button(t, text=name,fg="aqua",bg="black",bd=0,font=3, width=10)
            self.appruels.grid(row=5, column=30)
            #just space
            self.Label4 = tkinter.Label(t,text=nothind)
            self.Label4.grid(row=6, column=30)
            self.appruels = tkinter.Button(t, text=cycle,fg="aqua",bg="black",bd=0,font=3, width=10)
            self.appruels.grid(row=7, column=30)
            u=user(name,cycle)
            u.start_cycle()
    def display_rules(self):
         tkinter.messagebox.showinfo( "define App", "this APP make for you break after cycle will close all web sites and play some vidoes just for fun")        
class tru1:
    
    def __init__(self, t):
            name_of_APP="Cycle Break"
            nothind=" "
            self.t=t
            top.minsize(width=500, height=500)
            self.Label1 = tkinter.Label(top,text=nothind)
            self.Label1.grid(row=0, column=0)
            #name of app
            self.Label2 = tkinter.Label( top,fg="black",text=name_of_APP)
            self.Label2.grid(row=1, column=3)
            self.Label2.config(font=("Courier", 30))
            #for space
            self.Label3 = tkinter.Label(top,text=nothind)
            self.Label3.grid(row=2, column=0)
            # description of App
            self.appruels = tkinter.Button(top, text="About App",fg="aqua",bg="black",bd=0,font=3, width=10, command=self.display_rules)
            self.appruels.grid(row=3, column=3)
            #just space
            self.Label4 = tkinter.Label(top,text=nothind)
            self.Label4.grid(row=4, column=0)
            #take data
            self.Label5 = tkinter.Label( top,fg="black",text="user name")
            self.Label5.config(font=("Courier", 15))
            self.Label5.grid(row=5, column=0)
            self.E1 = tkinter.Entry(top,bd=5,fg="black")
            self.E1.grid(row=6, column=0)
            #just space
            self.Label6 = tkinter.Label(top,text=nothind)
            self.Label6.grid(row=7, column=0)
            #take data
            self.Label7 = tkinter.Label( top,fg="black",text="cycle lenght")
            self.Label7.config(font=("Courier", 15))
            self.Label7.grid(row=8, column=0) 
            self.E2 = tkinter.Entry(top,bd=5,fg="black")
            self.E2.grid(row=9, column=0)
             #just space
            self.Label8 = tkinter.Label(top,text=nothind)
            self.Label8.grid(row=10, column=0)
            self.getmassage = tkinter.Button(top, text="send Data",fg="aqua",bg="black",bd=0,font=3, width=10, command=self.takemaessae)
            self.getmassage.grid(row=11, column=0)
    def takemaessae(self):
            name=self.E1.get()
            cystring=self.E2.get()
            if name==" " :
                 self.some_erreor()
                 self.close()
            elif  cystring.isupper() or cystring.islower():
               
                self.some_erreor()
                self.close()
            else:
                cycle=int(cystring)
                self.close()
                root2 = tkinter.Tk()
                u=true2(name,cycle,root2)
    def some_erreor(self):
        tkinter.messagebox.showinfo( "ERRoR", "You don't enetr you name msh hnhzer bka")
    def close(self):
       top.destroy()
    def display_rules(self):
         tkinter.messagebox.showinfo( "define App", "this APP make for you break after cycle will close all web sites and play some vidoes just for fun")
class tru2:
    def __init__(self, t):
            self.t=t
            root2.minsize(width=666, height=666)
#tricket one          
top = tkinter.Tk()
t1=tru1(top)

########################################
top.mainloop()
             























