# Add a new subject
def add_subject(data):
    subject = input("Enter subject name: ")
    if subject in data:
      print("Subject already exists!")
    else:
      data[subject] = 0
      print("Subject added.")
# Update study hours
def update_hours(data):
    subject = input("Enter subject name: ")
    if subject in data:
      try:
        hours = float(input("Enter hours to add: "))
        data[subjects] += hours
        print("Hours updated.")
      except:
        print("Invalid input ! Enter a number: ")
      else:
        print("Subject not found.")

# View study report
def view_report(data):
   if not data:
      print("No Subjects added yet.")
   else:
     print("\n--- Study Report ---")
     for subject, hours in data.items():
               print(f"{subject}: {hours} hours")
     print()
# Delete subject
def delete_subject(data):
    subject = input("Enter subject to delete: ")
    if subject in data:
       del data[subject]
       print("Subject deleted.")
    else:
       print("Subject not found.")
        
        
