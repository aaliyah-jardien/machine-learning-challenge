import numpy

numbers = numpy.arange(0,20)

my_mean = numpy.mean(numbers)
print("The mean from the list of numbers is:", my_mean)

my_variance = numpy.var(numbers)
print("The variance of the numbers is:", my_variance)

my_deviation = numpy.std(numbers)
print("The standard deviation is:", my_deviation)
