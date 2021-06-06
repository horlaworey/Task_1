# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#         raise ValueError("That is not positive integer!")
# except ValueError as ve:
#     print(ve)

ans = input("What is your name? ")


def nameValidator(name):

    try:
        check = all(char.isalpha() or char.isspace() for char in name)
        split_name = name.split()
        len_of_firstname = len(split_name[0]) >= 5
        len_of_lastname = len(split_name[1]) <= 20
        assert check and len(split_name) == 2 and '' in name and len_of_firstname and len_of_lastname
    except:
        print("Your name must contain only alphabets, a combination of two substrings and a space in between.")
        # The length of the first and last name substrings each must be >= 5 characters and <= 20 characters
    else:
        print("You typed your name correctly.")


nameValidator(ans)
