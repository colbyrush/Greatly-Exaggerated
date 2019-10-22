from tkinter import *


# Creating our class, Window, and inheriting from the Frame class. Frame is a class from the tkinter module that has everything we need to create the GUI.
class Window(Frame):

    # Define what happens when the program first runs, which is what __init__ is. Init is the big bang
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class for future reasons
        Frame.__init__(self, master)   

        # reference to the master widget, which is the window through which to see the big bang                
        self.master = master

        # runs the function right beneath now that the big bang is finished and watchable
        self.init_window()

    # all the things that happen when the window is first built. Init_window is the creation of the earth
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("CoobyDM D&D5e Encounter Tracker Alpha")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # create initial buttons

        #create new combatant group
        createNewCombatantBtn = Button(self, text="Create New Combatant(s)",command=self.createNewCombatant)

        #create new encounter i.e. reset window
        createNewEncounterBtn = Button(self, text="Create New Encounter",command=self.client_exit)

        # placing the buttons
        createNewCombatantBtn.place(x=0,y=50)
        createNewEncounterBtn.place(x=0,y=0)      

    # exit window
    def client_exit(self):
        exit()
    
# all the functions to keep track of data for encounter
class combatTracking(Frame):
    exit()




# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  