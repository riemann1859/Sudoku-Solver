
import copy
from tkinter import *
import tkinter.messagebox
from sudokuclass import Sudoku




def sudoku_solver(sudoku):

   global list_of_sudokus
   global number_of_solutions
   if sudoku.any_contradiction or sudoku.number_of_boxes_determined==81:
      if sudoku.number_of_boxes_determined==81:
         number_of_solutions+=1
   else:
      for num in sudoku.matrix9by9possibilities[sudoku.choose_undetermined_entry()[0]][sudoku.choose_undetermined_entry()[1]]:
         list_of_sudokus.append(copy.deepcopy(sudoku))
         list_of_sudokus[len(list_of_sudokus)-1].change_sudoku_matrix(sudoku.choose_undetermined_entry()[0],sudoku.choose_undetermined_entry()[1],num)
         list_of_sudokus[len(list_of_sudokus) - 1].solver()
         sudoku_solver(list_of_sudokus[len(list_of_sudokus)-1])


def callback(i, j):
    global active_box
    active_box = [i,j]

def delete():
    sudoku_buttons[active_box[0]][active_box[1]]["text"] = " "
    sudoku_entries[active_box[0]][active_box[1]] = " "




def fill_the_box(i):
    sudoku_buttons[active_box[0]][active_box[1]]["text"] = i
    sudoku_entries[active_box[0]][active_box[1]] = i

def reset():
    global list_of_sudokus
    global number_of_solutions
    global sudoku_entries
    global active_box
    number_of_solutions = 0
    list_of_sudokus = []
    sudoku_entries = [[" " for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            sudoku_buttons[i][j]["text"] =" "

    active_box = None

def solve_sudoku():
    b = Sudoku(sudoku_entries)
    b.solver()

    list_of_sudokus.append(b)
    #import pdb
    #pdb.set_trace()
    sudoku_solver(b)
    if number_of_solutions==0:
        tkinter.messagebox.showinfo("Warning!", "No solution", )
    else:
        tkinter.messagebox.showinfo("Warning!", "We have found {x} solutions!".format(x=number_of_solutions))
        if number_of_solutions==1:
            answer_1 = tkinter.messagebox.askyesno("Question", "Would you like to see the solution?")
            if  answer_1:
                for s_ in list_of_sudokus:
                    if not s_.any_contradiction and s_.number_of_boxes_determined==81:
                        s_.print_sudoku(sudoku_buttons)
            else:
                root.destroy()
        if number_of_solutions>1:
            answer_1 = tkinter.messagebox.askyesno("Question", "Would you like to see one of possible solutions?")
            if  answer_1:
                for s_ in list_of_sudokus:
                    if not s_.any_contradiction and s_.number_of_boxes_determined==81:
                        s_.print_sudoku(sudoku_buttons)

    answer_2 = tkinter.messagebox.askyesno("Question", "Would you like to enter a new sudoku problem?")
    if answer_2:
        reset()
    else:
        root.destroy()

root = Tk()

root.title("Sudoku Solver")
number_of_solutions = 0
list_of_sudokus = []
active_box=None

frame0=Frame(root, height=20, bd=5)
frame0.pack()

frame1=Frame(root, bd=5)
frame1.pack()
sudoku_entries = [[" " for j in range(9)] for i in range(9)]
sudoku_buttons = [[] for i in range(9)]

for i in range(9):
    for j in range(9):
        sudoku_buttons[i].append(Button(frame1, width=5, height=3, fg="blue", relief=RIDGE, bd=3, font=('Times 12 bold'), text=" ",
                                       command=lambda i=i, j=j: callback(i, j)))
        # i=i, j=j is very important trick!!! remove this part execute the code you see the difference
        sudoku_buttons[i][j].grid(row=i, column=j)

frame2=Frame(root, height=10, bd=5)
frame2.pack()
frame3=Frame(root, bd=5)
frame3.pack()
numberbuttons = []
numberbuttons.append(Button(frame3, width=6, borderwidth=6, text="DELETE", fg="blue", command=delete))
numberbuttons[0].grid(row=9, column=0)

numberbuttons.append(Button(frame3, width=4, borderwidth=6, relief=FLAT, fg="blue"))
numberbuttons[1].grid(row=9, column=1)

for i in range(9):
    numberbuttons.append(Button(frame3, width=4, borderwidth=6, text="{x}".format(x=i + 1), fg="blue",
                                command=lambda i=i + 1: fill_the_box(i)))
    numberbuttons[i+2].grid(row=9, column=i+2)

frame4=Frame(root, height=10, bd=5)
frame4.pack()
solve_button=Button(frame4, width=6, borderwidth=6, text="SOLVE", fg="blue", command=solve_sudoku)
solve_button.pack()




root.mainloop()