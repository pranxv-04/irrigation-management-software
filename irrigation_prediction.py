from sklearn.naive_bayes import GaussianNB
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

prcp_df = pd.read_csv("D:\Projects\movis expo\datasets\precip_training data.csv")


clf = GaussianNB()


X = [] 
y = [] 


for index, row in prcp_df.iterrows():
    
    rainfall = row["precipitation_sum (mm)"]
    gw = random.random()
    
    if 0 <= rainfall < 2:
        # no rain
        if gw > 0:
            label = "Groundwater (no rain)"
        elif gw == 0:
            label = "No water source available"
    elif 2 <= rainfall < 5:
        # Little rain
        if gw > 0:
            label = "Groundwater (Little rain)"
        else:
            label = "Little chance of rain"
    elif 5 <= rainfall < 6:
        # Moderate rain
        if gw <= 0.4:
            label = "Moderate chance of rain"
        else:
            label = "Groundwater (Moderate rain)"
    elif 6 <= rainfall < 15:
        # Rainfall
        label = "Rain"
    elif 15 <= rainfall < 20:
        label = "Strong Rain"
    elif 20 <= rainfall < 40:
        label = "Heavy Rainfall. Take care."
    else:
        label = "Flood Warning"

    X.append([rainfall, gw])
    y.append(label)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf.fit(X_train, y_train)

predicted_labels = clf.predict(X_test)

'''
new_data_point = [[17, 0.7]]  


predicted_class = clf.predict(new_data_point)

print("Predicted Class:", predicted_class[0])
accuracy = accuracy_score(y_test, predicted_labels)
print("Accuracy:", accuracy)
'''


'''
Light rain gives up to 2-4 mm (0.07-0.15 in) of precipitation;
Moderate rain gives 5-6 mm (0.19-0.23 in);
Rain or strong rain gives up about 15-20 mm (0.59-0.78 in);
Rainfall gives more than 30 mm (1.18 in)

Test change

'''


