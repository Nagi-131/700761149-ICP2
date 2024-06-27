from collections import defaultdict
import string
from google.colab import drive

drive.mount('/content/gdrive')

word_count = defaultdict(int)

def count_words(line):
    
    words = line.strip().split()
    for word in words:
        
        word = word.strip(string.punctuation)
        if word:
            word_count[word] += 1
            
    return word_count


input_file = "/content/gdrive/My Drive/input.txt"
output_file = "/content/gdrive/My Drive/output.txt"

try:
    with open(input_file, 'r') as f:
        lines = f.readlines()
    with open(output_file, 'w') as f_out:

        for line in lines:
          print(line.strip())
          print(line.strip(), file=f_out)
        print("Word_Count:")
        print("Word_Count:", file=f_out)
        for line in lines:
            
            word_count = count_words(line)
            
        for word, count in word_count.items():
          print(f"{word}: {count}")
          print(f"{word}: {count}", file=f_out) 
            
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
