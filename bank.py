#[1]
import pandas as pd
import seaborn as sns

#[2]
df = pd.read_csv("Dataset/Churn_Modelling.csv")

#[3]
df.shape

#[4]
df.columns

#5
df.head()

#[6]

    # Input Data
    x = df[['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']]

    # Output Data
    y = df['Exited']

#[7] 
x

#[8]
sns.countplot(x = y);

#[9]
y.value_counts()

#[10]
from imblearn.over_sampling import RandomOverSampler

#[11]
ros = RandomOverSampler(random_state=0)

#[12]
x_yes, y_res = ros.fit_resample(x, y)

#[13]
y_res.value_counts()

#[14]
    # Normalize
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()

#[15] 
x_scaled = scaler.fit_transform(x)

#[16]
x_scaled

#[17]
  # Cross validation
  from sklearn.model_selection import train_test_split
  x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.25)

#[18]
x.shape

#[19]
x_test.shape

#[20]
x_train.shape

#[21]
from sklearn.neural_network import MLPClassifier

#[22]
ann = MLPClassifier(hidden_layer_sizes=(100, 100, 100), random_state=0, max_iter=100, activation='relu')

#[23]
ann.fit(x_train, y_train)

#[24]
y_pred = ann.predict(x_test)

#[25]
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
from sklearn.metrics import accuracy_score

#[26]
y_test.value_counts()

#[27]
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

#[28]
accuracy_score(y_test,y_pred)

#[29]
print(classification_report(y_test, y_pred))
