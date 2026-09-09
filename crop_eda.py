"""
Exploratory Data Analysis - Crop Recommendation Dataset
---------------------------------------------------------
This script reproduces the analysis and figures described in the
"Exploratory Data Analysis of a Crop Recommendation Dataset" report.

Dataset source (download the CSV and place it next to this script,
or update the path below):
https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset

Usage:
    pip install -r requirements.txt
    python crop_eda.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------
DATA_PATH = "Crop_recommendation.csv"  # update if your filename differs

df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
print(df.head())
print("\nMissing values per column:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# ---------------------------------------------------------------
# 2. Dataset description table (mean, min, max per feature)
# ---------------------------------------------------------------
summary = df[FEATURES].agg(["mean", "min", "max"]).T
summary.columns = ["mean", "min", "max"]
print("\nSummary statistics:\n", summary.round(2))

# ---------------------------------------------------------------
# 3. Figure 1 - Mean values of the seven agricultural features
# ---------------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.bar(FEATURES, df[FEATURES].mean())
plt.title("Average value of the main agricultural features")
plt.ylabel("Mean value")
plt.tight_layout()
plt.savefig("figure1_feature_means.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 4. Figure 2 - Min / Max / Mean range plot
# ---------------------------------------------------------------
plt.figure(figsize=(9, 5))
means = df[FEATURES].mean()
mins = df[FEATURES].min()
maxs = df[FEATURES].max()
plt.vlines(FEATURES, mins, maxs, color="tab:blue", label="Range")
plt.plot(FEATURES, means, "o", color="tab:blue", label="Mean")
plt.title("Minimum-maximum range and mean")
plt.ylabel("Observed value")
plt.legend()
plt.tight_layout()
plt.savefig("figure2_feature_ranges.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 5. Figure 3 - Crop category distribution
# ---------------------------------------------------------------
plt.figure(figsize=(9, 7))
df["label"].value_counts().sort_values().plot(kind="barh")
plt.title("Crop classes in the dataset")
plt.xlabel("Number of records")
plt.tight_layout()
plt.savefig("figure3_crop_distribution.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 6. Figure 4 - Phosphorus vs Potassium scatter (sample of rows)
# ---------------------------------------------------------------
sample = df.sample(12, random_state=42)

plt.figure(figsize=(10, 7))
plt.scatter(sample["P"], sample["K"], s=80)
for _, row in sample.iterrows():
    plt.annotate(
        row["label"],
        (row["P"], row["K"]),
        textcoords="offset points",
        xytext=(8, 8),
        fontsize=9,
    )
plt.xlabel("Phosphorus (P)")
plt.ylabel("Potassium (K)")
plt.title("Example P-K relationship using sample rows")
plt.tight_layout()
plt.savefig("figure4_p_k_scatter.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 7. Correlation between P and K (full dataset)
# ---------------------------------------------------------------
corr = df[FEATURES].corr()
print("\nP-K correlation (full dataset):", round(corr.loc["P", "K"], 3))

# Optional: full correlation heatmap
plt.figure(figsize=(7, 6))
plt.imshow(corr, cmap="viridis")
plt.colorbar(label="Correlation")
plt.xticks(range(len(FEATURES)), FEATURES, rotation=45)
plt.yticks(range(len(FEATURES)), FEATURES)
plt.title("Correlation heatmap - agricultural features")
plt.tight_layout()
plt.savefig("figure5_correlation_heatmap.png", dpi=150)
plt.close()

print("\nAll figures saved in the current directory.")
