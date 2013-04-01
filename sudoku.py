import random

#012
#345
#678
#0-8
#0-8
#sq0 would be r0,1,2 and col0,1,3
#sq1 would be r0,1,2 and col3,4,5
global columns 
columns=[[]]*9
global rows
rows  =[[]]
global board
board =[]


def square():
    nums = [1,2,3,4,5,6,7,8,9]
    i,j=0,0
    sqrow, sqcol, square =[],[],[]
    posrow, poscol =[],[]
    numsquare = len(board)
    if numsquare==0:
        while i<3:
            while j<3:
                sqrow.append(random.choice(nums))
                nums.remove(sqrow[j])
                j+=1
            square.append(sqrow)
            sqrow=[]
            i+=1
            j=0
    i, j =0,0
    if numsquare <3 and numsquare>0:
        while i<3:
            while j<3:
                if numsquare==1:
                    check_row_col(i,j+3,sqrow,posrow)
                if numsquare == 2:
                    check_row_col(i,j+6,sqrow,posrow)
                j+=1    

            square.append(sqrow)
            sqrow=[]
            j=0
            i+=1
            
    add_squarecs(square)
    return square

def check_row_col(i,j, sqrow, posrow):
    poscol =[]#cant make them empty everytime poscol is almost always empty
    posrow = []
    nums = [1,2,3,4,5,6,7,8,9]
    posrow+=(rows[i])
    poscol+=(columns[j])
    print (posrow)
    for e in posrow:
        if e in nums:
            nums.remove(e)
    #for e in poscol:
    #    if e in nums:
    #        nums.remove(e)
    sqrow.append(random.choice(nums))

        
def add_squarecs(square):
    board.append(square)
    numsquare=len(board)
    add_columns(square, board.index(square))
    add_rows(square, board.index(square))
    
def add_columns(square, index):
    i=0
    x=0
    for r in square:
        if index==1 or index == 4 or index == 7:
            i=3
        if index==2 or index==5 or index==8:
            i=6
        while x<3:
           # columns.append([]) i dont get why this appends everything element in the square
           #print (columns[i])
           columns[i].append(r[i])
           x+=1
           i+=1
        x=0
        i=0
def add_rows(square, index):
    i=0
    
    if index<3:

        for e in square:
            if len(rows) < 8:
                rows.append([])
            rows[i].append(e)
            

            #rows.append([])
            i+=1
    if index <6 and index>2:
        i=3
        for e in square:
            if len(rows) < 8:
                rows.append([])
            rows[i] += e

            #rows.append([])
            i+=1
            
    if index > 5:
        i=6
        for e in square:
            if len(rows) < 8:
                rows.append([])
            rows[i] += e
            #rows.append([])
            i+=1
            
    #rows.pop()

square1 = square()
square2 = square()
#square3 =square()
print (square1)
print (square2)
#print (square3)
print (rows)
#print ([[]]*9)
