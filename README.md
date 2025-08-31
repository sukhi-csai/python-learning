WEEK-1
CONCEPTS I LEARNT
*INDEXING & SLICING ->
ACCESSING PARTS OF STRINGS OR LISTS 
example- "Python"
print(text[0]) = P
print(text[1:4])= yth

*STRING METHODS= .upper() = converts to uppercase
name = "amruth"
print(name.upper()) = 'AMRUTH'
.lower() = converts to all the characters in lowercase
name = "Amruth"
print(name.lower()) = 'amruth'
.title()= converts all the alphabet in title format like the first letter in upper case and rest in lower case
for example 
name = "WE ARE LEARNING PYTHON"
print(name.title()) = 'We Are Learning Python'
like a title of movie or whatsoever
SPLIT
.split()= splits a string into a list
a = "we are learning python"
a.split("e") = ('w','ar','l','arning python,)
 OKAY SO FIND & INDEX ARE THE SAME BUT THE ONLY DIFFERENCE I LEARNT IS THAT IF THERES A UNKNOWN DATA SPECIFIED IT THROWS AN ERROR IN INDEX BUT WHEREAS IN FIND IT WILL NOT!
 LETS SEE HOW 
 .find() 
 text="hello world"
 print(text.find("o")) = # 4
 print(text.find("world")) = #6
 print(text.find("x")) = #-1 ( why -1 because it cant throw an error , because theres no x found in the text = ("hello")
 .index()
 text= "hello world"
 print(text.index("o")) = #4
 print(text.index("x")) = ERROR ( it throws an error because this is how index functions if theres unfamiliar alphabet mentioned) 
SPLIT - ( IT SPLITS THE STRING ACCORDINGLY)
 text= "I love python"
 print(text.split()) = ['I', 'love', 'Python']
 JOIN
 words= [ "I", "love","Python"]
 results=" ".join(words)
 print(result) = I love Python
 NOW WE LL SEE NEW STRING
 a = "I love apple"
 a.endswith() = ( THIS IS USED TO KNOW WHETHER IT ENDS WITH THE PARTICULAR ALPHABET IF YES THEN "TRUE" IF NO THEN "FALSE"
 EXAMPLE 
 a.endswith('ple') = TRUE ( because the sentence is ended with apple )
 a.endswith('ole') = FALSE ( because the sentence dont end with ole)
 LETS SEE THIS
 a.startswith('I') = TRUE ( because it starts with )
a.startswith('A')= FALSE ( because it doesnt starts with the word "a")
REPLACE
sentence = "I love cats"
new_sentence= sentence.replace("cats","dogs") = I love dogs ( THIS WILL REPLACE THE WORDS )
CENTER
text= "Python"
print(text.center(12))= ###center### ( THE HASH IS THE SPACES GIVEN ALL THE SPACE AND THE LETTERS ARE TOTALLY 12 ) 
STRIP ( STRIP MEANS IT REMOVES SPACE (#) IN THE FRONT AND IN THE END )
a = "####abcd@gmail.com####"
a.strip('a') = abcd@gmail.com
a.isalphanum() = ( DETECTS WHETHER THERE IS ALPHABETS AND NUMERICAL VALUE)
a.isalpha() = ( DETECTS ONLY IF THERE IS ALPHABETS ) 
IT IS STRICTLY FALSE IF THERE IS ANY SPACE OR COMMAS 
FORMAT 
sentence= "My name is {}"
.format("sukhi")
print(sentence.format)= My name is sukhi ( fills the curly bracket with the name mentioned )
CONCATENATION ( COMBINATION OF 2 STRINGS IN ONE STRING)
first= "Hello"
second="Python"
result= first + " " + second ( " " are for space)
print(result) = Hello Python
CONCATENATING WITH NUMBERS 
age= 19
text= "I am" + str(age) + " years old "
print(text) = I am 19 years old


  
 
 
 
 
 
 






