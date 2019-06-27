#guess game

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else :
        out_of_guesses = True

if out_of_guesses:   
    print("you lose")
else :
    print("you win")


#for loops

for letter in 'Computer Science':
    print(letter)

friends = ['chandan', 'nihal', 'pragati']
for friend in friends:
    print(friend)
    
for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(index)

def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result*base
    return result

print(raise_to_power(2, 3))
