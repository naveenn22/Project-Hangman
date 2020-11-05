from tkinter import *
def draw(canvas, width, height):

    # create_line(x1, y1, x2, y2) draws a line from (x1, y1) to (x2, y2)
    canvas.create_rectangle(170,  550, 790, 560, fill="orange", width=2)
    canvas.create_rectangle(250,  100, 260, 550, fill="orange", width=2)
    canvas.create_rectangle(260,  120, 580, 130, fill="orange", width=2)
    canvas.create_line(530, 130, 530, 200, width=3)

   
# def face(canvas, width, height):
    

    canvas.create_oval(500, 200, 560, 260, width=2)
    canvas.create_line(517, 220, 519, 222, width=3)     #left eye
    canvas.create_line(540, 220, 542, 222, width=3)     #right eye
    canvas.create_line(529, 230, 529, 235, width=3)     #nose
    canvas.create_line(521, 245, 538, 245, width=3)     # mouth
    canvas.create_line(530, 260, 530, 435, width=3)     #body line
    canvas.create_line(470, 320, 530, 290, width=2)     #left hand
    canvas.create_line(590, 320, 530, 290, width=2)     #right hand
    canvas.create_line(470, 475, 530, 435, width=2)     #left leg
    canvas.create_line(590, 475, 530, 435, width=2)

def runDraw(width=300, height=300):
    root=Tk()
    canvas=Canvas(root,width=width,height=height)
    canvas.pack()
    draw(canvas,width,height)
    root.mainloop()
    print("bye")

runDraw(1000,1000)

