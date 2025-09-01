a = "SUKHI"
print(a.lower())
b = "I love python"
print(b.upper())
a = "we are learning python"
a.split("e")
a = "helllllo world"
a.split("l")
c = "helllllooo worllld"
c.split("l")
print(c.split())
d = "python"
d.find("y")
print(d.find("y"))
e = "fruits are amazing"
e.endswith('ing')
print(e.endswith('ing'))
f = "icecream is sweet"
f.startswith('iced')
print(f.startswith('iced'))
j = "     abcd@gmail.com         "
j.strip('')
print(j.strip(''))
h = "sukhi123"
h.isalnum()
print(h.isalnum())
i = "1234"
i.isalpha()
print(i.isalpha())
z = ("I love python")
print(z.replace("python","excel"))
name = "Sukhi"
age = "19"
sentence = "My name is {} and I am {} years old." .format(name, age)
print(sentence)
name = "Sukhi"
age = 19
sentence = "My name is " + name + " and I am " + str(age) + " years old."
print(sentence)
product = "iPhone"
price = 89999
sentence = "The price of {} is ${}.".format(product, price)
print(sentence)