#!/usr/bin/env python3
import os
import glob
import pandas as pd

user_path = "/Users/YOUR_USERNAME/Downloads/" #Path where the 'maildir' folder lives after extracting the original zip file. You need modify this to run locally.
isExist = os.path.exists(f"{user_path}/enron-sent-emails")
if not(isExist):
    os.makedirs(f"{user_path}/enron-sent-emails")
path = f"{user_path}/enron-sent-emails"
persons = os.listdir(f"{user_path}/maildir")
data = []
for person in persons:
    # isExist = os.path.exists(f"{path}/{person}")
    # if not(isExist):
    #     os.makedirs(f"{path}/{person}")
    person_path = f"{path}/{person}"
    for subdir in glob.glob(f"{user_path}/maildir/{person}/sent*"):
        # print(subdir)
        for file in os.listdir(subdir):
            myfile = open(f"{subdir}/{file}", encoding="ISO-8859-1")
            text = []
            append_next = False
            for line in myfile:
                if "X-FileName:" in line:
                    append_next = True
                    continue
                if "----------------------" in line:
                    break
                if "-----Original Message-----" in line:
                    break
                if append_next:
                    text.append(line)
            body = ' '.join(text)
            text = ' '.join(body.split())
            data.append([text, person])
            # print(text)
df = pd.DataFrame(data, columns = ['Text', 'Person'])
df.to_pickle(f"{path}/enron_dataframe.pkl", protocol=4)
print(df.head())
print(df.shape)
