from  indexproblems import *

class Sudoku():


    def __init__(self, matrix_):

        # matrix_ contains numbers from 1 to 9 and " "
        # we  want to replace " "  by appropriate numbers

        self.matrix9by9=matrix_
        self.number_of_boxes_determined=0
        self.matrix9by9possibilities=[[{1, 2, 3, 4, 5, 6, 7, 8, 9} for j in range(9)] for i in range(9)]
        self.boolean_matrix=[[False for i in range(9)] for j in range(9)]
        # when we find a number for  any void entry in the sudoku, we make some changes in
        # matrix9by9possibilities. If these changes are done, then make corresponding
        # entry of the boolean_matrix TRUE. By this controller we avoid repetitions.
        self.show_must_go_on=True
        self.any_contradiction=False


        for i in range(9):
            for j in range(9):
                if self.matrix9by9[i][j]!=" ":
                    self.change_sudoku_matrix(i,j, self.matrix9by9[i][j])



    def delete_a_number_from_the_possibility_set(self, number, a,n):
        """""
        number=1,2...,9 which number will be deleted from the possibility set
        a=1,2,3:   1 means from columns
                   2 means from rows
                   3 means from 3by3 matrices 
        n=0,1,...,8  from which columns, which rows, or which 3by3 matrices
        """""
        if a==1:


            for i,j in list_of_columns[n]:
                self.matrix9by9possibilities[i][j].discard(number)

        elif a==2:

            for i,j in list_of_rows[n]:
                self.matrix9by9possibilities[i][j].discard(number)


        else:

            for i,j in list_of_three_by_three_matrices[n]:
                self.matrix9by9possibilities[i][j].discard(number)



    def change_sudoku_matrix(self, i,j, number):

        self.matrix9by9[i][j]=number
        self.number_of_boxes_determined+=1
        self.delete_a_number_from_the_possibility_set(number,1,j)
        self.delete_a_number_from_the_possibility_set(number,2,i)
        self.delete_a_number_from_the_possibility_set(number,3,(i//3)*3+(j//3))
        self.matrix9by9possibilities[i][j]={number}
        self.boolean_matrix[i][j]=True

    def controller_1(self):

        for i in range(9):
            for j in range(9):

                if not (self.boolean_matrix[i][j]) and len(self.matrix9by9possibilities[i][j])==1:
                    self.change_sudoku_matrix(i,j,list(self.matrix9by9possibilities[i][j])[0])
                    self.show_must_go_on=True
                    #print(i,j,list(self.matrix9by9possibilities[i][j])[0])



    def controller_2(self):


        for number in range(1,10):

            for column in list_of_columns:
                counter=0
                list_of_entries = []
                for i,j in column:
                    if number in self.matrix9by9possibilities[i][j]:
                        counter+=1
                        list_of_entries.append((i,j))
                if counter==1 and not self.boolean_matrix[list_of_entries[0][0]][list_of_entries[0][1]]:
                    self.change_sudoku_matrix(list_of_entries[0][0],list_of_entries[0][1],number)
                    #print(list_of_entries, number)

            for row in list_of_rows:
                counter=0
                list_of_entries = []
                for i,j in row:
                    if number in self.matrix9by9possibilities[i][j]:
                        counter+=1
                        list_of_entries.append((i,j))
                if counter==1 and not self.boolean_matrix[list_of_entries[0][0]][list_of_entries[0][1]]:
                    self.change_sudoku_matrix(list_of_entries[0][0],list_of_entries[0][1],number)
                    #print(list_of_entries, number)




            for three_by_three_matrix in list_of_three_by_three_matrices:
                counter=0  # how many entry of possibility matrix of 3 by 3 matrix does contain the number considered?
                list_of_entries=[]  # list of indices of such enntries in the three by three matrix considered
                for i,j in three_by_three_matrix:
                    if number in self.matrix9by9possibilities[i][j]:
                        counter+=1
                        list_of_entries.append((i,j))

                if counter==1 and not self.boolean_matrix[list_of_entries[0][0]][list_of_entries[0][1]]:
                    self.change_sudoku_matrix(list_of_entries[0][0],list_of_entries[0][1],number)
                    #print(list_of_entries, number)

                if counter==2:
                    if list_of_entries[0][0]==list_of_entries[1][0]:
                        self.delete_a_number_from_the_possibility_set(number, 2, list_of_entries[0][0])
                        self.matrix9by9possibilities[list_of_entries[0][0]][list_of_entries[0][1]].add(number)
                        self.matrix9by9possibilities[list_of_entries[1][0]][list_of_entries[1][1]].add(number)
                        self.show_must_go_on = True
                        #print(list_of_entries, number)

                    if list_of_entries[0][1]==list_of_entries[1][1]:
                        self.delete_a_number_from_the_possibility_set(number, 1, list_of_entries[0][1])
                        self.matrix9by9possibilities[list_of_entries[0][0]][list_of_entries[0][1]].add(number)
                        self.matrix9by9possibilities[list_of_entries[1][0]][list_of_entries[1][1]].add(number)
                        self.show_must_go_on = True
                        #print(list_of_entries, number)

                if counter == 3:
                    if list_of_entries[0][0] == list_of_entries[1][0]==list_of_entries[2][0]:
                        self.delete_a_number_from_the_possibility_set(number, 2, list_of_entries[0][0])
                        self.matrix9by9possibilities[list_of_entries[0][0]][list_of_entries[0][1]].add(number)
                        self.matrix9by9possibilities[list_of_entries[1][0]][list_of_entries[1][1]].add(number)
                        self.matrix9by9possibilities[list_of_entries[2][0]][list_of_entries[2][1]].add(number)
                        self.show_must_go_on = True
                        #print(list_of_entries, number)

                    if list_of_entries[0][1] == list_of_entries[1][1]==list_of_entries[2][1]:
                        self.delete_a_number_from_the_possibility_set(number, 1, list_of_entries[0][1])
                        self.matrix9by9possibilities[list_of_entries[0][0]][list_of_entries[0][1]].add(number)
                        self.matrix9by9possibilities[list_of_entries[1][0]][list_of_entries[1][1]].add(number)
                        self.matrix9by9possibilities[list_of_entries[2][0]][list_of_entries[2][1]].add(number)
                        self.show_must_go_on = True
                        #print(list_of_entries, number)

    def controller_3(self):
        """""
        a,b are numbers from 1 to 9, if there  are just two boxes for a and b in a column or  a row or a 3 by 3 matrix, 
        and two boxes are the same for a,b, then delete other possibilities different than a and b from these two boxes
        """""

        for num1 in range(1,10):
            for num2 in range(num1+1, 10):
                for column in list_of_columns:
                    list_num1 = list()
                    list_num2 = list()

                    for i, j in column:
                        if num1 in self.matrix9by9possibilities[i][j]:
                            list_num1.append((i, j))
                        if num2 in self.matrix9by9possibilities[i][j]:
                            list_num2.append((i, j))
                    if set(list_num1) == set(list_num2):
                        if len(list_num1) == 2:
                            self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]] = {num1, num2}
                            self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]] = {num1, num2}
                            self.show_must_go_on = True
                            #print(list_num1,num1,num2)
                        if len(list_num1) == 3:
                            a = self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]].intersection(
                                self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]]).intersection(
                                self.matrix9by9possibilities[list_num1[2][0]][list_num1[2][1]])
                            for b in list(a.difference({num1,num2})):
                                count=0
                                for i,j in column:
                                    if b in self.matrix9by9possibilities[i][j]:
                                        count+=1
                                if count==3:
                                    # print(list_num1,a)
                                    self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]] = {num1,num2,b}
                                    self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]] = {num1,num2,b}
                                    self.matrix9by9possibilities[list_num1[2][0]][list_num1[2][1]] = {num1,num2,b}
                                    self.show_must_go_on = True







                for row in list_of_rows:
                    list_num1 = list()
                    list_num2 = list()

                    for i, j in row:
                        if num1 in self.matrix9by9possibilities[i][j]:
                            list_num1.append((i, j))
                        if num2 in self.matrix9by9possibilities[i][j]:
                            list_num2.append((i, j))
                    if set(list_num1) == set(list_num2):
                        if len(list_num1) == 2:
                            self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]] = {num1, num2}
                            self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]] = {num1, num2}
                            self.show_must_go_on = True
                            #print(list_num1,num1,num2)

                        if len(list_num1) == 3:
                            a = self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]].intersection(
                                self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]]).intersection(
                                self.matrix9by9possibilities[list_num1[2][0]][list_num1[2][1]])
                            for b in list(a.difference({num1,num2})):
                                count=0
                                for i,j in row:
                                    if b in self.matrix9by9possibilities[i][j]:
                                        count+=1
                                if count==3:
                                    # print(list_num1,a)
                                    self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]] = {num1,num2,b}
                                    self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]] = {num1,num2,b}
                                    self.matrix9by9possibilities[list_num1[2][0]][list_num1[2][1]] = {num1,num2,b}
                                    self.show_must_go_on = True

                for threebythreematrix in list_of_three_by_three_matrices:
                    list_num1 = list()
                    list_num2 = list()

                    for i, j in threebythreematrix:
                        if num1 in self.matrix9by9possibilities[i][j]:
                            list_num1.append((i, j))
                        if num2 in self.matrix9by9possibilities[i][j]:
                            list_num2.append((i, j))
                    if set(list_num1) == set(list_num2):
                        if len(list_num1) == 2:
                            #print(list_num1,num1,num2)

                            self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]] = {num1,num2}
                            self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]] = {num1,num2}
                            self.show_must_go_on = True
                        if len(list_num1) == 3:
                            a = self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]].intersection(
                                self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]]).intersection(
                                self.matrix9by9possibilities[list_num1[2][0]][list_num1[2][1]])
                            for b in list(a.difference({num1,num2})):
                                count=0
                                for i,j in threebythreematrix:
                                    if b in self.matrix9by9possibilities[i][j]:
                                        count+=1
                                if count==3:
                                    # print(list_num1,a)
                                    self.matrix9by9possibilities[list_num1[0][0]][list_num1[0][1]] = {num1,num2,b}
                                    self.matrix9by9possibilities[list_num1[1][0]][list_num1[1][1]] = {num1,num2,b}
                                    self.matrix9by9possibilities[list_num1[2][0]][list_num1[2][1]] = {num1,num2,b}
                                    self.show_must_go_on = True




    def catch_contradictions(self):

        for column in list_of_columns:

            set_=set()
            for i, j in column:
                set_=set_.union(self.matrix9by9possibilities[i][j])

            if set_!={1,2,3,4,5,6,7,8,9}:
                self.any_contradiction = True
                return True

        for row in list_of_rows:

            set_=set()
            for i, j in row:
                set_=set_.union(self.matrix9by9possibilities[i][j])

            if set_!={1,2,3,4,5,6,7,8,9}:
                self.any_contradiction = True
                return True

        for threebythreematrix in list_of_three_by_three_matrices:

            set_=set()
            for i, j in threebythreematrix:
                set_=set_.union(self.matrix9by9possibilities[i][j])

            if set_!={1,2,3,4,5,6,7,8,9}:
                self.any_contradiction = True
                return True

        for col in list_of_columns:
            for i,j in col:
                for ind in range(i+1,9):
                    if self.matrix9by9[i][j]==self.matrix9by9[ind][j] and self.matrix9by9[i][j]!=" ":
                        self.any_contradiction = True
                        return True

        for row in list_of_rows:
            for i, j in row:
                for ind in range(j + 1, 9):
                    if self.matrix9by9[i][j] == self.matrix9by9[i][ind] and self.matrix9by9[i][j] != " ":
                        self.any_contradiction = True
                        return True

        for threebythreematrix in list_of_three_by_three_matrices:
            for i, j in threebythreematrix:
                for u, v in threebythreematrix:
                    if (i,j)==(u,v):
                        continue
                    else:
                        if self.matrix9by9[i][j] == self.matrix9by9[u][v] and self.matrix9by9[i][j] != " ":
                            self.any_contradiction = True
                            return True



    def solver(self):

        i=0
        #while(self.show_must_go_on and self.number_of_boxes_determined<81):
        while(i<20):
            self.show_must_go_on=False
            #self.print_sudoku_possibilities()
            #print(self.matrix9by9possibilities[6][4])
            self.controller_1()
            #self.print_sudoku_possibilities()
            #print(self.matrix9by9possibilities[6][4])
            self.controller_2()


            self.controller_3()

            if self.catch_contradictions():
                break
            i+=1

    def choose_undetermined_entry(self):

        for i in range(9):
            for j in range(9):
                if self.matrix9by9[i][j]==" ":
                    return (i,j)

    def print_sudoku(self,sudoku_buttons):
        for i in range(9):
            for j in range(9):
                sudoku_buttons[i][j]["text"] = self.matrix9by9[i][j]












