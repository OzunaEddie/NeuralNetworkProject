import random


class NeuralNetwork:

    def __init__(self, n, m):
        self.n = n
        self.random_points = [[0]*n]*m #Create an instance 2D list with n columns and m rows
        self.s = [[0]*n]*m #Create an instance 2D list with n columns and m rows
        self.t_of_h = [[0]*8]*m #Creates an instance 2D list with 8 columns and m rows. This will become our tuple of class H
        self.t_of_l = [[0]*8]*m #Creates an instance 2D list with 8 columns and m rows. This will become our tuple of class L
        points = random.sample(range(12), 12) #Points take 12 random values from range 0 to 11
        l = 0
        k = n
        for i in range(m):
            self.random_points[i] = points[l:k] #Values in random_points will be populated with values from points from l to k
            self.random_points[i].sort() #random_points will be sorted into increasing order
            l = k
            k += n

    def train(self, array): #This will help train the neural network to recognize which belongs to Class H or Class L
        for i in range(len(self.random_points)):
            points = self.random_points[i] #points will take values of random_points
            for j in range(len(points)):
                print(points[j])
                self.s[i][j] = array[points[j]]

    def class_l():
        return None

    def class_h():
        return None


# One of the way we can generate our dataset
f = open("training.txt", "w+") #Creates a new file if it doesn't exist and if it does, it writes over the original text
for j in range(300):
    training_set = ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"] #Create an array with a perfect H
    for i in range(4, 8, 3):
        training_set[i] = random.choice(['0', '1']) #Change the value at index 4 and 7 in order to form variations of a perfect H
    f.write("".join(training_set)) #Inserts the array into the text file
    f.write("\n")


a = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
network = NeuralNetwork(3, 4)
network.train(a)
for i in network.random_points:
    print(i)
print(" ")
for i in network.s:
    print(i)
