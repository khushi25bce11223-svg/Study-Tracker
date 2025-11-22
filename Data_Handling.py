import json
import os

Data_File = "study_data.json"

# Load saved data
def load_data():
  if os.path.exists(Data_File):
     with open(Data_File, "r") as f:
        return json.load(f)
  return {}
# Save data
def save_data(data):
   with open(Data_File, "w") as f:
     json.dump(data, f , indent=4)


                        
      
