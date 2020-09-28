import numpy
lis = [0,0,0,0,0]
lis[0] = int(input("Input a: "))
lis[1] = int(input("Input b: "))
lis[2] = int(input("Input c: "))
lis[3] = int(input("Input d: "))
lis[4] = int(input("Input e: "))
print("mean: %.3f"%(numpy.mean(lis))) 
print("sd: %.3f"%(numpy.std(lis))) 