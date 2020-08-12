import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc('text', usetex = True)
matplotlib.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman, Times']})
matplotlib.rc('xtick', labelsize = 15)
matplotlib.rc('ytick', labelsize = 15)

Ry2eV = 13.6056980659
weight_factor = 100
fermi_energy =0.71518 


spaghetti = open('LaNiO2_dmft.spaghetti_ene', 'r')

fig, ax = plt.subplots()
k = []
E = []
for i, line in enumerate(spaghetti):
    if 'bandindex' not in line:
        line = line.rstrip().lstrip()
        k.append(float(line.split()[3]))
        E.append(float(line.split()[4]))
    else:
        ax.plot(k,E, 'k-')
        kpts = k
        k = []
        E = []

ax.grid(True, which = 'major', axis = 'x', linewidth = 1, linestyle = '-', color = 'k')
ax.yaxis.set_tick_params(which='major', size=7, width=1, direction='inout')
ax.yaxis.set_tick_params(which='minor', size=5, width=1, direction='inout')
ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(1))
ax.set_xticks([0.000, 0.42100, 0.84201, 1.43740, 1.93058, 2.35158, 2.77259, 3.36798])
ax.set_xticklabels([r'$\Gamma$', 'X', 'M', r'$\Gamma$', 'Z', 'R', 'A', 'Z'])
ax.set_xlim([0,3.36798])
ax.set_ylim([-8,6])

with open('LaNiO2_dmft.qtl', 'r') as qtl:
    energy = []
    orbital_weight = []
    colors = []
    for i, line in enumerate(qtl):
        atom = 2
        if i > 7:
            if 'BAND' not in line:
                line = line.lstrip().rstrip()
                if line.split()[1] == str(atom):
                    energy.append((float(line.split()[0]) - fermi_energy)*Ry2eV)
                    if float(line.split()[8]) >= float(line.split()[10]):
                        orbital_weight.append(weight_factor*float(line.split()[8]))
                        colors.append('magenta')
                    else:
                        orbital_weight.append(weight_factor*float(line.split()[10]))
                        colors.append('blue')
            else:
                ax.scatter(kpts, energy, orbital_weight, colors)
                energy = []
                orbital_weight = []
                colors = []
plt.show()
                
