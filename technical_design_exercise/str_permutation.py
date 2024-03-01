# Write a function that take a string and returns all distinct permutations of a string.
# For example, the following string input 'POP' should return the set 'PPO' 'OPP' 'POP'
# Make sure to document additional example cases.

# clarifications:
# how should blank spaces be handled?
# is there a time complexity?

def str_perms(string):
    '''Returns all possible permutations of a given string.
        >>> str_perms("POP")
        ['POP','PPO','OPP']

    '''

    permutations = []
    i = 0

    list_of_chars = list(string)

    for letter in list_of_chars:
        print(i)
        print(list_of_chars, "list")
        letter = list_of_chars.pop(i)
        print(list_of_chars, "list")
        print(letter, " letter")
        # iterate through mutated list of chars
        #add the letter  at each index and the end
        j = 0
        while(j < len(list_of_chars)):
            list_of_chars.insert(j, letter)
            print(list_of_chars, "mutation")
            list_to_string = "".join(list_of_chars)
            j += 1

            if list_to_string not in permutations:
                print(list_to_string, "list to str in if block")
                permutations.append(list_to_string)
                
        print(permutations, "perms")

        i += 1
    return permutations


# input: string
# output: array of strings
# logic:

# loop - remove letter from place
    # loop through length of string
    # at the index concat the mini string to the large string
    # check if large string is included in permulations
    # no? add it to permutations
# return permutations
