appleCount = int(input("How many apples should I remove? "))
applesRemoved = 0
while applesRemoved < appleCount:
    applesRemoved = applesRemoved + 1
    print("Apple Removed")

obstacleCount = int(input("How many obstacles should I avoid? "))
obstaclesAvoided = 0
while obstaclesAvoided < obstacleCount:
    obstaclesAvoided = obstaclesAvoided + 1
    print(f"Avoiding done... {obstaclesAvoided} obstacle(s) avoided!")

print("All obstacles avoided!")

barCount = int(input("How many bars should be charged? "))
barsCharged = 0
chargingBar = "[ ]"

while barsCharged < barCount:
    barsCharged += 1
    chargingBar = "[" + "|" * barsCharged + " " * (barCount - barsCharged) + "]"
    print(f"Charging {chargingBar} ")

print("The battery is fully charged!")
