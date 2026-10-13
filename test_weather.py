from weather import get_weather

weather = get_weather()

print("Temperature:", weather["temperature_2m"], "°F")
print("Humidity:", weather["relative_humidity_2m"], "%")