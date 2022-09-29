import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

#ask the user for the code of the country and save it into a variable
name = input('enter country code: ')
print(name)

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
l = list(db.ws(ws='Sheet1').col(col=3)[1:])

c = l.count(name)

#Format and print the result
print(c)

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
while 1:
    done = False
    while done == False:
        try:
            population = int(input('enter population here: '))
            if population >= 400000:
                print(population, 'that is alot of people!')
                break
            else:
                print(population, 'Not as many people!')
                break
        except:
            print('Input cannot be converted to a INTEGER!, please try again!')

    break

#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5)[1:])

#Initialize a list lstOfRecords to an empty list
recordslist = []

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords


for el in l1:
    if el > population:
        recordslist.append(el)


#Print the list l1
print(recordslist)

#Bonus: Print the name of the cities whose index is in l1
l2 = list(db.ws(ws='Sheet1').col(col=2)[1:])
Popcitydict ={
    "populationlist": l1,
    "city": l2
}

for el, el2 in Popcitydict.items():
    print (el, "->", el2)



