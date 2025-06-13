from sklearn.linear_model import LinearRegression 
import pandas as pd
# example of linear reqgression probleme and solution => Predicting salary based on years of experience.

# load the file 
data = pd.read_excel("ML/Regression/salary.xlsx")

# extract data from the file Y = aX + b => on veut une estimation de Y a n'importe quel valeur de X 
X = data[["Experience"]] 
Y = data["Salary"]

# en se basant sur l'experience on prevoie un salaire => entrainer le modele    
model = LinearRegression()
model.fit(X , Y)

#on test 
test = model.predict([[4]])

print("la valeur estimé pour 4 ans :  ")
print(test)
