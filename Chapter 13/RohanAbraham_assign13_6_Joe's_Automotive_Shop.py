#Rohan Abraham
#Program has a user select service options and then will display the total

import tkinter

class JoesAutomotiveGUI:
    def __init__(self):
        #Create the main window
        self.main_window = tkinter.Tk()

        #Create two frames
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #Create IntVar objects
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        #Set the intVar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        #Create the Checkbuttons command names confusingasdfasdf
        self.cb1 = tkinter.Checkbutton(self.top_frame, text = 'Oil Change', onvalue=30,
                                       offvalue = 0,variable = self.cb_var1, command = self.oil_change)
        
        self.cb2 = tkinter.Checkbutton(self.top_frame, text = 'Lube Job', onvalue=20, 
                                       offvalue = 0, variable = self.cb_var2, command = self.lube_job)
        
        self.cb3 = tkinter.Checkbutton(self.top_frame, text = 'Radiator Flush', onvalue=40, 
                                       offvalue = 0, variable = self.cb_var3, command = self.radiator_flush)
        
        self.cb4 = tkinter.Checkbutton(self.top_frame, text = 'Transmission Flush', onvalue=100, 
                                       offvalue=0, variable = self.cb_var4, command = self.transmission_flush)
        
        self.cb5 = tkinter.Checkbutton(self.top_frame, text = 'Inspection', onvalue=35, 
                                       offvalue=0, variable = self.cb_var5, command = self.inspection)
        
        self.cb6 = tkinter.Checkbutton(self.top_frame, text = 'Muffler Replacement', onvalue=200, 
                                       offvalue=0, variable = self.cb_var6, command = self.muffler_replacement)
        
        self.cb7 = tkinter.Checkbutton(self.top_frame, text = 'Tire Rotation', onvalue=20, 
                                       offvalue= 0, variable = self.cb_var7, command = self.tire_rotation)


        #Pack the checkbuttons and the top label
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        #Create labels and initialize total to 0
        self.bottom_label = tkinter.Label(self.bottom_frame, text='Total Charge:')
        self.total = tkinter.StringVar()
        self.total.set('0.00')
        self.total_label = tkinter.Label(self.bottom_frame, textvariable=self.total)

        #Pack the frames and labels
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.bottom_label.pack()
        self.total_label.pack()

        #Start the main loop
        tkinter.mainloop()

    #Function adds to total if oil change used
    #All functions have the onvalue set to the price of procedure
    def oil_change(self):
        total = float(self.total.get())
        if self.cb_var1.get()==30:
            self.total.set(total+30)
        else:
            self.total.set(total-30)
        
        
    #Function adds to total if lube job used
    def lube_job(self):
        total = float(self.total.get())
        if self.cb_var2.get()==20:
            self.total.set(total+20)
        else:
            self.total.set(total-20)
        
    #Function adds to total if radiator flush used
    def radiator_flush(self):
        total = float(self.total.get())
        if self.cb_var3.get()==40:
            self.total.set(total+40)
        else:
            self.total.set(total-40)
        
    #Function adds to total if transmission flush used
    def transmission_flush(self):
        total = float(self.total.get())
        if self.cb_var4.get()==100:
            self.total.set(total+100)
        else:
            self.total.set(total-100)
        
    #Function adds to total if inspection used
    def inspection(self):
        total = float(self.total.get())
        if self.cb_var5.get()==35:
            self.total.set(total+35)
        else:
            self.total.set(total-35)
        
    #Function adds to total if muffler replaced
    def muffler_replacement(self):
        total = float(self.total.get())
        if self.cb_var6.get()==200:
            self.total.set(total+200)
        else:
            self.total.set(total-200)
        
    #Function adds to total if tires rotated
    def tire_rotation(self):
        total = float(self.total.get())
        if self.cb_var7.get()==20:
            self.total.set(total+20)
        else:
            self.total.set(total-20)
        
#Create an instance
my_gui = JoesAutomotiveGUI()
        

























        
