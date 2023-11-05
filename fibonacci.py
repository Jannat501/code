#Without Recurrsion

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a , end =" ")
#         next_term = a+b
#         a = b
#         b = next_term

# v = int(input("Enter number:"))      
# fibonacci(v)


#With Recurssion

def fibonacci(n):
    if(n <= 1):
      return n;
    else:
      return fibonacci(n-1) + fibonacci(n-2);

n = int(input("Enter number:")) 
for i in range(n):
   print(fibonacci(i))