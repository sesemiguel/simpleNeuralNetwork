#Created by Miguel Sese
#My first simple implementation of a neural network
import numpy as np
def sigmoidFunction(x):
    return 1/(1+np.exp(x))

def neuralNetwork(m1,m2,w1,w2,b):
    z = (m1 * w1) + (m2 * w2) + b
    return sigmoidFunction(z)

txt = open("Output.txt", "w")
txt.write("SIMPLE NEURAL NETWORK\n")
#Weights, Bias, and Inputs
w1 = 0.4 #Weight1
w2 = 0.9 #Weight2
b = 0.6 #Bias
m1 = np.array([3, 2, 4, 3, 3.5, 2, 5.5, 1, 4.5]) #Input1
m2 = np.array([1.5, 1, 1.5, 1, .5, .5, 1, 1, 1]) #Input2

txt.write("Weight1: "+str(w1)+"\n"+"Weight2: "+str(w2)+"\n"+"Bias: "+str(b)+"\n"+"Input1: "+str(m1)+"\n"+"Input2: "+str(m2)+"\n") #Write to text file

#Calculating Output
for i in range(0,np.size(m1)):
    predict = neuralNetwork(m1[i],m2[i],w1,w2,b)
    txt.write("Output"+str(i)+": "+str(predict)+"\n")
txt.close()




