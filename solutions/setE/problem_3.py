score = int(input().strip())

if score < 0 or score > 500:
    print("Invalid AQI")
else:
    if score <= 50:
        status = "Good"
    elif score <= 100:
        status = "Moderate"
    elif score <= 150:
        status = "Unhealthy for Sensitive Groups"
    elif score <= 200:
        status = "Unhealthy"
    elif score <= 300:
        status = "Very Unhealthy"
    else:
        status = "Hazardous"
    print(f"AQI: {score} | Status: {status}")
