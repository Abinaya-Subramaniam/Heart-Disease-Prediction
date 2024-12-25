# Predict Heart Disease

This predicts whether a person has heart disease based on various health parameters. The model is trained using the Cleveland heart disease dataset from the UCI Machine Learning Repository. 

## Data Source
The dataset used is the Cleveland dataset from the UCI Machine Learning Repository. You can access it [here](https://archive.ics.uci.edu/ml/datasets/heart+Disease).

## Data Dictionary

- **age**: Age in years.
- **sex**: (1 = male; 0 = female).
- **cp**: Chest pain type:
  - 0: Typical angina: chest pain related to decreased blood supply to the heart.
  - 1: Atypical angina: chest pain not related to the heart.
  - 2: Non-anginal pain: typically esophageal spasms (non-heart related).
  - 3: Asymptomatic: chest pain not showing signs of disease.
- **trestbps**: Resting blood pressure (in mm Hg on admission to the hospital). Typically, a value above 130-140 is a cause for concern.
- **chol**: Serum cholesterol in mg/dl. Serum = LDL + HDL + 0.2 * triglycerides. Values above 200 are a cause for concern.
- **fbs**: (Fasting blood sugar > 120 mg/dl) (1 = true; 0 = false). Values above 126 mg/dL signal diabetes.
- **restecg**: Resting electrocardiographic results:
  - 0: Nothing to note.
  - 1: ST-T Wave abnormality, can range from mild symptoms to severe problems indicating a non-normal heartbeat.
  - 2: Possible or definite left ventricular hypertrophy (enlarged heart's main pumping chamber).
- **thalach**: Maximum heart rate achieved.
- **exang**: Exercise-induced angina (1 = yes; 0 = no).
- **oldpeak**: ST depression induced by exercise relative to rest. Looks at stress on the heart during exercise (unhealthy hearts will stress more).
- **slope**: The slope of the peak exercise ST segment:
  - 0: Upsloping: better heart rate with exercise (uncommon).
  - 1: Flatsloping: minimal change (typical healthy heart).
  - 2: Downsloping: signs of an unhealthy heart.
- **ca**: Number of major vessels (0-3) colored by fluoroscopy. A colored vessel means the doctor can see the blood passing through, which is a sign of good blood movement (no clots).
- **thal**: Thallium stress result:
  - 1, 3: Normal.
  - 6: Fixed defect (used to be a defect but is now fine).
  - 7: Reversible defect (no proper blood movement when exercising).
- **target**: Target variable indicating whether the person has heart disease (1 = yes, 0 = no).

## Installation

1. Clone the repository:
   git clone https://github.com/Abinaya-Subramaniam/predict-heart-disease.git
   cd predict-heart-disease
2.Install the required dependencies:
  pip install -r requirements.txt
3.Run the app:
  streamlit run app.py
