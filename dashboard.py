import json
import api
import irrigation_prediction
import crop_details

def mean(x):
    if len(x) == 0:
        return None
    
    total = sum(x)
    return total/len(x)

# Precipitation

precip = []
precip = api.precipitation_levels
temp = api.temperatures
wspeed = api.wind_speeds

mean_precip = mean(precip) # Mean precipitation of two days
mean_temp = mean(temp) # Mean temperature of two days
mean_wspeed = mean(wspeed) # Mean wind speed of two days


# Farm details

with open('farm.json', 'r') as farm_file:
    farm_data = json.load(farm_file)

crop_list = []
area_list = []

for field in farm_data['fields']:
    crop_type = field['crop_type']
    area = field['area']
    crop_list.append(crop_type)
    area_list.append(area)

crop = crop_list[0] # Crop
area = area_list[0] # Area
print(crop)
print(area)
# Groundwater

with open('water_sources.json', 'r') as water_sources_file:
    data = json.load(water_sources_file)

cap = []
cur_lvl = []

for source in data:
    capacity = source['capacity']
    current_level = source['current_level']
    cap.append(capacity)
    cur_lvl.append(current_level)

capacity = mean(cap) # Max capacity of groundwater
current_lvl = mean(cur_lvl) # Current Level of groundwater

current_gw = mean(cur_lvl)/mean(cap) 


# Prediction

data = [[mean_precip,current_gw]]
prediction = irrigation_prediction.clf.predict(data) # prediction 


print(prediction)


