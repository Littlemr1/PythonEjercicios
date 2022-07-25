def is_vocal(c):
    if len(c) == 1:
        vocal = 'aeiou'
        c = c.lower()

        return c in vocal
    else:
        return False


print(is_vocal('i'))
print(is_vocal('I'))
print(is_vocal('z'))
print(is_vocal('ae'))
