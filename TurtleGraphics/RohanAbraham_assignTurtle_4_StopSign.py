#Rohan Abraham
#Program draws a stop sign
import tkinter
import tkinter.font

class MyGUI:
    def __init__(self):
        #Create the main window
        self.main_window = tkinter.Tk()

        #Create the canvas widget
        self.canvas = tkinter.Canvas(self.main_window,  width = 160, height = 160)

        #Draw the outer shell
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100, 100,
                                   140, 60, 140, 20, 100, 20, 60, fill = "#FF0000")
        #Create a font object
        myfont = tkinter.font.Font(family='Helvetica', size=24, weight='bold')

        #Display the text
        self.canvas.create_text(82, 82,  text='STOP', font=myfont, fill = "#ffffff")
        
        #Pack the canvas
        self.canvas.pack()

        #Start the main loop
        tkinter.mainloop()

my_gui = MyGUI()
