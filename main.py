import os
print("Keyword Command Line Finder for WINDOWS")

# Takes Keyword Input
keyword = input("Keyword: ")

# Takes Directory Input
# Takes Specific Directory (Layer 1 Search)
print("Current Location: " + os.getcwd())
directory = input("Directory: ")

# Navigate to Directory
try:
  os.chdir(directory)
except:
  print(f"{directory} was not found. Please put in the specific path.")
  quit()

# Display All Files
print(f"\nTotal Files: {len(os.listdir())}")
for i in range(len(os.listdir())):
  print(f"{i+1}. {os.listdir()[i]}")

print("Searching...\n")

# Search For Files
links = []
for x in range(len(os.listdir())):
  if keyword in (os.listdir()[x]):
    links.append(os.listdir()[x])
  else:
    # Failsafe for Future Code Cleanability
    try:
      break
    except:
      bool = True

# Display Results
print("Search Results: ")
for a in range(len(links)):
  print(links[a])

print("\nSearch Completed.")
  
