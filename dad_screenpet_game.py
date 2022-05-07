# tkinter is a standard python library to help you make interactive applications with windows
from tkinter import HIDDEN, NORMAL, Tk, Canvas

# a function for determining what colour the eyes are currently and switching to close blink or open
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')   # itemcget returns what the current fill colour in th eye is
    new_color = c.body_color if current_color == 'white' else 'white'  # sets the next color to the opposite of the answer
    current_state = c.itemcget(pupil_left, 'state')                    # checks if the pupils are hidden of visible
    new_state = NORMAL if current_state == HIDDEN else HIDDEN          # and like fill color sets the opposite in new_state
    c.itemconfigure(pupil_left, state=new_state)                       # these lines then apply the changes to left and right eye objects
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()                    # eyes will be open when we call this first, this closes them
    root.after(250, toggle_eyes)     # this command tells the root window to wait 250 ms (1/4 of a second) then open eyes again
    root.after(3000, blink)          # this asks the root window to call the blink function again after 3000milliseconds = 3s

root = Tk() # this generates the main root window, with a small default size at this point

c = Canvas(root, width=400, height=400)              # generates a canvas object in root window for you to draw on size 400x400 pixels
c.configure(bg='dark blue', highlightthickness=0)    # specifies a dark blue background colour

c.body_color = 'SkyBlue1'  # creates this variable in the canvas object so we don't have to type SkyBlue1 continually - this is the foreground color

# the following commands use tkinter's shape drawing commands to draw each part of the pet in turn
# where there are numbers these are coordinate pairs on screen where 0,0 is the TOP LEFT of the root window
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill= c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill= c.body_color)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)  # a curved line 1st pt start 2nd pt mid 3rd pt end


c.pack()                                             # places the canvas on the root window

root.after(1000, blink) # is requesting the root window to do the first screen pet eye blink after 1 s (1000 milliseconds)
root.mainloop()                                      # and this places the root window in to "listening" mode waitng for events/interactions
