#Rohan Abraham
#Program acts as a Latin to English translator

import tkinter

class LatinToEnglishGUI:
    def __init__(self):
        #Create the main window
        self.main_window = tkinter.Tk()

        #Create three frames
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #Create and pack labels
        self.greeting_label = tkinter.Label(self.top_frame, text='Click a button for a translation  ')
        self.greeting_label.pack()
        self.translation_label = tkinter.Label(self.bottom_frame, 
                                           text='Translation:')
        self.translation_label.pack(side='left')
        self.translation = tkinter.StringVar()
        self.translated = tkinter.Label(self.bottom_frame, 
                                     textvariable=self.translation)
        self.translated.pack()

        #Create the three buttons in the middle frame
        self.b1 = tkinter.Button(self.middle_frame, 
                                          text='sinister', command=self.translate_sinister)
        self.b2 = tkinter.Button(self.middle_frame, 
                                          text='dexter', command=self.translate_dexter)    
        self.b3 = tkinter.Button(self.middle_frame, 
                                          text='medium', command=self.translate_medium)

        #Pack the buttons
        self.b1.pack(side='left')
        self.b2.pack(side='left')
        self.b3.pack(side='left')
        
       

        #Pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #Enter the tkinter main loop
        tkinter.mainloop()

    #Function sets the translation string variable to left
    #When button is clicked the translation will be displayed at the bottom
    def translate_sinister(self):
        self.translation.set('left')
        
    #Function sets the translation string variable to right
    def translate_dexter(self):
        self.translation.set('right')
        
    #Function sets the translation string variable to center
    def translate_medium(self):
        self.translation.set('center')

#Create an instance
my_gui = LatinToEnglishGUI()



































        




























                                   
