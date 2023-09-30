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
    analysis of stored strain energy in redundant internal modes
    atoms: class 
        an ASE Atoms object to determine the atomic species of the indices
    rim_list: list
        a list of 4 numpy 2D arrays the first array containing bonds, second custom bonds, third bond angles, fourth dihedrals
    B: np array
        B matrix
    H_cart: np array
        Hessian in cartesian coordinates
    delta_q: np array
        array of deformations along the RICs
    E_geometries: float
        energy difference between the geometries
    printout: bool
        flag to print the output
    ase_units: bool
        flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians 
    Returns:
        E_RIMs
    '''
    pass
def jedi_printout(atoms,rim_list,delta_q,E_geometries, E_RIMs_total, proc_geom_RIMs,proc_E_RIMs, E_RIMs,ase_units=False):
    '''
    printout of analysis of stored strain energy in redundant internal modes
    Parameters:

    atoms: class
        an ASE Atoms object to determine the atomic species of the indices
    rim_list: list
        a list of 4 numpy 2D arrays the first array containing bonds, second custom bonds, third bond angles, fourth dihedrals
    delta_q: np array
        array of deformations along the RICs
    E_geometries: float
        energy difference between the geometries
    E_RIMs_total: float
        calculated total strain energy by jedi
    proc_geom_RIMs: float
        percentage deviation between calculated total energies 
    proc_E_RIMs: array
        array of energy stored in each RIC
    ase_units: bool
        flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians 
    '''
    pass

def jedi_printout_bonds(atoms,rim_list,E_geometries, E_RIMs_total, proc_geom_RIMs,proc_E_RIMs, E_RIMs,ase_units=False,file='total'):
    '''
    printout of analysis of stored strain energy in the bonds
    atoms: class
        an ASE Atoms object to determine the atomic species of the indices
    rim_list: list
        a list of 4 numpy 2D arrays the first array containing bonds, second custom bonds, third bond angles, fourth dihedrals
    delta_q: np array
        array of deformations along the RICs
    E_geometries: float
        energy difference between the geometries
    E_RIMs_total: float
        calculated total strain energy by jedi
    proc_geom_RIMs: float
        percentage deviation between calculated total energies 
    proc_E_RIMs: np array
        array of energy stored in each RIC
    ase_units: bool
        flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians 
    file: string
        file to store the output
    Returns
        2D array
    '''
    pass
def get_hbonds(mol):
    '''
    get all hbonds in a structure
    defined as X-H···Y where X and Y can be O, N, F and the angle XHY is larger than 90° and the distance between HY is shorter than 0.9 times the sum of the vdw radii of H and Y
    
    returns
        2D array of indices
    '''
    pass
@jsonable('jedi')
class Jedi:
    def __init__(self, atoms0, atomsF, modes, hbond=None): #indices=None
        '''

        atoms0: class
            Atoms object of relaxed structure with calculated energy
        atomsF: class
            Atoms object of strained structure with calculated energy
        modes: class
            VibrationsData object with hessian of relaxed structure 
        '''
        pass
    def todict(self) -> Dict[str, Any]:
        '''make it saveable with .write()

        '''
        pass
    @classmethod
    def fromdict(cls, data: Dict[str, Any]) -> 'Jedi':
        '''make it readable with .read()

        '''
        pass

    def run(self,indices=None,ase_units=False,hbond=True):
        """run the analysis

        Parameters:

        indices: lst
            list of indices of a substructure if desired
        ase_units: 
            flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians 

        """
        pass
        




    def get_rims(self,mol):
        '''get the redundant internal coordinates

        '''        
        pass
    def get_common_rims(self):
        '''get only the RICs in both structures bond breaks cannot be analysed logically

        '''        
        pass
    def get_hessian(self):
        '''calls the hessian from the VibrationsData object
        '''        
        pass
    
    def get_b_matrix(self,indices=None):
        '''calculates the derivatives of the RICs with respect to all cartesian coordinates using ase functions

        '''    
        
        pass
    def get_energies(self):
        '''calls the energies of the Atoms object
        returns [energy difference, energy of atoms0, energy of atomsF]

        '''    
        pass
        
    def get_delta_q(self):
        '''get the strain in RICs substracts the values of the relaxed structure from the strained structure
        returns np array of the values
        '''
        pass
    def vmd_gen(self,des_colors=None,box=False,man_strain=None,modus=None,colorbar=True):
        '''generates vmd scripts and files to save the values for the color coding
        des_colors: dict
            key: order number, value: [R,G,B]
        box: boolean
            True: draw box
            False: ignore box
        man_strain: float
            reference value for the strain energy used in the color scale
            default: 'None'
        modus: str
            defines where to use the man_strain
            default: 'None' 
        colorbar: boolean
            draw colorbar or not
        '''
        pass
    def partial_analysis(self,indices,ase_units=False):   
        '''
        analyse a substructure with given indices
        indices: np.2Darray
            list of indices of atoms in desired substructure
        '''
        pass
      
    def post_process(self,indices):             #a function to get segments of all full analysis for better understanding of local strain
        '''
        get only the values of RICs inside a defined substructure
        indices: np.2Darray
            list of indices of atoms in desired substructure
        '''
        pass
