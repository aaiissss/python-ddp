#Program Print Huruf Konsonan dalam Kata Nurul Fikri
def delVowel(input):
    vowels =['a','i','u','e','o','']
    output =""

    for char in input:
        if char.lower() not in vowels:
            output +=char
    return output

print(delVowel('Nurul Fikri'))