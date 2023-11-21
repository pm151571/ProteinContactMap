import Bio.PDB
import numpy as np
import pylab

pdb_code = "2HHB"
pdb_filename = "2hhb.pdb"  # Correct filename for the PDB code "1BOM"

def calculate_distance(a, b):
    if 'CA' in a and 'CA' in b:
        difference = a['CA'].coord - b['CA'].coord
        if np.sqrt(np.sum(difference * difference)) <= 8:
            return np.sqrt(np.sum(difference * difference))
        else:
            return None
    else:
        # Handle the case where 'CA' atom is missing in either residue
        return None  # Or any default value or error handling suitable for your analysis

def calculate_distance_matrix(chain):
    x = np.zeros((len(chain), len(chain)), float)
    for row, residue_row in enumerate(chain):
        for col, residue_col in enumerate(chain):
            x[row, col] = calculate_distance(residue_row, residue_col)
    return x

structure = Bio.PDB.PDBParser().get_structure("chains", pdb_filename)
model = structure[0]
chain_A = model["A"]
distance_matrix = calculate_distance_matrix(chain_A)

print(distance_matrix)
pylab.matshow(np.transpose(distance_matrix))
pylab.colorbar()
pylab.show()
