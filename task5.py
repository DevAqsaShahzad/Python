text=str(input())
def reverse(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse(text))
