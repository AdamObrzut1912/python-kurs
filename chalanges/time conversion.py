def convertToSeconds(hours, minutes):
    seconds = 0
    seconds += hours * 3600
    seconds += minutes * 60
    return seconds

def convertToHours(minutes):
    hours = 0
    hours =+ minutes / 60
    return hours

print(convertToSeconds(3,25))
print(convertToHours(120))