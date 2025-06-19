# Modeling Electricity Consumption in Relation to Temperature 
# => estimer que la consomation s'eleve dans les temperature extermemnt hot/cold et modérée en temperature normaux 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np

# njibo data mn le fichier excel 
salary_data = pd.read_excel("ML/Regression/poly-salary.xlsx")
X = salary_data[["Years of Experience"]] 
Y = salary_data["salary"]

polynomial_model = PolynomialFeatures(degree=2)
X_poly = polynomial_model.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, Y)

experience = np.array([[7]]) 
experience_poly = polynomial_model.transform(experience)
predicted_salary = model.predict(experience_poly)
print(Y)
print(f"7 years of experience: {predicted_salary[0]:.2f}")

polynomial_model.fit(X_poly, Y)


