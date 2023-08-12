Vowel_List = ['a','e','i','o','u']

def Vowel_Check(letter,LIST):
    letter_lower=letter.lower()
    for x in LIST:
        if(letter_lower == x):
            return True
        else:
            continue
    return False
    

letter = input("Enter the letter for check ")
print(Vowel_Check(letter,Vowel_List))
