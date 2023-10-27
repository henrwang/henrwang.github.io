import ase.io
from ase.vibrations.vibrations import VibrationsData
import numpy as np
from jedi.jedi import Jedi
from jedi.jedi import get_hbonds
from jedi.io.gaussian import get_vibrations,read_gaussian_out

mol=ase.io.read('opt.log')
ase.io.write('test.json',mol)
mol2=ase.io.read('dist.log')
modes=get_vibrations('freq',mol)#VibrationsData.from_2d(mol,np.loadtxt('hes'))
j=Jedi(mol,mol2,modes)
j.add_custom_bonds(get_hbonds(mol))

j.run()
j.vmd_gen()