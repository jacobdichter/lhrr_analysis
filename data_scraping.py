################################################################################
# I will attempt to extract the HTML content from past online LHRR race results
# and parse them using beautifulsoup, structure the data, and output to .csv
################################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://web.archive.org/web/20030622213128/http://www.coolrunning.com/bin/res_load/res_print.cgi?r=98/ct/litc0614.htm'

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

# Strip all white space from each line
# cleaned_lines = [line.strip() for line in lines if line.strip()]

# Specify the string containing the COLUMN HEADER INDEX
start_index = lines.index("PLACE NAME                NO.  S AG DIV   DIV CITY       ST time    PACE")

# print(repr(lines[start_index:][2]))

results = []
for line in lines[start_index:]:
    # if len(parts) < 13:
    #     break
    place = line[0:5]
    name = line[6:26]
    num = line[26:30]
    sex = line[31:32]
    age = line[33:35]
    div = line[36:41]
    div_rank = line[42:45]
    cty = line[46:56]
    state = line[57:59]
    time = line[60:67]
    pace = line[68:]

    results.append([place, name, num, sex, age, div, div_rank, cty, state, time, pace])

print(results)

# print(lines[start_index:][0].replace(" ", "."))
# for i in results[3]:
#     print(i.replace(" ","."))
# # print(results[3])


# Fixth width of columns 0:10
data_lens = [5, 19, 4, 1, 2, 5, 3, 10, 2, 7, 5]
# for i in data_lens:
#     i += 1

# start_idx = 0
# end_idx = 0
# for i in data_lens:
#     end_idx += i
#     print(f'variable = line[', start_idx, ':', end_idx, ']', sep="")
#     start_idx += i



# df = pd.DataFrame(results, columns=["place", "fname", "lname", "num", "sex", "age", "div", "age2", "div_rank", "cty", "state", "time", "pace"])
# print(df)
# # df.to_csv('lhrr_1998_results.csv', index=False)