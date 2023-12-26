from tkinter import *
 
 
class resultsDisplay:
    def __init__(self, root):
        height = root.winfo_screenheight() - 400
        width = root.winfo_screenwidth() - 700
        frame = LabelFrame(root, text="Numerical Results")
        frame.place(x= width, y=height - 45)
        total_rows = height // 50 + 7
        total_columns = len(lst[0])

        #add so that the boxes in a column just fit the biggest entry and not less and not more
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(frame, width=15, fg='black',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                if (i < len(lst) and j < len(lst[0])):
                    self.e.insert(END, lst[i][j])
 
# example data
lst = [('Reverb',4 ,'',19),
       ('Power',4.4444,'',18),
       ('Decibel',4 + 3,'',20),
       ('Hertz','', 3, 21),
       ('sound','number','',21)]
