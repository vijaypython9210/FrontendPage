l = input("Input a letter of the alphabet: ")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("alphabet is a vowel." , l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("alphabet is a consonant." , l)
