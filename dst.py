from utils import *

class dst:
    """Class for solving a D-S evidence theory problem."""

    def __init__(self, D, masses):
        assert(len(masses[0]) == (1 << len(D)))

        self.D = D
        self.mass = multi_joint_mass(masses)

    def m_belief(self, mask):
        """Calculate the belief of hypothesis, which is represented by mask."""

        belief = 0.0
        for m in range(len(self.mass)):
            if (m & mask) == m:
                belief += self.mass[m]
        return belief

    def m_plausibility(self, mask):
        """Calculate the plausibility of hypothesis, which is represented by mask."""

        complement = (len(self.mass) - 1) ^ mask
        return 1.0 - self.m_belief(complement)

    def name(self, mask):
        """The name of the mask indicates."""

        s = ""
        for i in range(len(self.D)):
            if (mask >> i) & 1:
                s += "U " + "'" + self.D[i] + "' "
        return "∅" if s == "" else s[2:]

    def summary(self):
        """Print summary."""

        table = [["Hypothesis", "Mass", "Belief", "Plausibility"]]
        for m in range(len(self.mass)):
            table.append([self.name(m), round(self.mass[m], 3), round(self.m_belief(m), 3), round(self.m_plausibility(m), 3)])
        print_table(table)

def K(mass_a, mass_b):
    """Calculate value K in Dempster's rule of combination."""

    k = 0.0
    for a in range(len(mass_a)):
        for b in range(len(mass_b)):
            if (a & b) == 0:
                k += mass_a[a] * mass_b[b]
    return k

def joint_mass(mass_a, mass_b):
    """Combine mass_a and mass_b using Dempster's rule of combination."""

    k2 = 1.0 - K(mass_a, mass_b)
    mass = [0.0] * len(mass_a)
    for a in range(len(mass_a)):
        for b in range(len(mass_b)):
            if (a & b) != 0:
                mass[a & b] += mass_a[a] * mass_b[b] / k2
    return mass

def multi_joint_mass(masses):
    """Combine multiple masses using Dempster's rule of combination."""

    mass = masses[0]
    for m in masses[1:]:
        mass = joint_mass(mass, m)
    return mass
