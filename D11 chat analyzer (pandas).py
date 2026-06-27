import pandas as pd
names =[]
messages =[]
# open file
with open("chat.txt","r") as file:
    lines = file.readlines()
    # loop for each line
    for line in lines:
        # remove extra spaces
        line = line.strip()
        if line =="":
            continue
        name,message = line.split(":",1)
        name = name.strip()
        message = message.strip()
        # store data in list
        names.append(name)
        messages.append(message)
        # now create dictionary
data = {
    "Name": names,
    "Message": messages
}
df = pd.DataFrame(data)
print("----------------chat data--------------")
print(df)
print("total messages:",len(df))
print("\n----- Messages Count -----")
print(df["Name"].value_counts())
print("\nMost Active Person:")
print(df["Name"].value_counts().idxmax())
all_words =[]
for message in df["Message"]:
    words = message.split()
    all_words.extend(words)
word_series = pd.Series(all_words)

# Display most common words
print("\n----- Common Words -----")
print(word_series.value_counts())  
    