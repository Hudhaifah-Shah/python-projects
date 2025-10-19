import random
word_list = ["aardvark", "baboon", "camel"]
lives = 7
word = random.choice(word_list)
pr_word = "_" * len(word)
pr_word = list(pr_word)
while lives > 0 and ("_" in pr_word):
    prt_word = " ".join(pr_word)
    letter = input(f"{prt_word}, guess a letter: ").strip().lower()
    if letter in word:
        ind_letter = [i for i, val in enumerate(word) if val==letter]
        for i in ind_letter:
            pr_word[i] = letter
    else:
        lives -= 1
        print(f"Wrong! You have {lives} left")
prt_word = " ".join(pr_word)
if lives > 0:
    print(f"{prt_word}\nYou win!")
else:
    print(f"You lose! The correct word was {word}")

