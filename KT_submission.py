'''Try to create a working game for the Demo'''

#_______________IMPORTS________________#
import sys
import stdio
import stdarray
import stddraw

#_______________ARGUMENTS & VALIDATION______________#
if len(sys.argv)!=3+1:
    if len(sys.argv)<4:
        stdio.writeln("ERROR: Too few arguments")
        sys.exit()
    else:
        stdio.writeln("ERROR: Too many arguments")
        sys.exit()
        

row_max = int(sys.argv[1])
col_max = int(sys.argv[2])
gui_mode = int(sys.argv[3])

if row_max not in [8,9,10]:
    stdio.writeln("ERROR: Illegal argument")
    sys.exit()
if col_max not in [8,9,10]:
    stdio.writeln("ERROR: Illegal argument")
    sys.exit()
if gui_mode not in [0,1]:
    stdio.writeln("ERROR: Illegal argument")

#_____________GLOBAL VARIABLES_____________#
board = stdarray.create2D(row_max, col_max, "  ")
count_light = 0
count_dark = 0
turn = "light"
#____________PRINT BOARD____________#
def print_board(row_max, col_max):
    global board
    
    #this is for the column numbers
    stdio.write(" ")
    for k in range(col_max):
      stdio.write(f"  {k}")
    stdio.writeln()
    
    #this is for the first +--+
    stdio.write("  ")
    for k in range(col_max):
        stdio.write("+")
        stdio.write("--")
    stdio.writeln("+")
    
    for iv in range(row_max-1,-1,-1):
        stdio.write(iv)
        stdio.write(" ")
        for block in board[iv]:
            stdio.write("|")
            stdio.write(f"{block}")
        stdio.writeln("|")
        
        stdio.write("  ")
        for ii in range(col_max):
            stdio.write("+")
            stdio.write("--")
        stdio.writeln("+")

#___________READ BOARD___________#
def read_board():
    global board
    
    
    try:
        stop = False
        while stop==False:
            user_input = stdio.readLine()
            charecters = user_input.split()
            
            if "#" in charecters:
                stop=True
                break
            elif charecters[0]=="x":
                row = int(charecters[1])
                col = int(charecters[2])
            else:
                row = int(charecters[2])
                col = int(charecters[3])
            
            if col>=col_max:
                stdio.writeln(f"ERROR: Field {row} {col} not on board")
                sys.exit()
            if row>=row_max:
                stdio.writeln(f"ERROR: Field {row} {col} not on board")
                sys.exit()
            if charecters[1] not in ["A", "a", "b", "B", "c", "C", "d", "D", "x", "s","1","2"]:
                stdio.writeln(f"ERROR: Invalid piece type {charecters[1]}")
                sys.exit()
            if charecters[0]=="l":
                charecters[1]=charecters[1].lower()
            elif charecters[0]=="d":
                charecters[1]=charecters[1].upper()
            else:
                pass
            #create if statements for the other pieces/occurances
            if charecters[0]=="s":
                if col in range(3,len(board[row])-4) and row in range(3, len(board[col])-4):
                    stdio.writeln("ERROR: Sink in the wrong position")
                    sys.exit()
                elif board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    # stdio.writeln("ERROR: Sink in the wrong position")
                    # sys.exit()
                elif charecters[1]=="1":
                    board[row][col]=" s"
                elif charecters[1]=="2":
                    board[row][col]=" s"#bottom left corner
                    board[row][col+1]=" s"
                    board[row+1][col]=" s"
                    board[row+1][col+1]=" s"
                else:
                    stdio.writeln(f"ERROR: Invalid piece type {charecters[0]}")
            elif charecters[1]=="a":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                    # stdio.writeln("ERROR: Piece in the wrong position")
                    # sys.exit()
                else:
                    board[row][col]=" a"
            elif charecters[1]=="b":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                else:
                    board[row][col]=" b"
            elif charecters[1]=="c":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                else:
                    board[row][col]=" c"
            elif charecters[1]=="d":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                else:
                    board[row][col]=" d"#bottom left corner
                    board[row+1][col]=f"{row}{col}"
                    board[row][col+1]=f"{row}{col}"
                    board[row+1][col+1]=f"{row}{col}"
            elif charecters[1]=="A":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                else:
                    board[row][col]=" A"
            elif charecters[1]=="B":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                else:
                    board[row][col]=" B"
            elif charecters[1]=="C":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                else:
                    board[row][col]=" C"
            elif charecters[1]=="D":
                if col not in range(3,len(board[row])-3) and row not in range(3, len(board[col])-3):
                    stdio.writeln("ERROR: Piece in the wrong position")
                    sys.exit()
                if board[row][col]!="  ":
                    stdio.writeln(f"ERROR: Field {row} {col} not free")
                    sys.exit()
                else:
                    board[row][col]=" D"
                    board[row+1][col]=f"{row}{col}"
                    board[row][col+1]=f"{row}{col}"
                    board[row+1][col+1]=f"{row}{col}"
            elif charecters[0]=="x":
                board[row][col]=" x"
            else:
                stdio.writeln(f"ERROR: Invalid piece type {charecters[1]}")
    except IndexError:
        stdio.writeln(f"ERROR: Invalid object type {charecters[0]}")
        sys.exit()
        

#_______________DO MOVE______________#
def do_move():
    global board
    global count_light
    global count_dark
    
    if count_dark==4:
        stdio.writeln("Dark Wins")
        sys.exit()
    if count_light==3:
        stdio.writeln("Light Wins")
        sys.exit()
    
    try: #with the try-except conditions I am trying to catch the EOFError and print what I want
        stop = False
        while stop==False:
            
            user_input = stdio.readLine()
            movements = user_input.split()
            
            #board[1][2].isupper
            
            
            if len(user_input)==0:
                stop = True
                break
            elif len(user_input)==1:
                stop = True
                break
            else:
                # col = int(movements[0])
                # row = int(movements[1])
                row = int(movements[0])
                col = int(movements[1])
                direction = movements[2]
            
                if direction in ["l", "r", "u", "d"]:
                    if board[row][col]=="  ":
                        stdio.writeln("ERROR: Invalid move. Please try again")
                        sys.exit()
            #=====================================================================#
                    elif direction=="l":
                        if col>=0:
                            if board[row][col]=="  ":  #or board[row][col]==" ":
                                stdio.writeln(f"ERROR: No piece on field {row} {col}")
                                sys.exit()
                            # elif board[row][col-1]not in["  ", f"{row}{col}"]:
                            elif board[row][col-1] not in ["  ", f"{row}{col}", " s"]:
                                stdio.writeln(f"ERROR: Field {row} {col-1} not free")
                                sys.exit()
                            elif col==0:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif board[row][col-1]==" s" and board[row][col-2]==" s" and board[row][col] in [" a"," A"," b"," B"," c", " C"]:# this is a 2x2 sink
                                if board[row][col] in [" a"," A"," b"," B"," c", " C"]:
                                    if board[row][col] in [" a", " A"]:
                                        if board[row][col]==" a":
                                            board[row][col]="  "
                                            count_light+=1
                                        elif board[row][col]==" A":
                                            board[row][col]="  "
                                            count_dark+=1
                                    if board[row][col]==" b":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            count_light+=2
                                        else:
                                            board[row][col]="  "
                                    elif board[row][col]==" B":
                                        board[row][col]=="  "
                                        count_light+=2
                                    elif board[row][col]==" c":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col]=="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                            count_light+=3
                                        else:
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                            sys.exit()
                                    elif board[row][col]==" C":
                                        if  board[row][col+1]==f"{row}{col}":
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                            count_dark+=3
                                        else:
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                            sys.exit()
                            elif board[row][col-1]==" s" and board[row+1][col-1]==" s":
                                if board[row][col] in [" d", " D"]:
                                    if board[row][col]==" d":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                        count_light+=4
                                    elif board[row][col]==" D":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                        count_dark+=4
                                    else: stdio.writeln("Problem 111")
                            elif board[row][col-1]==" s" and board[row][col-2]!=" s":
                                if board[row][col]==" d" or board[row][col]==" D":
                                    stdio.writeln(f"ERROR: Field {row} {col-1}  not free 880")
                                    sys.exit()
                                elif board[row][col] in [" a", " b", " c", " A", " B", " C"]:
                                    if board[row][col]==" a":
                                        board[row][col]="  "
                                        count_light+=1
                                    elif board[row][col]==" A":
                                        board[row][col]="  "
                                        count_dark+=1
                                    elif board[row][col]==" b":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                            sys.exit()
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            count_light+=1
                                    elif board[row][col]==" B":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                            sys.exit()
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            count_dark+=1
                                    elif board[row][col]==" C":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                            sys.exit()
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                            count_dark+=3         
                                    elif board[row][col]==" c":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                            sys.exit()
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                            count_light+=3 
                                    else: stdio.writeln("PROBLEM 000")
                                # sys.exit()
                            elif col==1 and (board[row][col]==" B" or board[row][col]==" b" or board[row][col]==" d" or board[row][col]==" D") and (board[row][col+1]=="  "):
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                # sys.exit()
                            elif (col in [0,1,2]) and (board[row][col]==" C" or board[row][col]==" c" or board[row][col]==" d" or board[row][col]==" D") and (board[row][col+1]=="  "):
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                # sys.exit()
                            elif (board[row][col]==" c" or board[row][col]==" C") and (col<=2) and board[row][col+1]!=f"{row}{col}":
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                # sys.exit()
                            elif (board[row][col] in [" d", " D"]) and col<=1:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                # sys.exite()
                            elif board[row][col] in [" d", " D"] and ((board[row][col-2] not in ["  ", f"{row}{col}"]) or board[row][col-1] not in ["  ", f"{row}{col}"] or board[row+1][col-1] not in ["  ", f"{row}{col}"] or board[row+1][col-2] not in ["  ", f"{row}{col}"]):
                                stdio.writeln(f"ERROR: Field {col} {row} not free 990")
                                # sys.exit()
                            # elif (board[row][col] in [" b", " B"]) and ((board[row+1][col]==f"{row}{col}" and (board[row+1][col-1] not in ["  ", f"{row}{col}"])) or (board[row-1][col]==f"{row}{col}" or (board[row-1][col-1] not in  ["  ", f"{row}{col}"]))):
                            #     stdio.writeln(f"ERROR: Field {col} {row} not free 1111")
                                # sys.exit()
                            elif (board[row][col==" c" or board[row][col]==" C"]) and col<=col_max-2 and (board[row+1][col]==f"{row}{col}") and  (board[row+1][col-1]!="  " and board[row+2][col-1]!="  "):
                                stdio.writeln(f"ERROR: Field {col} {row} not free")
                                # sys.exit()
                            elif (board[row][col]==" d" or board[row][col]==" D") and (board[row][col-1] not in ["  ", f"{row}{col}", " s"] or board[row+1][col-1] not in ["  ", f"{row}{col}", " s"]) :
                                stdio.writeln(f"ERROR: Field {row} {col-1}  not free 000")
                                # sys.exit()
                            elif board[row][col-1] not in ["  ", f"{row}{col}"]:
                                    stdio.writeln(f"ERROR: Field {row} {col-1} not free  1")
                                # sys.exit()
                            elif board[row][col] in [" c", " C"] and board[row][col-2] not in ["  ", f"{row}{col}"] and board[row][col+1]!="  " and board[row][col+1]!=f"{row}{col}":
                                stdio.writeln(f"ERROR: Field {row} {col-2} not free  4")
                            else:
                                if board[row][col] in [" a", " b", " c", " d"]:
                    #---------------------------------------------------------------#
                                    if board[row][col]==" a": #or board[row][col]==" A":
                                        board[row][col-1]=board[row][col]
                                        board[row][col]="  "
                            #----------------------------------------------------------------#
                                    elif board[row][col]==" b": # or board[row][col]==" B":
                                        # if board[row][col+1]=="  " and board[row][col-1]=="  " and board[row-1][col]=="  "
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row+1][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row][col-2]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row-1][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                        else:
                                            board[row][col-2]=board[row][col]
                                            board[row][col-1]=f"{row}{col-2}"
                                            board[row][col]="  "
                                            #stdio.writeln("FOUND")
                        #-------------------------------------------------------------#
                                    elif board[row][col]==" c": #or board[row][col]==" C":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row+1][col-1]=f"{row}{col-1}"
                                            board[row+2][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                            board[row+2][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row][col-3]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row-1][col-1]=f"{row}{col-1}"
                                            board[row-2][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                            board[row-2][col]="  "
                                        else:
                                            board[row][col-3]=board[row][col]
                                            board[row][col-2]=f"{row}{col-3}"
                                            board[row][col-1]=f"{row}{col-3}"
                                            board[row][col]=f"{row}{col-1}"
                                            board[row][col]="  "
                        #-----------------------------------------------------------------#
                                    elif board[row][col]==" d": # or board[row][col]==" D": #here I am trying to move the entire d piece along with it's coordinates
                                        board[row][col-2]=board[row][col]
                                        board[row][col-1]=f"{row}{col-2}"
                                        board[row+1][col-1]=f"{row}{col-2}"
                                        board[row+1][col-2]=f"{row}{col-2}"
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                elif board[row][col] in [" A", " B", " C", " D"]:
                        #------------------------------------------------------------------#
                                    if board[row][col]==" A": #or board[row][col]==" A":
                                        board[row][col-1]=board[row][col]
                                        board[row][col]="  "
                        #--------------------------------------------------------------#
                                    elif board[row][col]==" B": # or board[row][col]==" B":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row+1][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row][col-2]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row-1][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                        else:
                                            board[row][col-2]=board[row][col]
                                            board[row][col-1]=f"{row}{col-2}"
                                            board[row][col]="  "
                        # '''--------------------------------------------------------'''
                                    elif board[row][col]==" C": #or board[row][col]==" C":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row+1][col-1]=f"{row}{col-1}"
                                            board[row+2][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                            board[row+2][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row][col-3]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row][col-1]=board[row][col]
                                            board[row-1][col-1]=f"{row}{col-1}"
                                            board[row-2][col-1]=f"{row}{col-1}"
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                            board[row-2][col]="  "
                                        else:
                                            board[row][col-3]=board[row][col]
                                            board[row][col-2]=f"{row}{col-3}"
                                            board[row][col-1]=f"{row}{col-3}"
                                            board[row][col]=f"{row}{col-1}"
                                            board[row][col]="  "
                        #-------------------------------------------------------------#
                                    elif board[row][col]==" D": # or board[row][col]==" D": #here I am trying to move the entire d piece along with it's coordinates
                                        if board[row][col-1]!=" s":
                                            board[row][col-2]=board[row][col]
                                            board[row][col-1]=f"{row}{col-2}"
                                            board[row+1][col-1]=f"{row}{col-2}"
                                            board[row+1][col-2]=f"{row}{col-2}"
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row+1][col]="  "
                                            board[row+1][col+1]="  "
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row+1][col]="  "
                                            board[row+1][col+1]="  "
                                            count_dark+=1
                            print_board(row_max, col_max)
                        else:
                            stdio.writeln("ERROR: Cannot move beyond the board")
                            # sys.exit()
                #==========================================================================#
                    elif direction=="r":
                        if col<col_max:
                            if board[row][col]== "  ": #or board[row][col]==" ":
                                stdio.writeln(f"ERROR: No piece on field {row} {col}")
                                # sys.exit()
                            elif col==col_max:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                # sys.exit()
                            elif col==col_max-1:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                # sys.exit()
                            elif board[row][col+1]==" s" and board[row][col+2]==" s":# this is a 2x2 sink
                                if board[row][col] in [" a"," A"," b"," B"," c", " C",]:
                                    if board[row][col] in [" a", " A"]:
                                        if board[row][col]==" a":
                                            board[row][col]="  "
                                            count_light+=1
                                        elif board[row][col]==" A":
                                            board[row][col]="  "
                                            count_dark+=1
                                    if board[row][col]==" b":
                                        if board[row][col-1]==f"{row}{col}":
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            count_light+=2
                                        else:
                                            board[row][col]="  "
                                    elif board[row][col]==" B":
                                        board[row][col]=="  "
                                        count_light+=2
                                    elif board[row][col]==" c":
                                        if board[row][col-1]==f"{row}{col}":
                                            board[row][col]=="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                            count_light+=3
                                        else:
                                            stdio.writeln(f"ERROR: Field {row} {col+1}  not free")
                                    elif board[row][col]==" C":
                                        if  board[row][col-1]==f"{row}{col}":
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                            count_dark+=3
                                        else:
                                            stdio.writeln(f"ERROR: Field {row} {col+1}  not free")
                            elif board[row][col+1]==" s" and board[row+1][col+1]==" s":
                                if board[row][col] in [" d", " D"]:
                                    if board[row][col]==" d":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                        count_light+=4
                                    elif board[row][col]==" D":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                        count_dark+=4
                            elif board[row][col+1]==" s" and board[row][col+2]!=" s":
                                if board[row][col]==" d" or board[row][col]==" D":
                                    stdio.writeln(f"ERROR: Field {row} {col+1}  not free 123")
                                    # sys.exit()
                                elif board[row][col] in [" a", " b", " c", " A", " B", " C"]:
                                    if board[row][col]==" a":
                                        board[row][col]="  "
                                        count_light+=1
                                    elif board[row][col]==" A":
                                        board[row][col]="  "
                                        count_dark+=1
                                    elif board[row][col]==" b":
                                        if board[row][col-1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col+1}  not free 667")
                                        else:
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            count_light+=1
                                    elif board[row][col]==" B":
                                        if board[row][col-1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col+1}  not free 5555")
                                        else:
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            count_dark+=1
                                    elif board[row][col]==" C":
                                        if board[row][col-1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col+1}  not free 444")
                                        else:
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                            count_dark+=3         
                                    elif board[row][col]==" c":
                                        if board[row][col-1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col+1}  not free 333")
                                        else:
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                            count_light+=3 
                            elif board[row][col+1] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row} {col+1} not free 222")
                                sys.exit()
                            elif (board[row][col] in [" B", " b", " C", " c"]) and col>=col_max-2 and board[row][col-1]!=f"{row}{col}":
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif board[row][col] in [" d", " D"] and ((board[row][col+2] not in ["  ", f"{row}{col}", " s"]) or board[row][col+3] not in ["  ", f"{row}{col}", " s"] or board[row+1][col+2] not in ["  ", f"{row}{col},"," s"] or board[row+1][col+3] not in ["  ", f"{row}{col}", " s"]):
                                stdio.writeln(f"ERROR: Field {col} {row} not free 111")
                                sys.exit()
                            elif (board[row][col] in [" c", " C"]) and col>=col_max-3 and board[row][col-1]!=f"{row}{col}":
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif (board[row][col] in [" d", " D"]) and col>=col_max-3:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                            else:
                    #------------------------------------------------------------------#
                                if board[row][col]==" a" or board[row][col]==" A":
                                    board[row][col+1]=board[row][col]
                                    board[row][col]="  "
                    #------------------------------------------------------------------#
                                elif board[row][col]==" b" or board[row][col]==" B":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col+2]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row][col+1]=board[row][col]
                                            board[row+1][col+1]=f"{row}{col+1}"
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row][col+1]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row][col+1]=board[row][col]
                                            board[row-1][col+1]=f"{row}{col+1}"
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                        else:
                                            board[row][col+1]=board[row][col]
                                            board[row][col+2]=f"{row}{col+1}"
                                            board[row][col]="  "
                            #-------------------------------------------------------------#
                                elif board[row][col]==" c" or board[row][col]==" C":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row][col+3]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row][col+1]=board[row][col]
                                            board[row+1][col+1]=f"{row}{col+1}"
                                            board[row+2][col+1]=f"{row}{col+1}"
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                            board[row+2][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row][col+1]=board[row][col]
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row][col+1]=board[row][col]
                                            board[row-1][col+1]=f"{row}{col+1}"
                                            board[row-2][col+1]=f"{row}{col+1}"
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                            board[row-2][col]="  "
                                        else:
                                            board[row][col+1]=board[row][col]
                                            board[row][col+2]=f"{row}{col+1}"
                                            board[row][col+3]=f"{row}{col+3}"
                                            board[row][col]="  "
                            #---------------------------------------------------------------#
                                elif board[row][col]==" d" or board[row][col]==" D": #here I am trying to move the entire d piece along with it's coordinates
                                    if board[row][col+2]!=" s":
                                        board[row][col+2]=board[row][col]
                                        board[row][col+3]=f"{row}{col+2}"
                                        board[row+1][col+2]=f"{row}{col+2}"
                                        board[row+1][col+3]=f"{row}{col+2}"
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                    else:
                                        if board[row][col]==" d":
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row+1][col]="  "
                                            board[row+1][col+1]="  "
                                            count_light+=1
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row+1][col]="  "
                                            board[row+1][col+1]="  "
                                            count_dark+=1
                            print_board(row_max, col_max)
                        else:
                            stdio.writeln("ERROR: Cannot move beyond the board")
                            sys.exit()
            #================================================================================#
                    elif direction=="d":
                        if row in range(0, row_max):
                            if board[row][col]=="  ": # or board[row][col]==" ":
                                stdio.writeln(f"ERROR: No piece on field {row} {col}")
                                # sys.exit()
                            elif board[row-1][col]==" s":
                                if board[row][col]==" d" or board[row][col]==" D":
                                    board[row][col] ="  "
                                    board[row][col+1]="  "
                                    board[row+1][col]="  "
                                    board[row+1][col+1]="  "
                                else:
                                    board[row][col]="  "
                            elif row==0:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif (board[row][col] in [" B", " b", " c", " C"]) and row==1 and board[row+1][col]!=f"{row}{col}":
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif board[row-1][col] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row-1} {col} not free  322")
                            elif board[row][col] in [" d", " D", " b", " B", " c", " C"] and board[row][col+1]==f"{row}{col}" and (board[row-1][col+1] not in ["  ", f"{row}{col}"]):
                                stdio.writeln(f"ERROR: Field {row-1} {col} not free  324")
                                sys.exit()
                            elif board[row][col] in [" c", " C"] and board[row][col+1]==f"{row}{col}":
                                stdio.writeln(f"ERROR: Field {row-1} {col} not free  3")
                            elif board[row][col] in [" c", " C"] and board[row][col+2]==f"{row}{col}" and (board[row-1][col+2] not in ["  ", f"{row}{col}"]):
                                stdio.writeln(f"ERROR: Field {row-1} {col+2} not free  433")
                                sys.exit()
                            elif board[row-2][col] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row-2} {col} not free  433")
                                sys.exit()
                            elif board[row-1][col]==" s" and board[row-1][col-1]==" s" and board[row][col+1]==f"{row}{col}" and board[row][col]==" b":
                                board[row][col]="  "
                                board[row][col+1]="  "
                                count_light+=2
                            elif board[row-1][col]==" s" and board[row-1][col-1]==" s" and board[row][col+1]==f"{row}{col}" and board[row][col]==" B":
                                board[row][col]="  "
                                board[row][col+1]="  "
                                count_dark+=2
                            elif board[row-1][col]==" s" and board[row-2][col]==" s":# this is a 2x2 sink
                                if board[row][col] in [" a"," A"," b"," B"," c", " C"]:
                                    if board[row][col] in [" a", " A"]:
                                        if board[row][col]==" a":
                                            board[row][col]="  "
                                            count_light+=1
                                        elif board[row][col]==" A":
                                            board[row][col]="  "
                                            count_dark+=1
                                    elif board[row][col]==" b" and board[row][col+1]==f"{row}{col}" and board[row-1][col]==" s" and board[row-1][col+1]==" s":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                    elif board[row][col]==" b":
                                        if board[row+1][col]==f"{row}{col}":
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                            count_light+=2
                                        else:
                                            board[row][col]="  "
                                    elif board[row][col]==" B" and board[row+1][col]==f"{row}{col}":
                                        board[row][col]="  "
                                        board[row+1][col]="  "
                                        count_dark+=2
                                    elif board[row][col]==" C" and board[row][col+1]==f"{row}{col}":
                                        stdio.writeln(f"ERROR: Field {row-1} {col} not free  3")
                                    elif board[row][col]==" c" and board[row+1][col]==f"{row}{col}":
                                        stdio.writeln(f"ERROR: Field {row} {col-1} not free")
                                        # if board[row+1][col]==f"{row}{col}":
                                        board[row][col]=="  "
                                        board[row+1][col]="  "
                                        board[row+2][col]="  "
                                        count_light+=3
                                    elif board[row][col]==" C":
                                        if  board[row][col+1]==f"{row}{col}":
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                            board[row+2][col]="  "
                                            count_dark+=3
                                        else:
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                            sys.exit
                            elif board[row][col-1]==" s" and board[row+1][col-1]==" s":
                                if board[row][col] in [" d", " D"]:
                                    if board[row][col]==" d":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                        count_light+=4
                                    elif board[row][col]==" D":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row+1][col]="  "
                                        board[row+1][col+1]="  "
                                        count_dark+=4
                            elif board[row][col-1]==" s" and board[row][col-2]!=" s":
                                if board[row][col]==" d" or board[row][col]==" D":
                                    stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                    sys.exit()
                                elif board[row][col] in [" a", " b", " c", " A", " B", " C"]:
                                    if board[row][col]==" a":
                                        board[row][col]="  "
                                        count_light+=1
                                    elif board[row][col]==" A":
                                        board[row][col]="  "
                                        count_dark+=1
                                    elif board[row][col]==" b":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            count_light+=1
                                    elif board[row][col]==" B":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            count_dark+=1
                                    elif board[row][col]==" C":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                            count_dark+=3
                                    elif board[row][col]==" c":
                                        if board[row][col+1]=="  ":
                                            stdio.writeln(f"ERROR: Field {row} {col-1}  not free")
                                        else:
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                            count_light+=3
                            else:
                        #----------------------------------------------------------------------#
                                if board[row][col]==" a" or board[row][col]==" A":
                                    board[row-1][col]=board[row][col]
                                    board[row][col]="  "
                        #----------------------------------------------------------------------#
                                elif board[row][col]==" b" or board[row][col]==" B":
                                    if board[row-1][col]==" s" and board[row-1][col-1]==" s" and board[row][col+1]==f"{row}{col}":
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                    if board[row][col+1]==f"{row}{col}":
                                        board[row-1][col]=board[row][col]
                                        board[row-1][col+1]=f"{row-1}{col}"
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                    elif board[row+1][col]==f"{row}{col}":
                                        board[row-1][col]=board[row][col]
                                        board[row][col]="  "
                                        board[row+1][col]="  "
                                    elif board[row][col-1]==f"{row}{col}":
                                        board[row][col+1]=board[row][col]
                                        board[row][col]="  "
                                        board[row][col-1]="  "
                                    elif board[row-1][col]==f"{row}{col}":
                                        board[row-2][col]=board[row][col]
                                        board[row][col]="  "
                                        board[row-1][col]="  "
                                    else:
                                        board[row-2][col]=board[row][col]
                                        board[row-1][col]=f"{row-2}{col}"
                                        board[row][col]="  "
                        #-------------------------------------------------------------------------#
                                elif board[row][col]==" c" or board[row][col]==" C":
                                    if board[row][col+1]==f"{row}{col}":
                                        board[row-1][col]=board[row][col]
                                        board[row-1][col+1]=f"{row-1}{col}"
                                        board[row-1][col+2]=f"{row-1}{col}"
                                        board[row][col]="  "
                                        board[row][col+1]="  "
                                        board[row][col+2]="  "
                                    elif board[row+1][col]==f"{row}{col}":
                                        board[row-1][col]=board[row][col]
                                        board[row][col]="  "
                                        board[row+1][col]="  "
                                        board[row+2][col]="  "
                                    elif board[row][col-1]==f"{row}{col}":
                                        board[row-1][col]=board[row][col]
                                        board[row-1][col-1]=f"{row-1}{col}"
                                        board[row-1][col-2]=f"{row-1}{col}"
                                        board[row][col]="  "
                                        board[row][col-1]="  "
                                        board[row][col-2]="  "
                                    elif board[row-1][col]==f"{row}{col}":
                                        board[row-3][col]=board[row][col]
                                        board[row][col]="  "
                                        board[row-1][col]="  "
                                        board[row-2][col]="  "
                                    else:
                                        board[row-3][col]=board[row][col]
                                        board[row-2][col]=f"{row-3}{col}"
                                        board[row-1][col]=f"{row-3}{col}"
                                        board[row][col]="  "
                                        # stdio.writeln("FOUND D")
                        #-----------------------------------------------------------------#
                                elif board[row][col]==" d" or board[row][col]==" D": #here I am trying to move the entire d piece along with it's coordinates
                                    board[row-2][col]=board[row][col]
                                    board[row-1][col]=f"{row-2}{col}"
                                    board[row-1][col+1]=f"{row-2}{col}"
                                    board[row-2][col+1]=f"{row-2}{col}"
                                    board[row][col]="  "
                                    board[row][col+1]="  "
                                    board[row+1][col]="  "
                                    board[row+1][col+1]="  "
                            print_board(row_max, col_max)
                        else:
                            stdio.wrieln("ERROR: Cannot move beyond the board")
                            sys.exit()
             #=======================================================================================#
                    elif direction=="u":
                        if row<row_max:
                            if board[row][col]=="  ": #or board[row][col]==" ":
                                stdio.writeln(f"ERROR: No piece on field {row} {col}")
                                sys.exit()
                            elif row==row_max:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif row==row_max-1:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif board[row+1][col]==" s":
                                if board[row][col]==" d" or board[row][col]==" D":
                                    board[row][col] ="  "
                                    board[row][col+1]="  "
                                    board[row+1][col]="  "
                                    board[row+1][col+1]="  "
                                else:
                                    board[row][col]="  "
                            elif board[row][col] in [" B", " b", " c", " C"] and row>=row_max-2 and board[row-1][col]!=f"{row}{col}":
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif board[row][col] in [" d", " D"] and row>=row_max-2:
                                stdio.writeln("ERROR: Cannot move beyond the board")
                                sys.exit()
                            elif board[row+1][col] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row+1} {col} not free")
                                sys.exit()
                            elif board[row][col] in [" b", " B", " c", " C", " d"," D"] and board[row+2][col] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row+2} {col} not free")
                                sys.exit()
                            elif board[row][col] in [" b", " B", " c", " C"] and board[row+1][col] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row+1} {col} not free")
                                sys.exit()
                            elif board[row][col] in [" c", " C"] and board[row+1][col] not in ["  ", f"{row}{col}"] and board[row+2][col] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row+2} {col} not free")
                                sys.exit()
                            elif board[row][col] in [" d", " D"] and board[row+2][col] not in ["  ", f"{row}{col}"] and board[row+2][col] not in ["  ", f"{row}{col}"] and board[row+2][col+1] not in ["  ", f"{row}{col}"] and board[row+3][col+1] not in ["  ", f"{row}{col}"]:
                                stdio.writeln(f"ERROR: Field {row+1} {col} not free")
                        #-----------------------------------------------------------------#
                            else:
                                if board[row][col]==" a" or board[row][col]==" A":
                                    board[row+1][col]=board[row][col]
                                    board[row][col]="  "
                        #----------------------------------------------------------------#
                                elif board[row][col]==" b" or board[row][col]==" B":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row+1][col]=board[row][col]
                                            board[row+1][col+1]=f"{row+1}{col}"
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row+2][col]=board[row][col]
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row+1][col]=board[row][col]
                                            board[row+1][col-1]=f"{row+1}{col}"
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row+1][col]=board[row][col]
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                        else:
                                            board[row+1][col]=board[row][col]
                                            board[row+2][col]=f"{row+1}{col}"
                                            board[row][col]="  "
                            #-------------------------------------------------------------------#
                                elif board[row][col]==" c" or board[row][col]==" C":
                                        if board[row][col+1]==f"{row}{col}":
                                            board[row+1][col]=board[row][col]
                                            board[row+1][col+1]=f"{row+1}{col}"
                                            board[row+1][col+2]=f"{row+1}{col}"
                                            board[row][col]="  "
                                            board[row][col+1]="  "
                                            board[row][col+2]="  "
                                        elif board[row+1][col]==f"{row}{col}":
                                            board[row+3][col]=board[row][col]
                                            board[row][col]="  "
                                            board[row+1][col]="  "
                                            board[row+2][col]="  "
                                        elif board[row][col-1]==f"{row}{col}":
                                            board[row+1][col]=board[row][col]
                                            board[row+1][col-1]=f"{row+1}{col}"
                                            board[row+1][col-2]=f"{row+1}{col}"
                                            board[row][col]="  "
                                            board[row][col-1]="  "
                                            board[row][col-2]="  "
                                        elif board[row-1][col]==f"{row}{col}":
                                            board[row-3][col]=board[row][col]
                                            board[row][col]="  "
                                            board[row-1][col]="  "
                                            board[row-2][col]="  "
                                        else:
                                            board[row+1][col]=board[row][col]
                                            board[row+2][col]=f"{row+1}{col}"
                                            board[row+3][col]=f"{row+1}{col}"
                                            board[row][col]="  "
                            #-------------------------------------------------------------#
                                elif board[row][col]==" d" or board[row][col]==" D":
                                    board[row+2][col]=board[row][col]
                                    board[row+3][col]=f"{row+2}{col}"
                                    board[row+2][col+1]=f"{row+2}{col}"
                                    board[row+3][col+1]=f"{row+2}{col}"
                                    board[row][col]="  "
                                    board[row+1][col]="  "
                                    board[row][col+1]="  "
                                    board[row+1][col+1]="  "
                            #---------------------------------------------------------------#
                            print_board(row_max, col_max)
                        else:
                            stdio.writeln("ERROR: Cannot move beyond the board")
                            sys.exit()
                else:
                    stdio.writeln(f"ERROR: Invalid direction {direction}")
                            
    except EOFError:
        stdio.writeln()
    except IndexError:
        stdio.writeln("Theres an error")

#______________GUI MODE_______________#
def gui_enable():
    pass
    
if __name__ == "__main__":
    read_board()
    print_board(row_max, col_max)
    do_move()