
import matplotlib.pyplot as plt
import seaborn as sb

def plot(df, Y):
  df_=df.drop(Y, axis=1)
  object_features = df_.select_dtypes(include='object').columns.tolist()
  float_features = df_.select_dtypes(include='float').columns.tolist()
  int_features = df_.select_dtypes(include='int').columns.tolist()

    # Tracé des variables catégorielles (object)
  if object_features:
    plt.figure(figsize=(5 * len(object_features), 5))
    for i, col in enumerate(object_features):
      plt.subplot(1, len(object_features), i + 1)
      sb.countplot(data=df, x=col, hue=Y)
      plt.xlabel(col)
      plt.ylabel(f"Effet de {col} sur AVC")
    plt.tight_layout()
    plt.show()

    # Tracé des variables flottantes (float)
  if float_features:
    plt.figure(figsize=(5 * len(float_features), 5))
    for i, col in enumerate(float_features):
      plt.subplot(1, len(float_features), i + 1)
      sb.histplot(data=df, x=col, hue=Y, kde=True)
      plt.xlabel(col)
      plt.ylabel(f"Effet de {col} sur AVC")
    plt.tight_layout()
    plt.show()

    # Tracé des variables entières (int)
  if int_features:
    plt.figure(figsize=(5 * len(int_features), 5))
    for i, col in enumerate(int_features):
      plt.subplot(1, len(int_features), i + 1)
      sb.countplot(data=df, x=col, hue=Y)
      plt.xlabel(col)
      plt.ylabel(f"Effet de {col} sur AVC")
    plt.tight_layout()
    plt.show()

#Création des histogrammes
def histplot(df, X, Y, name):
  sb.set(style='whitegrid')
  sb.histplot(data=df, x=X, hue=Y)
  plt.xlabel(name)
  plt.ylabel('nombre de cas')
  plt.title(f"Distribution de '{X}' selon '{Y}'")

#Création des bars
def barplot(df , X, Y, name):
  sb.set(style='whitegrid')
  sb.countplot(data=df, x=X, hue=Y)
  plt.xlabel(name)
  plt.ylabel('nombre de cas')
  plt.xticks(rotation=45)
  plt.title(f"Distribution de '{X}' selon '{Y}'")


#Création des camemberts
def camembert(X1,X2, Y, name1, name2):
  label=[f"no {Y}", f" {Y}"]
  n1=X1[Y].value_counts()
  n2=X2[Y].value_counts()
  plt.figure(figsize=(14, 5))
  plt.subplot(1 , 2 , 1)
  plt.pie(n1, autopct='%1.1f%%', explode=(0 , 0.2), labels=label)
  plt.title(name1)
  plt.subplot(1 , 2 , 2)
  plt.pie(n2, autopct='%1.1f%%', explode=(0 , 0.2), labels=label)
  plt.title(name2)
  plt.tight_layout()  

#Création des scatterplot
def scatter(df,X1, X2, Y, name1, name2):
  sb.set(style='whitegrid')
  sb.scatterplot(data=df, x=X1, y=X2, hue=Y)
  plt.xlabel(name1)
  plt.ylabel(name2)
  plt.title(f"Nuage de points:{X1} vs {X2} coloré par {Y}")  
  
