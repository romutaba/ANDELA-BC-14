def words(string):
  #split the input words and assign to a new empty list
  new_list = string.split()
  #create a new dictionary
  string_dict = {}
  #iterate through list 
  for word in new_list:
    #convert character to Integer if it is a digit
    if word.isdigit(): 
      word = int(word)
    #count each word occurrence 
    if word in string_dict:
      string_dict[word] +=  1
    else:
      string_dict[word] = 1
  return string_dict

print (words("car 8 carpet as java : javascript!!&@$%^&"))
print (words("3"))