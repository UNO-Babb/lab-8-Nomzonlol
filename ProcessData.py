#ProcessData.py
#Name:Nomaan Ahmed 
#Date:4/5/2025
#Assignment:Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    parts = line.strip().split()
    if len(parts) < 6:  # Skip lines with insufficient data
      continue
    
    # Find the email (contains @ symbol)
    email_index = -1
    for i, part in enumerate(parts):
      if '@' in part:
        email_index = i
        break
    
    if email_index == -1:  # No email found, skip line
      continue
    
    # Extract first name and last name
    first_name = parts[0]
    last_name = ' '.join(parts[1:email_index])
    
    # Extract student ID (should follow email)
    student_id = parts[email_index + 1] if email_index + 1 < len(parts) else ""
    
    # Extract year (freshman, sophomore, junior, senior)
    year_keywords = ["Freshman", "Sophomore", "Junior", "Senior"]
    year = ""
    for part in parts[email_index + 2:]:  # Look for year after student ID
      if part in year_keywords:
        year = part
        break
    
    if not year:  # No valid year found, skip line
      continue
    
    # Extract major (everything after year until end of line)
    year_index = parts.index(year)
    major = ' '.join(parts[year_index + 1:])
    
    # Create UserID: first initial + last name (lowercase) + last 3 digits of student ID
    first_initial = first_name[0].lower()
    last_name_lower = last_name.lower()
    
    # Add 'x' if last name is less than 5 characters
    if len(last_name_lower) < 5:
      last_name_lower += 'x'
    
    last_three_digits = student_id[-3:]
    user_id = f"{first_initial}{last_name_lower}{last_three_digits}"
    
    # Create Major-Year field
    # Get first 3 letters of major
    major_code = ''.join(filter(str.isalpha, major))[:3].upper()
    
    # Convert year to abbreviation
    year_abbr = {
      "Freshman": "FR",
      "Sophomore": "SO",
      "Junior": "JR",
      "Senior": "SR"
    }.get(year, "FR")
    
    # Combine with hyphen
    major_year = f"{major_code}-{year_abbr}"
    
    # Write to CSV: LastName,FirstName,UserID,MajorYear
    csv_line = f"{last_name},{first_name},{user_id},{major_year}\n"
    outFile.write(csv_line)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
