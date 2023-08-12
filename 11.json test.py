

import requests
import json
import webbrowser
import pprint
""" 
https://api.stackexchange.com/docs/questions
 
"site": "stackoverflow",
    "sort": "votes",
    "order": "desc",
    "fromdate": "2023-08-12",
    "tagged": "python",
    "min": "15"
    
    
activity – last_activity_date
creation – creation_date
votes – score
hot – by the formula ordering the hot tab
Does not accept min or max
week – by the formula ordering the week tab
Does not accept min or max
month – by the formula ordering the month tab
Does not accept min or max
activity is the default sort.

It is possible to create moderately complex queries using sort, min, max, fromdate, and todate.


"""

params = {
    "site": "stackoverflow",
    "sort": "hot",
    "order": "desc",
    "fromdate": "2023-08-12",
    "tagged": "python",
    # "min": "5"
}

r = requests.get("https://api.stackexchange.com/2.3/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("zły format")
else:
    # pprint.pprint(questions)
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
