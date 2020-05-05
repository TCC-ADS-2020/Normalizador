import normalizer as norm
from load_data import load_csv

raw_data = load_csv('./tests/raw_data.csv')
normalized = norm.normalizer(raw_data)

print(normalized)
