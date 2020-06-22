import numpy as np
import normalizer as norm
from load_data import load_csv

base_path = '/home/daniel/Documentos/Projetos/TCC/Normalizador/tests'  # Trocar por caminho relativo do projeto.

raw_data = load_csv(f'{base_path}/raw_data.csv')
normalized = norm.normalizer(raw_data)

np.savetxt(f'{base_path}/normalized.csv', normalized, fmt='%.8f')

print(normalized)
