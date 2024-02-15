def main():
 book_Path = "book/franks.txt"
 file_content = read_file(book_Path)
 word_num = word_count(file_content)
 letter_num = letter_count(file_content)
 print(f"--- Begin report of {book_Path} ---")
 print(f"the book has {word_num} words.")
 for letter in letter_num:
     print(f"the letter {letter} was found {letter_num[letter]} times.")
 print("--- End report ---")    

def read_file(path):
    with open(path) as f:
      return f.read()
    
def word_count(text):
    return len(text.split())
 
def letter_count(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
       if letter.isalpha():
            letter_count[letter] = letter_count.get(letter,0 )+1
       

          
    return letter_count
    
main()   

 