import json


# Initialize data structures to store farm and water source information
farm = {
    'fields': []
}

water_sources = []

# Function to add a field to the farm
def add_field():
    crop_type = input("Enter crop type: ")
    area = float(input("Enter field area (acres): "))

    field = {
        'crop_type': crop_type,
        'area': area,
    }

    farm['fields'].append(field)

# Function to add a water source
def gw():
    capacity = float(input("Enter ground water capacity: "))
    current_level = float(input("Enter current water level (gallons): "))

    source = {
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
        gw()
    elif choice == '3':
        print("\nFarm Information:")
        print("Fields:")
        for field in farm['fields']:
            print(f"Crop: {field['crop_type']}, Area: {field['area']} acres")
        
        print("\nWater Sources:")
        for source in water_sources:
            print(f"Capacity: {source['capacity']} gallons, Current Level: {source['current_level']} gallons")
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
# To clear contents from json file
data = {}

with open('farm.json', "w") as farm_file:
    json.dump(data, farm_file)
'''