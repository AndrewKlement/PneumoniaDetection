import os
import shutil
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("dataset_labels.csv")

train_df, temp_df = train_test_split(
    df,
    test_size=0.3,
    stratify=df['label'],
    random_state=42
)

val_df, test_df = train_test_split(
    temp_df,
    test_size=0.5,
    stratify=temp_df['label'],
    random_state=42
)

print("Train class distribution:\n", train_df['label'].value_counts(normalize=True))
print("Val class distribution:\n", val_df['label'].value_counts(normalize=True))
print("Test class distribution:\n", test_df['label'].value_counts(normalize=True))

os.makedirs("datasets1", exist_ok=True)
train_df.to_csv("datasets1/train_split.csv", index=False)
val_df.to_csv("datasets1/val_split.csv", index=False)
test_df.to_csv("datasets1/test_split.csv", index=False)

def copy_images(df, split_name, target_root):
    for _, row in df.iterrows():
        src_path = row['filepath']
        label = row['label']
        filename = os.path.basename(src_path)
        dst_dir = os.path.join(target_root, split_name, label)
        os.makedirs(dst_dir, exist_ok=True)
        dst_path = os.path.join(dst_dir, filename)
        shutil.copyfile(src_path, dst_path)

copy_images(train_df, "train", "datasets1")
copy_images(val_df, "val", "datasets1")
copy_images(test_df, "test", "datasets1")

print("Images copied to datasets1/train, val, and test.")