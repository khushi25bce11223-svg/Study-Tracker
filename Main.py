def main():
  data = load_data()

  while True:
    print("\n1. Add Subject")
    print("2. Update Study Hours")
    print("3. View Report")
    print("4. Delete Subject")
    print("5. Exit")

    choice = input("Choose option: ")
    if choice == "1":
      add_subject(data)
    elif choice == "2":
      update_hours(data)
    elif choice == "3":
      view_report(data)
    elif choice == "4":
      delete_subject(data)
    elif choice== "5":
      save_data(data)
      print("Data saved. Exiting...")
      break
    else:
      print("Invalid choice!")
if __name__ == "__main__":
  main()
    
