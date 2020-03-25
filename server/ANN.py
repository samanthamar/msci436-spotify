from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from get_data import X,Y

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y.ravel(), test_size=0.2)
# Scale data
scaler = StandardScaler()
# Only fit to training data 
scaler.fit(X_train)
# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
# NOTE: this is used for our testing only 
X_test = scaler.transform(X_test)

def train(): 
    # Train the model
    print("===============Training ANN===============")
    nn = MLPClassifier(activation='relu', solver='sgd', hidden_layer_sizes=(6), max_iter=500)
    nn.fit(X_train, Y_train)
    print("===============Training complete=============")
    # return the neural network
    return nn 

def predict(nn, X_predict): 
    '''
    Predict the popularity score from user 
    '''
    print("===============PREDICTING===============")
    # scale the input
    X_predict = scaler.transform(X_predict)
    predict_test = nn.predict(X_predict)
    print("===============Prediction complete===============")
    # Cast to an int 
    return int(predict_test[0])

def check_model():
    '''
    Used to check the accuracy of our model 
    '''
    nn = train()
    # Test the model
    predict_train = nn.predict(X_train)
    predict_test = nn.predict(X_test)
    # Check accuracy
    from sklearn.metrics import classification_report,confusion_matrix
    print(confusion_matrix(Y_train,predict_train))
    print(classification_report(Y_train,predict_train))

# check_model()