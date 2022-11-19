import time

n = int(input("Enter the value of N: "))
print("Results: ")
cnt=0

#starting time
starting_time = time.time()

def solveNQueens(n):
    
        col = set()
        posDiag = set() # (r+c)
        negDiag = set() # (r-c)
        
        board = [-1] * n 
        
        def backtrack(r):
            global cnt
            if r==n:              
                print(board)
                cnt+=1
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r]=c
           
                backtrack(r+1)
       
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r]=-1
             
        backtrack(0)
        return

solveNQueens(n)

# Ending Time
ending_time = time.time()

# get the execution time
elapsed_time = ending_time - starting_time

print("Total no. of Solutions: ", cnt)
print("Execution time:", elapsed_time, "seconds")