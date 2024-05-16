import os

print("-----------Word_Frequency_analyzer----------")
file_path = input("Enter the path to the text file: ")
if not os.path.exists(file_path):
    print("Error: File not found.")
    exit()

file_descriptor = open(file_path, "r" )
data = file_descriptor.read()
file_descriptor.close()


special_chars = "_,.!?"
for char in special_chars:
  data = data.replace(char, "")
word_list = data.split()


word_count = {}
for word in word_list:
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
    
print("All Present Words are")
for word, count in word_count.items():
  print(f"'{word}' occurs {count} times")
print(f"\n\n The number Of words are {len(word_count)}")
 