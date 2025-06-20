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

polynomial_model = PolynomialFeatures(degree=4)

X_poly = polynomial_model.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, Y)

experience = np.array([[8]]) # creer un tableau 2d 
experience_poly = polynomial_model.transform(experience) # transormer sous forme matricielle 
print(experience_poly)
predicted_salary = model.predict(experience_poly) # l'utiliser dans le model linear pour predicter 
print(Y)
print(f"8 years of experience: {predicted_salary[0]:.2f}")





