import pandas as pd


data = {'Name':['Jack', 'Maria', 'Alan', 'Casey'],
        'Salary':[2400, 3000, 2000, 1700],
        'Rent_Cost':[900, 850, 550, 650]
       }

df = pd.DataFrame(data)

df['Salary_%_Spent'] = round((df['Rent_Cost']/df['Salary']*100), 2)

print(df)
