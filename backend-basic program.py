import json
from sklearn.naive_bayes import GaussianNB
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

prcp_df = pd.read_csv("D:\Projects\movis expo\precip_training data.csv")


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
new_data_point = [[17, 0.7]]  


predicted_class = clf.predict(new_data_point)

print("Predicted Class:", predicted_class[0])
accuracy = accuracy_score(y_test, predicted_labels)
print("Accuracy:", accuracy)

'''
# Initialize data structures to store farm and water source information
farm = {
    'fields': []
}

water_sources = []

# Function to add a field to the farm
def add_field():
    field_name = input("Enter field name: ")
    crop_type = input("Enter crop type: ")
    area = float(input("Enter field area (acres): "))
    irrigation_schedule = input("Enter irrigation schedule (e.g., daily, weekly): ")

    field = {
        'name': field_name,
        'crop_type': crop_type,
        'area': area,
        'irrigation_schedule': irrigation_schedule
    }

    farm['fields'].append(field)

# Function to add a water source
def add_water_source(rain, gw):
    source_name = input("Enter water source name: ")
    capacity = float(input("Enter water source capacity (gallons): "))
    current_level = float(input("Enter current water level (gallons): "))

    source = {
        'name': source_name,
        'capacity': capacity,
        'current_level': current_level
    }

    water_sources.append(source)

# Main menu
while True:
    print("\nWater Resource and Management Tracking Software")
    print("1. Add Field")
    print("2. Add Water Source")
    print("3. View Farm Information")
    print("4. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        add_field()
    elif choice == '2':
        add_water_source()
    elif choice == '3':
        print("\nFarm Information:")
        print("Fields:")
        for field in farm['fields']:
            print(f"- {field['name']}: Crop: {field['crop_type']}, Area: {field['area']} acres, Schedule: {field['irrigation_schedule']}")
        
        print("\nWater Sources:")
        for source in water_sources:
            print(f"- {source['name']}: Capacity: {source['capacity']} gallons, Current Level: {source['current_level']} gallons")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Save data to JSON files for future use
with open('farm.json', 'w') as farm_file:
    json.dump(farm, farm_file)

with open('water_sources.json', 'w') as water_sources_file:
    json.dump(water_sources, water_sources_file)
'''