# string concatenation

first_word = "Hello"
second_word = "World"

concat_words = first_word + " " + second_word

print(concat_words)

print((first_word + " ") * 3)

#indexing
print(first_word[0])
print(first_word[1])
print(first_word[2])

#slicing
print(first_word[1:4])

# lower upper

text = "python"
print(text.upper())


#strip

text = "     Python      "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


# replace

text = "Hello World"

print(text.replace("Hello","Bye"))


# join split

text = "apple,banana,grapes"

listOfFruits = text.split(",")
print(listOfFruits)

print(";".join(listOfFruits))

# find count

text = "Hello world world"
print(text.find("world"))

print(text.count("o"))


#f strings

name = "Shiva"
city = "chennai"

print(f"My name is {name} from {city}")


print("my height 5\t8")

# isupper

text = "ABCDEFGHIJK"

print(text.isupper())

print(text[1:7:2])

print(len(text))

print(text.count(""))
