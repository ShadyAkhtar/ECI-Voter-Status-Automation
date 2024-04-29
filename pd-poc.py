import pandas as pd

df = pd.read_csv("voter-list.csv")

# Create an empty list to store the status values
status_list = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    application_no = row["APPLICATION NO"]
    # # Example condition: If the application number ends with 'CONFIRMED', set status as 'CONFIRMED', otherwise 'PENDING'
    # if application_no.endswith('CONFIRMED'):
    #     status = 'CONFIRMED'
    # else:
    #     status = 'PENDING'
    # Append the status to the status list
    # print(application_no)print  type of application_no
    print(type(application_no), application_no, type(application_no) == str)
    status = "FVR SUBMITTED"
    status_list.append(status)

# Add the status list as a new column to the DataFrame
df["STATUS"] = status_list

# Save the DataFrame back to CSV
df.to_csv("voter-list-with-status.csv", index=False)

# import pandas as pd
# from openpyxl import load_workbook

# # Read the Excel file
# df = pd.read_excel("voter-list.xlsx", engine="openpyxl")

# # Create an empty list to store the status values
# status_list = []

# # Iterate over each row in the DataFrame
# for index, row in df.iterrows():
#     application_no = row["APPLICATION NO"]
#     # Example condition: If the application number ends with 'CONFIRMED', set status as 'CONFIRMED', otherwise 'PENDING'
#     # if application_no.endswith('CONFIRMED'):
#     #     status = 'CONFIRMED'
#     # else:
#     status = "PENDING"
#     # Append the status to the status list
#     status_list.append(status)

# # Add the status list as a new column to the DataFrame
# df["STATUS"] = status_list

# # Load the existing Excel file
# book = load_workbook("voter-list.xlsx")

# # Open the existing sheet
# writer = pd.ExcelWriter("voter-list.xlsx", engine="openpyxl")
# writer.book = book
# writer.sheets = {ws.title: ws for ws in book.worksheets}

# # Overwrite the existing sheet with the updated DataFrame
# df.to_excel(writer, index=False, sheet_name="Sheet1")

# # Save the changes
# writer.save()
