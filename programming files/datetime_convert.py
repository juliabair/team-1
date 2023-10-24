from datetime import datetime

# Set Date and Time in string
date_str = "2022-03-17 10:45:30"
# Read date_str into a datetime object
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
# Read the date object out into a formatted string M/D/Y H:M:S
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# Print the formatted date string
print(formatted_date)
