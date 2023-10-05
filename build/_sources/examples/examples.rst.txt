================
Further analysis
================

Custom bonds
============

Custom bonds can be analyzed too.

.. code-block:: python
    
    import ase.io
    from ase.vibrations.vibrations import VibrationsData
    import numpy as np
    from jedi.jedi import Jedi
    from jedi.jedi import get_hbonds

    mol=ase.io.read('opt.json')
    mol2=ase.io.read('dis.json')
    modes=VibrationsData.read('modes.json')
    j=Jedi(mol,mol2,modes)
    j.add_custom_bonds(get_hbonds(mol))
    
    j.run()
    j.vmd_gen()

.. image:: hcnhbond.png
    :width: 20%

.. image:: hcnhbondbar.png
    :width: 10%

Analysis of a substructure
==========================

From the above we can get an analysis of only a part of the structure by giving the indeices of the desired atoms

.. code-block:: python

    j.run(indices=[12,17,14,18,23,20,16,15,13,22,21,19,0,5,2,6,11,8,4,3,1,10,9,7])
    j.vmd_gen()

.. image:: hcnparthbond.png
    :width: 20%

.. image:: hcnhbondbar.png
    :width: 10%

Or using a Hessian calculated for only the substructure with:

.. code-block:: python
    
    modes=VibrationsData.from_2d(mol,np.loadtxt('partH'),indices=[12,17,14,18,23,20,16,15,13,22,21,19,0,5,2,6,11,8,4,3,1,10,9,7])
    j=Jedi(mol,mol2,modes)
    j.add_custom_bonds(get_hbonds(mol))
    
    j.run()
    j.vmd_gen()