
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sb
import matplotlib.pyplot as plt
def cla_repo(Y_test, Y_predicted):
  print(classification_report(Y_test, Y_predicted))

def conf_mat(Y_test, Y_predicted, annot='d', cmap='viridis'):
  cm=confusion_matrix(Y_test, Y_predicted)
  sb.heatmap(data=cm, annot=True, fmt=annot, cmap=cmap)
  plt.xlabel('Valeurs réelle')
  plt.ylabel('Valeurs prédites')
  plt.title('Matrice de confusion')
