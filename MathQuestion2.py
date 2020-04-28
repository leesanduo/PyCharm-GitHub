'''Solving a math equation that takes numbers 1-9 and cannot repeat'''

# AB * C (=DE) + FG = HI where all are different digits

import constraint

problem = constraint.Problem()
problem.addVariables("ABCDEFGHI", range(1,10))  # Adding multiple variables. Apparently since Strings are arrays of characters we can write "AB" instead of ['A','B'].

def our_constraint(a, b, c, d, e, f, g, h, i):
    if (a*10 + b) * c + (f*10 + g) == (h*10 + i) and \
        (a*10 + b) * c == (d*10 + e):
        return True

problem.addConstraint(our_constraint, "ABCDEFGHI")  # Adding the equation constraint
problem.addConstraint(constraint.AllDifferentConstraint())  # AllDifferentConstraints is in-built method for all values must be different

solutions = problem.getSolutions()
print("Number of solutions found: {}\n".format(len(solutions)))
for s in solutions:  # getSolutions() returns a dictionary
    print("AB={}{}, C={}, DE={}{}, FG={}{}, HI={}{}".format(s['A'], s['B'], s['C'], s['D'], s['E'], s['F'], s['G'], s['H'], s['I']))