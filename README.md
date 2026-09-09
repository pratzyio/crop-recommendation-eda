# crop-recommendation-eda
# Exploratory Data Analysis - Crop Recommendation Dataset

This project performs an exploratory data analysis (EDA) on the publicly
available **Crop Recommendation Dataset**, examining soil and weather
variables to understand patterns relevant to crop selection and
agribusiness planning.

## Project Summary

This report presents an exploratory data analysis (EDA) of the Crop
Recommendation Dataset, a publicly available agricultural dataset
comprising 2,200 records across 22 balanced crop categories, with 100
observations per crop. The dataset contains seven numerical features —
Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, soil
pH, and rainfall — describing the soil and climatic conditions associated
with different crops.

The analysis begins by examining the dataset's structure, confirming it
is clean, complete, and balanced across all crop labels. Univariate
analysis explores the distribution, mean, and range of each feature,
revealing considerable variation in rainfall and potassium in particular.
Bivariate analysis then investigates the relationship between phosphorus
and potassium, identifying a strong positive correlation (approximately
0.86) consistent with figures reported in published research on this
dataset. Four supporting visualizations — covering feature means, value
ranges, crop-category distribution, and the phosphorus–potassium
relationship — illustrate these findings.

The report concludes by discussing practical implications for
agribusiness decision-making, emphasizing that soil and climate variables
should be considered jointly rather than individually. It also outlines
the dataset's limitations, such as the absence of yield and time-series
data, and suggests directions for future analysis that could incorporate
pricing, location, and seasonal weather information.

## Dataset

- **Source:** [Crop Recommendation Dataset on Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- **Records:** 2,200
- **Crop categories:** 22 (100 records each, balanced)
- **Features:** N, P, K, temperature, humidity, ph, rainfall
- **Target:** `label` (crop name)

Download `Crop_recommendation.csv` from the Kaggle link above and place
it in the project root before running the script.

## Project Structure

```
.
├── crop_eda.py                          # main analysis script
├── requirements.txt                     # Python dependencies
├── README.md
├── Humanized_Agricultural_EDA_Report.docx  # full written report
└── figures/                             # generated charts (created on run)
```

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add the dataset CSV (see Dataset section above)

# 4. Run the analysis
python crop_eda.py
```

The script prints summary statistics to the console and saves five
figures (feature means, feature ranges, crop distribution, P–K scatter,
and a full correlation heatmap) as PNG files.

## Key Findings

- The dataset is clean and perfectly balanced (100 samples per crop).
- Rainfall and potassium show the widest variation among features.
- Phosphorus and potassium are strongly positively correlated (~0.86).
- Soil and climate variables are more informative for crop suitability
  when considered together rather than individually.

## Author

<Pratikshya Prusty>
