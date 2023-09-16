"""A class for Jedi analysis"""

import collections
import numpy as np
import ase.neighborlist
import ase.geometry
from collections import Counter
from typing import  Any, Dict
from ase.atoms import Atoms
from ase.vibrations import VibrationsData
from ase.atoms import Atom
from ase.utils import jsonable
import os
import ase.io
import scipy
from ase.units import Hartree, Bohr, mol, kcal
def jedi_analysis(atoms,rim_list,B,H_cart,delta_q,E_geometries,printout=None,ase_units=False):
    '''
    '''
    pass
def jedi_printout(atoms,rim_list,delta_q,E_geometries, E_RIMs_total, proc_geom_RIMs,proc_E_RIMs, E_RIMs,ase_units=False):
    '''
    '''
    pass

def jedi_printout_bonds(atoms,rim_list,E_geometries, E_RIMs_total, proc_geom_RIMs,proc_E_RIMs, E_RIMs,ase_units=False,file='total'):
    '''
    '''
    pass
def get_hbonds(mol):
    '''
    '''
    pass
@jsonable('jedi')
class Jedi:
    def __init__(self, atoms0, atomsF, modes, hbond=None): #indices=None
        '''
    '''
        pass
    def todict(self) -> Dict[str, Any]:
        '''
    '''
        pass
    @classmethod
    def fromdict(cls, data: Dict[str, Any]) -> 'Jedi':
        '''
    '''
        pass

    def run(self,indices=None,ase_units=False,hbond=True):
        pass
        




    def get_rims(self,mol,hbond=True):
        '''
    '''        
        pass
    def get_common_rims(self,hbond=True):
        '''
    '''        
        pass
    def get_hessian(self):
        '''
    '''        
        pass
    
    def get_b_matrix(self,indices=None):
        '''
    '''    
        
        pass
    def get_energies(self):
        '''
    '''    
        pass
        
    def get_delta_q(self):
        '''
    '''
        pass
    def vmd_gen(self,des_colors=None,box=False,man_strain=None,modus=None,colorbar=True):
        '''
    '''
        pass
    def partial_analysis(self,indices,hbond=False,ase_units=False):   
        '''
    '''
        pass
      
    def post_process(self,indices):             #a function to get segments of all full analysis for better understanding of local strain
        '''
    '''
        pass
