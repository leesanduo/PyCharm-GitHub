'''Solving a math equation that takes numbers 1-9 and cannot repeat'''

# x * y + z = r where x is 2 digit number and y is 1 digit and r is 2 digit and result is 2 digit

import constraint

problem = constraint.Problem()

problem.addVariable('x', range(11,100))
problem.addVariable('y', range(1,10))
problem.addVariable('z', range(11,100))
problem.addVariable('r', range(11,100))


def our_constraint(x,y,z,r):
    digit_list = [str(num)[position] for num in [x,z,r] for position in range(2)]
    if x*y+z == r and \
        list(set(digit_list)) == digit_list:
        return True

problem.addConstraint(our_constraint, ['x', 'y', 'z', 'r'])

solutions = problem.getSolutions()
print(solutions)