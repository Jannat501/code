#[1]
x = 2   #starting point
lr = 0.01  #learning rate
precision = 0.000001
previous_step_size = 1
max_iter = 10000
iters = 0
gf = lambda x: (x+3) ** 2


#[2]
import matplotlib.pyplot as plt
gd = []

#[3]
while precision < previous_step_size and iters < max_iter:
    prev = x
    x = x - lr * gf(prev)
    previous_step_size = abs(x-prev)
    iters +=1
    print('Iteration:',iters,'Value :',x)
    gd.append(x)


#[4]
print('Local Minima',x)    

#[5]
plt.plot(gd)