
guess_me=7

while True:
	guess=int(input('guess a number:'))

	if guess_me<guess:
		print("too high")

	elif guess_me>guess:
		print("too low")

	else:
		print("just right")
	break
