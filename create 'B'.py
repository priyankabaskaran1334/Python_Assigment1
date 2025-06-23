text = input("Enter your text: ")

sentences = text.split('.')  # split by period
count = 0

for sentence in sentences:
    sentence = sentence.strip()  # remove spaces
    if sentence.startswith('B') or sentence.startswith('b'):
        count += 1

print("Sentences starting with B:", count)
