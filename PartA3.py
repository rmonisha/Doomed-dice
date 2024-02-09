combinations = {}
diceLength = 6
for i in range(1,diceLength+1):
    for j in range(1,diceLength+1):
        combinations[i+j] = combinations.get(i+j, 0) + 1
print("Distribution of all possible combinations when rolling both dice:")
print("Total\tFrequency\tProbability")
for total, frequency in combinations.items():
    print(total,"\t",frequency,"\t\t",frequency/36)