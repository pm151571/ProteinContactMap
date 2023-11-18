from Bio.PDB import PDBParser
from Bio.PDB.NeighborSearch import NeighborSearch
import matplotlib.pyplot as plt

prot_id="2BGL"
def calculate_contact_map(pdb_id, threshold=8.0):
    pdb_file = f"{pdb_id}.pdb"  # Możesz pobrać PDB z RCSB PDB

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, pdb_file)

    ca_atoms = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.get_id()[0] == ' ' and 'CA' in residue:
                    ca_atoms.append(residue['CA'])

    contact_map = {atom: [] for atom in ca_atoms}
    ns = NeighborSearch(ca_atoms)

    for atom in ca_atoms:
        neighbors = ns.search(atom.get_coord(), radius=threshold, level='R')
        for neighbor in neighbors:
            if neighbor != atom:
                contact_map[atom].append(neighbor)

    return contact_map

# Użycie funkcji do obliczenia mapy kontaktów
contact_map_prot = calculate_contact_map(prot_id, threshold=8.0)

def plot_contact_map_scatter(contact_map):
    contact_counts = [len(contacts) for contacts in contact_map.values()]
    x_values = range(len(contact_counts))

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, contact_counts, color='blue', alpha=0.7)
    plt.xlabel('Indeks atomu CA')
    plt.ylabel('Liczba kontaktów')
    plt.title('Scatter plot mapy kontaktów dla białka')

    plt.show()

# Użycie funkcji do wygenerowania scatter plotu na podstawie mapy kontaktów
plot_contact_map_scatter(contact_map_prot)