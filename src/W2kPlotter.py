import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys
matplotlib.rc('text', usetex = True)
matplotlib.rc('font', **{'family':'sans-serif', 'sans-serif':['Computer Modern Roman, Times']})

# Welcome to Wien2k Plotter (W2kPlotter) a python class for plotting the bandstructure and density of states from WIEN2k's output files.


# Design to be an interactive program that allows the user to communicte their needs to the code and the code produces publishable figures.
# All the user must do is provide the correct input files into the program.
class W2kPlotter():

    def __init__(self, spaghetti, grace, title, save, Emin, Emax):
        # the grace file will give us the high symmetry points because as of now I'm
        # not sure how to find the high symmetry points
        self.spaghetti = spaghetti
        self.grace = grace
        self.save = save
        self.Emin = Emin
        self.Emax = Emax
        self.title = title

    def getHighSymmetryPoints(self):
        f = open(self.grace, 'r')
        highSymmPts = []
        highSymmLabels = []
        for i, line in enumerate(f):
            if 'tick major' in line:
                if 'grid on' not in line:
                    line = line.lstrip().rstrip()
                    pt = float(line.split()[5])
                    highSymmPts.append(pt)
            if 'ticklabel' in line:
                if 'size' not in line:
                    line = line.lstrip().rstrip()
                    label = line.split()[4][2:]
                    if label == '\\xG"':
                        highSymmLabels.append(r'$\Gamma$')
                    else:
                        highSymmLabels.append(label)
        return(highSymmPts, highSymmLabels)


    def BS_Plotter(self):
        f = open(self.spaghetti, 'r')
        k = []
        E = []
        highsymmpts, labels = self.getHighSymmetryPoints()
        plt.figure()

        for i, line in enumerate(f):
            if 'bandindex' not in line:
                line = line.rstrip().lstrip()
                if float(line.split()[4]) > self.Emin and float(line.split()[4]) < self.Emax:
                    k.append(float(line.split()[3]))
                    E.append(float(line.split()[4]))

            else:
                plt.plot(k, E, linewidth = 1)
                #kmax = np.max(k)
                k = []
                E = []
        plt.grid(True, linewidth =1, linestyle =':')
        # This part will be generated by another function at antoher point
        #plt.xticks(highsymmpts, (r'$\Gamma$', 'X', 'M', r'$\Gamma$', 'Z', 'R', 'A', 'Z'))
        plt.xticks(highsymmpts, labels)
        plt.ylabel('Energy (eV)')
        plt.ylim([self.Emin,self.Emax])
        plt.xlim([0,2.91])
        plt.plot(np.linspace(0,2.91,1000), [0 for i in range(1000)], 'k--', linewidth = 1)
        plt.title(self.title)
        if self.save:
            plt.savefig('%s.eps'  %(self.title), format = 'eps')
        else:
            plt.show()

file2 = '/Users/harrisonlabollita/Documents/Arizona State University/Botana group/Projects/ho_nick/bandstruct/W2k_spaghetti/dz2/5410_k_1000_tot_Ni_dz2.agr'
file = '/Users/harrisonlabollita/Documents/Arizona State University/Botana group/Projects/ho_nick/bandstruct/W2k_spaghetti/dz2/5410_k_1000_tot_Ni_dz2.spaghetti_ene'
W = W2kPlotter(file, file2, r'5410 Tot Ni dz$^{2}$', save=False, Emin = -2, Emax = 2)
W.BS_Plotter()
