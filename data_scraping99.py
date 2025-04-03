################################################################################
# I will attempt to extract the HTML content from past online LHRR race results
# and parse them using beautifulsoup, structure the data, and output to .csv
################################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://web.archive.org/web/20040331224312/http://www.coolrunning.com/bin/res_load/res_print.cgi?r=99/ct/Jun13_Litchf_set1.shtml'

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
# start_index = lines.index("PLACE NAME                NO.  S AG DIV   DIV CITY       ST time    PACE")

# # print(repr(lines[start_index:][2]))

results = []
for line in lines:
    # if len(parts) < 13:
    #     break
    place = line[0:4]
    name = line[5:23]
    sex = line[23:24]
    age = line[25:27]
    div_rank = line[28:36]
    div = line[37:42]
    num = line[43:47]
    cty = line[48:59]
    state = line[59:61]
    time = line[62:69]
    pace = line[70:]

    results.append([place, name, num, sex, age, div, div_rank, cty, state, time, pace])

print(results)

cleaned_results = []
for i in results:
    cleaned_i = []
    for each in i:
        cleaned = each.strip()
        cleaned_i.append(cleaned)
    cleaned_results.append(cleaned_i)

print(cleaned_results[15:50])

# Export cleaned data to .csv
df = pd.DataFrame(cleaned_results, columns=["place", "name", "num", "sex", "age", "div", "div_rank", "cty", "state", "time", "pace"])
print(df.loc[50:150])
df['race_date'] = '1999-06-13'
df['race_year'] = '1999'
print(df.loc[50:150])
# df.to_csv('lhrr_1999_results_virgin.csv', index=False)