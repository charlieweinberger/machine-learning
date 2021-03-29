from parse_line import parse_line
import math
import sys
sys.path.append('src')
from dataframe import DataFrame

data_types = {
    "PassengerId": int,
    "Survived": int,
    "Pclass": int,
    "Name": str,
    "Sex": str,
    "Age": float,
    "SibSp": int,
    "Parch": int,
    "Ticket": str,
    "Fare": float,
    "Cabin": str,
    "Embarked": str
}

df = DataFrame.from_csv("kaggle/data/dataset_of_knowns.csv", data_types=data_types, parser=parse_line)
assert df.columns == ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

ans1 = [
  [1, 0, 3, '"Braund, Mr. Owen Harris"', "male", 22.0, 1, 0, "A/5 21171", 7.25, None, "S"],
  [2, 1, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', "female", 38.0, 1, 0, "PC 17599", 71.2833, "C85", "C"],
  [3, 1, 3, '"Heikkinen, Miss. Laina"', "female", 26.0, 0, 0, "STON/O2. 3101282", 7.925, None, "S"],
  [4, 1, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', "female", 35.0, 1, 0, "113803", 53.1, "C123", "S"],
  [5, 0, 3, '"Allen, Mr. William Henry"', "male", 35.0, 0, 0, "373450", 8.05, None, "S"]
]

assert df.to_array()[:5] == ans1

# Name -> Surname

def name_to_surname(name): return name.split(',')[0][1:]

df.data_dict['Surname'] = df.data_dict['Name']
df = df.apply('Surname', lambda x: name_to_surname(x))
del df.data_dict['Name']

new_columns = ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

df.columns = new_columns
df.data_dict = {key : df.data_dict[key] for key in df.columns}

# Cabin -> CabinType, CabinNumber

def cabin_to_cabin_type(cabin): return None if cabin == None else cabin[0]

def cabin_to_cabin_number(cabin):
    
    if cabin == None or len(cabin) == 1:
        return None
    
    elif cabin[1] == ' ':
        return int(cabin.split(' ')[1][1:])

    else:      
        return int(cabin.split(' ')[0][1:])

df.data_dict['CabinType'] = df.data_dict['Cabin']
df.data_dict['CabinNumber'] = df.data_dict['Cabin']
df = df.apply('CabinType', lambda x: cabin_to_cabin_type(x))
df = df.apply('CabinNumber', lambda x: cabin_to_cabin_number(x))
del df.data_dict['Cabin']

new_columns = ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "CabinType", "CabinNumber", "Embarked"]

df.columns = new_columns
df.data_dict = {key : df.data_dict[key] for key in df.columns}

# Ticket -> TicketType, TicketNumber

def ticket_to_ticket_type(ticket):
    if ticket == None or ticket.split(' ')[0][0] in [str(i) for i in range(10)]:
        return None
    else:
        return ticket.split(' ')[0]

def ticket_to_ticket_number(ticket):
    if ticket == None or ticket.split(' ')[-1] == 'LINE':
        return None
    else:
        return int(ticket.split(' ')[-1])

df.data_dict['TicketType'] = df.data_dict['Ticket']
df.data_dict['TicketNumber'] = df.data_dict['Ticket']
df = df.apply('TicketType', lambda x: ticket_to_ticket_type(x))
df = df.apply('TicketNumber', lambda x: ticket_to_ticket_number(x))
del df.data_dict['Ticket']

new_columns = ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"]

df.columns = new_columns
df.data_dict = {key : df.data_dict[key] for key in df.columns}

# tests

assert df.columns == ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"]

ans2 = [
  [1, 0, 3, "Braund", "male", 22.0, 1, 0, "A/5", 21171, 7.25, None, None, "S"],
  [2, 1, 1, "Cumings", "female", 38.0, 1, 0, "PC", 17599, 71.2833, "C", 85, "C"],
  [3, 1, 3, "Heikkinen", "female", 26.0, 0, 0, "STON/O2.", 3101282, 7.925, None, None, "S"],
  [4, 1, 1, "Futrelle", "female", 35.0, 1, 0, None, 113803, 53.1, "C", 123, "S"],
  [5, 0, 3, "Allen", "male", 35.0, 0, 0, None, 373450, 8.05, None, None, "S"]
]

assert df.to_array()[:5] == ans2

# Assignment 73 - processing and interpreting Ages data and Fare data

ages = []
max_age = max(df.where(lambda row: row['Age'] != None).data_dict['Age'])
for i in [10*i for i in range(math.ceil(max_age) // 10)]:
    this_age_range = df.where(lambda row: row['Age'] != None).where(lambda row: i < row['Age'] <= (i + 10))
    ages.append(this_age_range)

for age_range in ages:
    age_range_survived = [elem[0] for elem in age_range.select(["Survived"]).to_array()]
    survival_rate = sum(age_range_survived) / len(age_range_survived)
    
    # print('\nsurvival_rate:', round(survival_rate, 2))
    # print('count:', len(age_range_survived))

# python kaggle/titanic/data_loading.py

fares = []
fare_ranges_mins = [0, 5, 10, 20, 50, 100, 200, 99999999999999999999999999999999999999999]
for i in range(len(fare_ranges_mins)):
    this_fare_range = df.where(lambda row: row['Fare'] != None).where(lambda row: fare_ranges_mins[i] < row['Fare'] <= fare_ranges_mins[i + 1])
    fares.append(this_fare_range)

for fare_range in fares:
    fare_range_survived = [elem[0] for elem in fare_range.select(["Survived"]).to_array()]
    avg = sum(fare_range_survived) / len(fare_range_survived)
    
    # print('\naverage:', round(avg, 2))
    # print('count:', len(fare_range_survived))