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