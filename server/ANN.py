from matplotlib import pyplot as plt 
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from get_data import X,Y

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Scale data
scaler = StandardScaler()
# Only fit to training data 
scaler.fit(X_train)
# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
nn = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(13), max_iter=500)
nn.fit(X_train, Y_train)

# Test the model
predict_train = nn.predict(X_train)
predict_test = nn.predict(X_test)

# Check accuracy
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(Y_train,predict_train))
print(classification_report(Y_train,predict_train))