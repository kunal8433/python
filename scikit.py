from sklearn.linear_model import LinearRegression

# data
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

# model
model = LinearRegression()
model.fit(X, y)

# prediction
print(model.predict([[5]]))
