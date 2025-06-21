# Modeling Electricity Consumption in Relation to Temperature 
# => estimer que la consomation s'eleve dans les temperature extermemnt hot/cold et modérée en temperature normaux 

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

# njibo data mn le fichier excel 
salary_data = pd.read_excel("ML/Regression/poly-salary.xlsx")
X = salary_data[["Years of Experience"]] 
Y = salary_data["salary"]

#diviser les données qu'on a en 80% training et 20% test 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

polynomial_model = PolynomialFeatures(degree=2) #degree de polynome 

X_poly_train = polynomial_model.fit_transform(X_train)
X_poly_test = polynomial_model.transform(X_test)

#traoner le modele 
my_model = LinearRegression() 
my_model.fit(X_poly_train , y_train)

train_preds = my_model.predict(X_poly_train)
test_preds = my_model.predict(X_poly_test)

# evaluation , calcule de r2 score => coefficient de determination 
train_score = r2_score(y_train, train_preds)
test_score = r2_score(y_test, test_preds)

print(f"Train R² Score: {train_score:.3f}")
print(f"Test R² Score: {test_score:.3f}")









