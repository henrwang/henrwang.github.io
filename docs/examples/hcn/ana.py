

from jedi.jedi import Jedi
from dipole import get_hbonds
import ase.io
from ase.vibrations.vibrations import VibrationsData
import os
import numpy as np
from ase.visualize import view
mol=ase.io.read('opt.json')
modes=VibrationsData.read('modes.json')
modes=VibrationsData.from_2d(mol,np.loadtxt('parthess'),indices=[0,4,1,6,10,7])
mol2=ase.io.read('dis.json')
j=Jedi(mol,mol2,modes)
j.add_custom_bonds(get_hbonds(mol))
try: 
    os.makedirs('partdipole')
except:
    pass
os.chdir('partdipole')

#j.run()
j.partial_analysis(indices=[0,4,1,6,10,7])
j.vmd_gen()
