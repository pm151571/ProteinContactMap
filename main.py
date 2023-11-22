import Bio.PDB
import numpy as np
import pylab

pdb_code = "2HHB"
pdb_filename = "2hhb.pdb"

def calculate_distance(x, y):
    if 'CA' in x and 'CA' in y:
        roznica = x['CA'].coord - y['CA'].coord
        if np.sqrt(np.sum(roznica * roznica)) <= 8:
            return np.sqrt(np.sum(roznica * roznica))
        else:
            return None
    else:
        return None

def calculate_distance_matrix(chain):
    x = np.zeros((len(chain), len(chain)), float)
    for row, residue_row in enumerate(chain):
        for col, residue_col in enumerate(chain):
            x[row, col] = calculate_distance(residue_row, residue_col)
    return x

structure = Bio.PDB.PDBParser().get_structure("lancuchy", pdb_filename)
model = structure[0]
chain_A = model["A"]
distance_matrix = calculate_distance_matrix(chain_A)

print(distance_matrix)
pylab.matshow(np.transpose(distance_matrix))
pylab.colorbar()
pylab.show()
