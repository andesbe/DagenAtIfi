# Reading data.txt
with open('data.txt','r') as fd:
    contents = str(fd.read())
    fd.close()
vowels = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"] 
def count_vowels(txt_file):
    """ Function that counts the number of vowels in a string
    Args:
        txt_file .txt: Text file containing a string
    Returns:
        int: Counter with the number of vowels in given string.
    """
    txt_file = txt_file.lower()
    counter = 0
    for letter in txt_file:
        if letter in vowels:
            counter += 1
    return counter
answer = count_vowels(contents)
print(f"Number of vowels in data.txt: \t {answer}")