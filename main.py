import os
from random import randint

import pandas as pd

# Getting terminal size and adding divider for any screen.
sp = "-" * os.get_terminal_size().columns

# CSV file to Data Frame.
df = pd.read_csv("merged.csv")

# Printing divider and Data Frame.
print("\nBefore Data Cleaning", sp)
print(df.head())
print(sp, "\n")

# Removing NaN values.
df = df.dropna()

# Removing duplicate columns.
df = df.drop_duplicates()

# Removing Unused Columns.
del df["Luminosity"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

# Renaming some columns.
df.rename(
    columns={
        "distance_ly": "distance",
    }
)

# Storing File name for re-cleaning file
fileNameGlobal = []

# Checking merged-cleaned.csv is exist or not.
if (
    os.path.isfile("merged-cleaned.csv") == True
):  # if merged-cleaned.csv is exist than create merged-cleaned1.csv or merged-cleaned2.csv / 3....10 random number.
    f = str(os.getcwd() + "\merged-cleaned-" + str(randint(1, 10)) + ".csv")
    fileNameGlobal.append(f)

    df.to_csv(f, index=False)
    print("Data is cleared ->", f, "\n")

elif (
    os.path.isfile("merged-cleaned.csv") == False
):  # else if merged-cleaned.csv is not exist than create merged-cleaned.csv file.
    fileNameGlobal.append("merged-cleaned.csv")

    df.to_csv("merged-cleaned.csv", index=False)
    print("Data is cleared ->", os.getcwd() + "\merged-cleaned.csv", "\n")
else:
    pass

# Reading merged-cleaned.csv file for re-cleaning.
df = pd.read_csv(fileNameGlobal[0])

# Removing NaN values.
df = df.dropna()

# Removing duplicate columns.
df = df.drop_duplicates()

# Removing Unused Columns.
del df["Unnamed: 0"]
del df["Unnamed: 6"]


# Printing divider and result Data Frame.
print(sp, "\n")
print(df.head())
print(
    "After Data Cleaning",
    sp,
)

# After re-cleaning , saving file as same file name.
df.to_csv(fileNameGlobal[0])
