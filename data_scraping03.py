################################################################################
# I will attempt to extract the HTML content from past online LHRR race results
# and parse them using beautifulsoup, structure the data, and output to .csv
################################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.plattsys.com/results/res2003/lhills03.htm'

# Send HTTP requests for website
response = requests.get(url)

# Print HTTP requests status code [200 = Success]
print(response.status_code)

# print(response.content)

# Create bs4.BeautifulSoup object / convert response to text / pass 'html.parser' argument
soup = BeautifulSoup(response.text, "html.parser")

# Call .get_text() on BeautifulSoup object and assign into text
text = soup.get_text()

# Print soup text | Quite nice formatting here
# print(text)

# Split text on all new line \n characters
lines = text.split("\n")

###########################################################
# FROM HERE ONWARD - Requires case-specific string parsing
###########################################################

# # Strip all white space from each line
# # cleaned_lines = [line.strip() for line in lines if line.strip()]

# # Specify the string containing the COLUMN HEADER INDEX
# start_index = lines.index("PLACE   LAST          FIRST        CITY          SEX  DIV    PLC/TOT   TIME     PACE  BIB")

# # print(repr(lines[start_index:][2]))


# Print each line with dots filling the white spaces to count exact spacing
# dotted_lines = [line.replace(" ", ".") for line in lines]
# for line in dotted_lines:
#     print(line)

# Loop through each result line and capture variable data / Assign into results as list of str
results = []
for line in lines:
    # if len(parts) < 13:
    #     break
    place = line[0:4]
    lname = line[5:19]
    fname = line[20:31]
    cty = line[32:47]
    state = line[48:50]
    age = line[51:53]
    div = line[54:59]
    div_rank = line[60:67]
    time = line[68:78]
    pace = line[79:86]
    num = line[87:]

    results.append([place, lname, fname, num, age, time, pace, div_rank, div, cty, state])

# print(results)

# After parsing on fixth widths and capturing variables, remove white spaces from the values
cleaned_results = []
for i in results:
    cleaned_i = []
    for each in i:
        cleaned = each.strip()
        cleaned_i.append(cleaned)
    cleaned_results.append(cleaned_i)

print('\nCLEANED RESULTS:\n\n', cleaned_results[51:150])

# Export cleaned data to .csv
df = pd.DataFrame(cleaned_results, columns=["place", "lname", "fname", "num", "age", "time", "pace", "div_rank", "div", "cty", "state"])
print(df.loc[50:150])
df['race_date'] = '2003-06-08'
df['race_year'] = '2003'
df['sex'] = df['div'].astype(str).str[0]
# df['sex'] = df['div'].str.strip().str[0]


print(df.loc[50:150])
df.to_csv('lhrr_2003_results.csv', index=False)