
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def L_R(X, Y, test_size, max_ite):
  Y = Y.values.ravel()
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=42, stratify=Y)
  model = LogisticRegression(max_iter=max_ite, class_weight='balanced') 
  model.fit(X_train, Y_train)
  Y_predict = model.predict(X_test)
  return Y_predict, Y_test

def R_F_C(X, Y, test_size, n_estimators, class_weight):
  Y = Y.values.ravel()
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=42, stratify=Y)
  rf = RandomForestClassifier(n_estimators=n_estimators, random_state=42, class_weight=class_weight)
  rf.fit(X_train, Y_train)
  Y_predict = rf.predict(X_test)
  return Y_predict, Y_test

