spam = [1, 2, 3, 4]
i = 5

while i < 9002:
	spam.append(i)
	if i == 9001:
		break
	else:
		i += 1

print(spam)