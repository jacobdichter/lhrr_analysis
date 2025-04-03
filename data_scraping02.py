################################################################################
# I will attempt to extract the HTML content from past online LHRR race results
# and parse them using beautifulsoup, structure the data, and output to .csv
################################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://web.archive.org/web/20030306094211/http://www.coolrunning.com/bin/res_load/res_print.cgi?r=02/ct/Jun9_Litchf_set1.shtml'

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
print(text)

# Split text on all new line \n characters
lines = text.split("\n")

###########################################################
# FROM HERE ONWARD - Requires case-specific string parsing
###########################################################

# # Strip all white space from each line
# # cleaned_lines = [line.strip() for line in lines if line.strip()]

# # Specify the string containing the COLUMN HEADER INDEX
start_index = lines.index("PLAC FIRST NAME  LAST  S AG TIME    PACE  DIV/TOT  DIV   NO.  CITY       ST")

# # print(repr(lines[start_index:][2]))

# Print each line with dots filling the white spaces to count exact spacing
dotted_lines = [line.replace(" ", ".") for line in lines[start_index:]]
for line in dotted_lines:
    print(line, '\n')

# Loop through each result line and capture variable data / Assign into results as list of str
results = []
for line in lines[start_index:]:
    # if len(parts) < 13:
    #     break
    place = line[0:4]
    name = line[5:23]
    sex = line[23:24]
    age = line[25:27]
    time = line[28:35]
    pace = line[36:41]
    div_rank = line[42:50]
    div = line[51:56]
    num = line[57:61]
    cty = line[62:72]
    state = line[72:]


    results.append([place, name, num, sex, age, time, pace, div_rank, div, cty, state])

print(results)

# After parsing on fixth widths and capturing variables, remove white spaces from the values
cleaned_results = []
for i in results:
    cleaned_i = []
    for each in i:
        cleaned = each.strip()
        cleaned_i.append(cleaned)
    cleaned_results.append(cleaned_i)

print('\nCLEANED RESULTS:\n\n', cleaned_results[15:50])

# Export cleaned data to .csv
df = pd.DataFrame(cleaned_results, columns=["place", "name", "num", "sex", "age", "time", "pace", "div_rank", "div", "cty", "state"])
print(df.loc[50:150])
df['race_date'] = '2002-06-09'
df['race_year'] = '2002'
print(df.loc[50:150])
df.to_csv('lhrr_2002_results.csv', index=False)