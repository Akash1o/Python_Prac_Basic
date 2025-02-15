import pandas as pd

#creating a dataframe
user ={
    'Name':["Akash","Sabin" , "Alisha"],
    'Age' :[25,30,34],
    'Location' :["Ktm","Pkr","BKT"]
}

df=pd.DataFrame(user)

print(df)

#changing the name of column
df=df.rename(columns={"Name":'YourName'})

print(df)

#another way of making it

data=[
    ['Akash',100,'China'],
      ['Sabin',44,'India'],
      ['Johnathan',22, 'USA']
]

column =['Name','Emp_ID', 'Location']

df= pd.DataFrame(data,columns=column)

print(df)

#anothe way of crating list of dictionaries.
datas = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

df = pd.DataFrame(datas)
print(df)
