from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
n2 = Atoms('N2', [(0, 0, 0), (0, 0, 1.1)],
            calculator=EMT())
BFGS(n2).run(fmax=0.01)

vib = Vibrations(n2)
vib.run()
modes = vib.get_vibrations()
n2l = n2.copy()
n2l.positions[1][2] = n2.positions[1][2]+0.1
n2l.calc = EMT()
n2l.get_potential_energy()

from jedi.jedi import Jedi

j = Jedi(n2, n2l, modes)

j.run()

