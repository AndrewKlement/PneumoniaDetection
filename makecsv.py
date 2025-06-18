import os
import pandas as pd


root_dir = 'datasets'

data = []

for split in ['train', 'test', 'val']:
    split_dir = os.path.join(root_dir, split)
    
    for label in ['NORMAL', 'PNEUMONIA']:
        label_dir = os.path.join(split_dir, label)
        
        for filename in os.listdir(label_dir):
            file_path = os.path.join(label_dir, filename)
            data.append({'filepath': file_path, 'label': label})


df = pd.DataFrame(data)
df.to_csv('dataset_labels.csv', index=False)

print("CSV saved as 'dataset_labels.csv'")