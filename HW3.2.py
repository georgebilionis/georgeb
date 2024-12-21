def temperatureRange(readings):
    return (min(readings), max(readings))


readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings))