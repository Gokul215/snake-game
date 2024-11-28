from collections import deque
import random

class snake:
    queue=deque()
    food=deque()
    def __init__(self,row,col) -> None:
        self.row=row
        self.col=col
        self.snakeboard=[['1']*(col) for i in range(row)]
        self.point=0
        self.fooddisplay()
    def initiateSnake(self):
         row = 0
         col = 0
         self.snakeboard[row][col]='.'
         snake.queue.append((row,col))
         while True:
            self.printsnake()
            # print(row,col)
            choice=input("enter move(U/D/L/R): ").upper()
            if choice=='U':
                if self.movement(row-1,col):
                  row=row-1
                  col=col
                else:
                    break
    
            elif choice=='D':
                if self.movement(row+1,col):
                    row=row+1
                    col=col
                else:
                    break
                
            elif choice=='L':
                if self.movement(row,col-1):
                    col=col-1
                    row=row
                else:
                    break
                
            elif choice=='R':
                if self.movement(row,col+1):
                    col=col+1
                    row=row
                else:
                    break
            else:
                print("invalid key")
                return
    def movement(self,row,col):
        
        if row>=0 and row<len(self.snakeboard) and col>=0 and col < len(self.snakeboard[0]):
            # print(snake.queue)
            snake.queue.append((row,col))
            if self.snakeboard[row][col]=='X':
                self.snakeboard[row][col]='.'
                self.point+=1
                self.fooddisplay()
                
                
                
            elif self.snakeboard[row][col]=='.':
                print("Game over----")
                print(f"Your score:{self.point}")

                return False
            elif self.snakeboard[row][col]!='X':
                r,c=snake.queue.popleft()
                # print(r,c)
                self.snakeboard[r][c]='1'
                self.snakeboard[row][col]='.'
            
    
            return True
        else:
            print("Game over----")
            print(f"Your score:{self.point}")
            return False
         
    def fooddisplay(self):
        while True:
            x=random.randrange(self.row)
            y=random.randrange(self.col)
            if (x,y) not in self.queue:
                self.snakeboard[x][y]='X'
                break
        # snake.food.append((x,y))
        # row,col=path
        
        
    def printsnake(self):
        for i in range(len(self.snakeboard)):
            for j in range(len(self.snakeboard[0])):
                
                print(self.snakeboard[i][j],end='  ')
            print()