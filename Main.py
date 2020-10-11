
import pandas as pd
Data_txt = open('Goodies.txt', 'r')
data = { 'Goodies': ['Fitbit Plus', 'IPods', 'MI Band', 'Cult Pass', 'Macbook Pro', 'Digital Camera', 'Alexa', 'Sandwich Toaster', 'Microwave Oven', 'Scale'], 'Price':
         [7980, 22349, 999, 2799, 229900, 11101, 9999, 2195, 9800, 4999]}
df = pd.DataFrame(data, columns =['Goodies', 'Price'])
print(df)

print(" ")
# Taking the user input
M = int(input('Number of employees: '))
print(" ")
# Generating Number of Goodies and there price for the number of employees
N = df.head(M)
#print(N)

# Converting dataframe to dictionary
d = N.to_dict()
#print(d)

print('Here are the goodies that are selected for distribution are: ')
# Printing the data under Goodies and Price columns
dff = pd.DataFrame(d, columns = ['Goodies', 'Price'])
print(dff)
# Generating the Maximum and Minimum values present in column 'Price'
Largest = dff['Price'][dff['Price'].idxmax()]
Smallest = dff['Price'][dff['Price'].idxmin()]

# Printing the Largest and Smallest Values
print('')
print('The Largest value is: ',Largest)
print("")
print('The Lowest value is',Smallest)
print("")
Difference = Largest - Smallest
print('And the difference between the chosen goodie with highest price and the lowest price is: ',Difference)


Data_txt.close()
#print(L)

#s = df['Price'].idxmin()


