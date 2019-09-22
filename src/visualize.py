import Tkinter as tk
import Image, ImageTk,ImageDraw
import math
import random as rn
import io
import os
import numpy as np


FilePath='/c/'
Tcols=0
C=R=1
# sizeP=0,0
# # sizeP=500/N,500/N
class GameBoard(tk.Frame):
    def __init__(self, parent, rows=R, columns=C, size=64, color1="grey", color2="white"):
        '''size is the size of a square, in pixels'''
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    #Add piece
    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    #place pieace to canvas
    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    #refresh canvas
    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                if ((np.max(self.columns))%2!=0 and col==(np.max(self.columns)-1)):
                	lol=True
                else:
                	color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
        # save canvas
        self.save()
        # self.canvas.pack()
        # self.canvas.postscript(file="file_name.ps", colormode='color')

    #function that saves images
    def save(self):
        ps = self.canvas.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        img_name= str(find_available_name(FilePath))+'_TColisions_'+str(Tcols)+'.jpg'
        img.save(FilePath+img_name)

def ShowQueens(grid):
    N=len(grid)
    C=N
    R=N
    sizeP=500/N,500/N

    root = tk.Toplevel()
    board = GameBoard(root,R,C)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)

    imO = Image.open('QBlack.jpg')
    imO.thumbnail(sizeP, Image.ANTIALIAS)
    playerO = ImageTk.PhotoImage(imO)
    for i in grid:
        if((i+grid[i])% 2 == 0):
            board.addpiece("player"+str(i), playerO, i,grid[i])

    imE = Image.open('QWhite.jpg')
    imE.thumbnail(sizeP, Image.ANTIALIAS)
    playerE = ImageTk.PhotoImage(imE)
    for i in grid:
        if((i+grid[i])% 2 != 0):
            board.addpiece("player"+str(i), playerE, i,grid[i])


    # root.mainloop()
    root.update()
    root.quit()

#Find available name for storing image
#image's name format : #_Tcolisions_#*.jpg  where # serial number of image
#                                                 #* number of colisions
def find_available_name(directory):
    _list=os.listdir(directory)
    # print(_list)
    Names=[]
    for i in _list: Names.append(int(os.path.basename(i).split('_')[0]))
    try:
        fn=np.max(Names)
    except:
        fn=0
    return (fn+1)


# N=8
# ShowQueens([0,2,4,6,1,3,5,7])
# ShowQueens([0,2,3,1,4,6,5,8,7,9])
# ShowQueens([0,1,3,2,4,6,5,8,7,9])
# print(find_available_name("Images/SA/5-Queens/"))



# if __name__ == "__main__":
#     grid=[0,2,4,6,1,3,5,7]

#     root = tk.Tk()

#     board = GameBoard(root)
#     board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
#     im = Image.open('bq.jpg')
#     im.thumbnail(sizeP, Image.ANTIALIAS)
#     player = ImageTk.PhotoImage(im)
#     for i in grid:
#         board.addpiece("player"+str(i), player, i,grid[i])

#     # root.mainloop()
#     root.update()
#     root.quit()
