# Code your functions here!

# We're going to write three functions: one to build downward stairs, one to build upward stairs, and one to build pyramid stairs (they go up and then back down).

'''1) Descending stairs'''
# The code above should print a descending staircase

# count = 1

def downstairs(num):
  for i in range(1, num+1):
    print("#"*i)
    
# downstairs(3)

'''2) Ascending stairs'''
# The code above should print an ascending staircase

# def upstairs(num):
#   #spaces * incrimental-1, # - whatev left
#   for i in range(num+1):
#     i = 1
#     print(" "*num-1 + "#"*i)
#     i += 1
# upstairs(6)

#Jayne's Solution
def stair(num):
  n = num 
  i = 1 
  while(n > 0):
    print(" "* (n-1) + "#" * (i)) 
    n-=1 
    i+=1

stair(6)

'''3) Pyramid stairs'''
# The code should print an ascending staircase and it's mirror descending staircase