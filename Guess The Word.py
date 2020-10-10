master = "hacktoberfest"
word = list(master)
length = len(word)
right = list("_" * length)

while True:
    guess = input("Guess a letter! ")
    
    if guess not in master:
        print("This letter is not in the word!")
    elif len(guess) > 1:
        print("Write single letter at a time!")
        
    for letter in word:
        if guess == letter:
            index = word.index(guess)
            word[index] = "_"
            right[index] = guess
            
    print(right)
        
    if list(master) == right:
        print("You Won!")
        break
