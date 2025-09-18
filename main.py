#WeightConvert2.py
initial_earth_weight=50
lunar_radio=0.165
annual_growth=0.5
print("年份\t地球体重(kg)\t月球体重(kg)")
for year in range(1,11):
    earth_weight=initial_earth_weight+year*annual_growth
    lunar_weight=earth_weight*lunar_radio
    print(f"{year}\t{earth_weight:.2f}\t\t{lunar_weight:.2f}")
