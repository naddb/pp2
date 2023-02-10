a = 'hello'
print(a)
a = "hello"
print(a)

a = '''dfghjkl
sghjkl
gyhjk;'''
print(a)

a = 'Hii, world.'
print(a[7])
print(len(a))

for x in 'banana':
    print(x)

a = 'the best things in life are free!'
print('es' in a)

a = 'the best things in life are free!'
if 'best' in a:
    print('Yes, "best" the present')

a = 'the best things in life are free!'
print('tree' not in a)

a = 'the best things in life are free!'
if 'tree' not in a:
    print('No, "tree" is not present')


s = 'hello, world'
print(s[2:5])  #(]

s = 'hello, world'
print(s[:4])

s = 'hello, world'
print(s[2:])

s = 'hello, world'
print(s[-5:-2])  #[)


a = 'Hello worlD'
print(a.upper())

b = 'HeLlO wOrLd'
print(b.lower())

c = '     hello brooo     '
print(c.strip())

d = 'Dianf'
print(d.replace('f', 'a'))

e = 'diana, f, rrrr'
print(e.split(',')) 


a = 'hiiiiii'
b = 'brooooo'
c = a + b
print(c)

a = 'hiiiiii'
b = 'brooooo'
c = a + ' ' + b
print(c)


'''
age = 19
txt = 'hii my name is Diana and I am' + age
print(txt)'''
age = 19
txt = 'hii my name is Diana and I am' 
print(txt, age)

age = 19 
txt = 'hii my name is Diana and I am {}'
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#txt = "We are the so-called "Vikings" from the north."
txt = 'We are the so-called "Vikings" from the north.'
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#\'	Single Quote
txt = 'It\'s alright.'
print(txt) 

#\\	Backslash	
txt = "This will insert one \\ (backslash)."
print(txt) 

#\n	New Line
txt = "Hello\nWorld!"
print(txt) 

#\r	Carriage Return
txt = "Hello\rWorld!"
print(txt) 

#\t	Tab	
txt = "Hello\tWorld!"
print(txt) 

#\b	Backspace
txt = "Hello \bWorld!"
print(txt) 

#\f	Form Feed	

#\ooo	Octal value	
txt = "\110\145\154\154\157"
print(txt) 

#\xhh	Hex value	
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
