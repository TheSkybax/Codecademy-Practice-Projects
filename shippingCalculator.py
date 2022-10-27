weight = 4.8

# Ground Shipping
if weight <= 2:
    print("Your package will cost $" + str(weight * 1.5 + 20),
          "to ship with Ground Shipping.")
elif weight > 2 and weight <= 6:
    print("Your package will cost $" + str(weight * 3 + 20),
          "to ship with Ground Shipping.")
elif weight > 6 and weight <= 10:
    print("Your package will cost $" + str(weight * 4 + 20),
          "to ship with Ground Shipping.")
else:
    print("Your package will cost $" + str(weight * 4.75 + 20),
          "to ship with Ground Shipping.")

# Ground Premium
premium = 125
print("Premium shipping is a flat rate of $" +
      str(premium), "regardless of weight.")

# Drone Shipping
if weight <= 2:
    print("Your package will cost $" + str(round(weight * 4.5, 2)),
          "to ship with Drone Shipping.")
elif weight > 2 and weight <= 6:
    print("Your package will cost $" + str(round(weight * 9, 2)),
          "to ship with Drone Shipping.")
elif weight > 6 and weight <= 10:
    print("Your package will cost $" + str(weight * 12),
          "to ship with Drone Shipping.")
else:
    print("Your package will cost $" + str(weight * 14.25),
          "to ship with Drone Shipping.")
