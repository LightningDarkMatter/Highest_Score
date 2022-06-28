scores = input("Enter a list of scores: ").split()
for n in range (0, len(scores)):
    scores[n] = int(scores[n])
print(scores)

high_score = 0

for i in range(0, len(scores)):
    if scores[i] > high_score:
        high_score = scores[i]
    else: 
        high_score = high_score

print("The highest score is: ", high_score)
