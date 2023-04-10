from dst import *

D = ["Red", "Yellow", "Green"]
mass1 = [0.0, 0.2, 0.1, 0.15, 0.1, 0.3, 0.1, 0.05]
mass2 = [0.0, 0.3, 0.2, 0.1, 0.15, 0.2, 0.03, 0.02]
mass3 = [0.0, 0.1, 0.05, 0.2, 0.1, 0.3, 0.1, 0.15]

dst(D, [mass1, mass2, mass3]).summary()
