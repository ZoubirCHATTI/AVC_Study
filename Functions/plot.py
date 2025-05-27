
import seaborn as sb  
import matplotlib.pyplot as plt
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
