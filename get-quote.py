import random #To generate random numbers, we'll use a Python module, a built-in extension of the language.

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = 13
  rnd = random.randint(0, last)
  # The last variable holds the highest index for the array. Then our random number is stored in rnd using the random.randint function, which takes the lowest-possible number (zero) and the highest-possible number (stored in last).
  #  If you want to add or remove quotes from your text file, you could change the last variable to update automatically:
  # last = len(quotes) - 1
  
  print(quotes[rnd])

if __name__== "__main__":
  primary()
