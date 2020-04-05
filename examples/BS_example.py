import sys
sys.path.apend('/Users/harrisonlabollita/Documents/Coding/W2kPlotter/src/W2kPlotter.py')
import W2kPlotter as W2k
#file2 = '/Users/harrisonlabollita/Documents/Arizona State University/Botana group/Projects/ho_nick/bandstruct/W2k_spaghetti/dz2/5410_k_1000_tot_Ni_dz2.agr'
#file = '/Users/harrisonlabollita/Documents/Arizona State University/Botana group/Projects/ho_nick/bandstruct/W2k_spaghetti/dz2/5410_k_1000_tot_Ni_dz2.spaghetti_ene'
W = W2k.W2kPlotter()
W.BS_Plotter(file, file2, r'5410 Tot Ni dz$^{2}$', save=False, Emin = -2, Emax = 2)
