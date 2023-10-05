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
    Analysis of strain energy stored in redundant internal modes.

    atoms: class 
        An ASE Atoms object to determine the atomic species of the indices.
    rim_list: list
        A list of 4 numpy 2D arrays the first array containing bonds, second custom bonds, third bond angles, fourth dihedrals.
    B: np array
        B matrix.
    H_cart: np array
        Hessian in cartesian coordinates.
    delta_q: np array
        Array of deformations along the RICs.
    E_geometries: float
        Energy difference between the geometries.
    printout: bool
        Flag to print the output.
    ase_units: bool
        Flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians.
    Returns:
        Analysis of RIMs.
    '''
    pass
def jedi_printout(atoms,rim_list,delta_q,E_geometries, E_RIMs_total, proc_geom_RIMs,proc_E_RIMs, E_RIMs,ase_units=False):
    '''
    Printout of analysis of stored strain energy in redundant internal modes.

    atoms: class
        An ASE Atoms object to determine the atomic species of the indices.
    rim_list: list
        A list of 4 numpy 2D arrays the first array containing bonds, second custom bonds, third bond angles, fourth dihedrals.
    delta_q: np array
        Array of deformations along the RICs.
    E_geometries: float
        Energy difference between the geometries.
    E_RIMs_total: float
        Calculated total strain energy by jedi.
    proc_geom_RIMs: float
        Percentage deviation between calculated total energies.
    proc_E_RIMs: array
        Array of energy stored in each RIC.
    ase_units: bool
        Flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians. 
    '''
    pass

def jedi_printout_bonds(atoms,rim_list,E_geometries, E_RIMs_total, proc_geom_RIMs,proc_E_RIMs, E_RIMs,ase_units=False,file='total'):
    '''
    Printout of analysis of stored strain energy in the bonds.

    atoms: class
        An ASE Atoms object to determine the atomic species of the indices.
    rim_list: list
        A list of 4 numpy 2D arrays the first array containing bonds, second custom bonds, third bond angles, fourth dihedrals.
    delta_q: np array
        Array of deformations along the RICs.
    E_geometries: float
        Energy difference between the geometries.
    E_RIMs_total: float
        Calculated total strain energy by jedi.
    proc_geom_RIMs: float
        Percentage deviation between calculated total energies.
    proc_E_RIMs: np array
        Array of energy stored in each RIC.
    ase_units: bool
        Flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians. 
    file: string
        File to store the output.

    '''
    pass
def get_hbonds(mol):
    '''
    Get all hbonds in a structure.
    Hbonds are defined as the HY bond inside X-H···Y where X and Y can be O, N, F and the angle XHY is larger than 90° and the distance between HY is shorter than 0.9 times the sum of the vdw radii of H and Y.

    mol: class
        Structure of which the hbonds should be determined.
    returns
        2D array of indices.
    '''
    pass
@jsonable('jedi')
class Jedi:
    def __init__(self, atoms0, atomsF, modes, hbond=None): #indices=None
        '''

        atoms0: class
            Atoms object of relaxed structure with calculated energy.
        atomsF: class
            Atoms object of strained structure with calculated energy.
        modes: class
            VibrationsData object with hessian of relaxed structure.
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

    def run(self,indices=None,ase_units=False):
        """Runs the analysis. Calls all necessary functions to get the needed values.

        Args:
            indices: 
                list of indices of a substructure if desired
            ase_units: boolean
                flag to get eV for energies å fo lengths and degree for angles otherwise it is kcal/mol, Bohr and radians 
        Returns:
            Indices, strain, energy in every RIM

        """
        pass
        




    def get_rims(self,mol):
        '''Gets the redundant internal coordinates.

        '''        
        pass
    def get_common_rims(self):
        '''Get only the RIMs that are in both structures because bond breaks cannot be analysed logically.

        '''        
        pass
    def get_hessian(self):
        '''Calls the hessian from the VibrationsData object.
        '''        
        pass
    
    def get_b_matrix(self,indices=None):
        '''Calculates the derivatives of the RICs with respect to all cartesian coordinates using ASE functions.

        '''    
        
        pass
    def get_energies(self):
        '''Calls the energies of the Atoms objects.

            Returns: 
                [energy difference, energy of atoms0, energy of atomsF]

        '''    
        pass
        
    def get_delta_q(self):
        '''get the strain in RICs substracts the values of the relaxed structure from the strained structure
        
            Returns: 
                2D array of the values.
        '''
        pass
    def vmd_gen(self,des_colors=None,box=False,man_strain=None,modus=None,colorbar=True):
        '''generates vmd scripts and files to save the values for the color coding

        Args:
            des_colors: (dict)
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
        Analyse a substructure with given indices. 

        Args:
            indices: 
                list of indices of atoms in desired substructure
        '''
        pass
      
    def post_process(self,indices):             #a function to get segments of all full analysis for better understanding of local strain
        '''
        get only the values of RICs inside a defined substructure

        Args:
            indices: 
                list of indices of atoms in desired substructure
        Returns:
            Values for analyzed RIMs in the defined substructure
        '''
        pass
    
    def add_custom_bonds(self, bonds):
        '''Add custom bonds after creating the object.
        
        Args:
            bonds: 
                2Darray
            '''