t = float(input())
lb = int(input())

# Convert each quantity into its desired units before calculation
v = 60 * 1600 / 3600
a = v/t
m = lb * 0.45
F = m * a

print("The engine must produce", F, "Newtons of force.") 