from fractions import Fraction as Frac
import heapq

################################################################################
#                           FRACTION ARCTAN STUFF                              #
################################################################################

def sub(x,y): # X = Smaller number
    return Frac((x*y+1),(y-x))
def create(degree,m=0):
    inputs = [5,7,8]
    coefficients = [2,1,2]
    for z in range(degree):
        print((inputs,coefficients))
        if m == 1:
            smallest = input('Change Number: ')
            next_smallest = input('Keep Index: ')
        else:
            smallest = min(inputs)
            next_smallest = smallest
            n = 2
            while next_smallest == smallest:
                next_smallest = heapq.nsmallest(n, inputs)[-1]
                n += 1
        coefficients[inputs.index(next_smallest)] += coefficients[inputs.index(smallest)]
        inputs[inputs.index(smallest)] = sub(smallest,next_smallest)
    return (inputs,coefficients)

def insert(original, new, pos):
    return original[:pos] + new + original[pos:]

def arccot(m, x, one=1000000):
    """
    Calculate arctan(1/x) using euler's accelerated formula

    This calculates it in fixed point, using the value for one passed in
    """
    x_squared = x * x
    x_squared_plus_1 = x_squared + 1
    term = (x * 10**one) // x_squared_plus_1
    total = term
    two_n = 2
    while True:
        divisor = (two_n+1) * x_squared_plus_1
        term *= two_n
        term = term // divisor
        if term == 0:
            break
        total += term
        two_n += 2
    return m*total

def pi(digits,inputs=[5,239],coefficients=[4,-1]):
    one = digits+len(str(digits))
    pi_val = 0
    me = len(inputs)
    for x in range(len(inputs)):
        pi_val += 4*arccot(coefficients[x],inputs[x],one)
    return str(pi_val)

################################################################################
#                            INTEGER ARCTAN STUFF                              #
################################################################################

def evolarctan():    
    def alltuples(nums):
        """
        Return all pairs of numbers in a list.
        If two numbers are the same, they will not be counted as a pair.
        """
        nums = list(set(nums))
        tuples = []
        for thing in nums:
            for other_thing in nums:
                if thing != other_thing:
                    tuples.append((thing,other_thing))
        return tuples
    
    def sub(x,y):
        return (x*y+1)/(y-x)

    def all_sub(x):
        subs = []
        for i in range(2*x,x,-1):
            j = sub(x,i)
            if j%1 == 0:
                subs.append((i,int(j)))
        return subs

    inputs = [2,7]
    coefficients = [1,-1]
    population = {1:1}
    for i in inputs:
        for a in all_sub(i):
            d = 0
evolarctan()
