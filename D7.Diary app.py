from datetime import datetime
import random as r
class diary:
    def __init__(self,title = "my diary"):
        self.title = title
        self.entries =[]
    def add_diary(self , text, mood =None):
        # this can convert date into proper format
        date = datetime.now().strftime("%d-%m-%Y")
        entry_id = r.randint(1000, 9999)
        entry = {
            "id": entry_id,
            "date":date,
            "text":text,
            "mood": mood
        }
        self.entries.append(entry)
        print("entry saved")
    def show_entries(self):
        print("diary entries")
        for entry in self.entries:
            # print values from dictionary
            print("ID:", entry["id"])
            print("Date:", entry["date"])
            print("Text:", entry["text"])
            print("Mood:", entry["mood"])
            print("-" * 20)
d1 = diary()
d1.add_diary("today i learned python","happy")   
d1.add_diary("completed my question")    
d1.show_entries()    
            
        