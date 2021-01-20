username = input('what is your name?')
password = input('just type your password : ')
lengthPass= len(password)
passwordStars = '*' * lengthPass

print(f'{username}, your password {passwordStars} is {lengthPass} letters long')