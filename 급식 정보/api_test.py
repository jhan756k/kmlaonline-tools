import requests
import json
import datetime

def get_food():
  food = dict()
  now = datetime.datetime.now()

  URI = "https://open.neis.go.kr/hub/mealServiceDietInfo"

  with open("config.json") as f:
    config = json.load(f)
    KEY = config["FOOD_KEY"]

  TYPE = "json"
  
  ATPT_OFCDC_SC_CODE = "K10"
  SD_SCHUL_CODE = "7801132"
  MLSV_FROM_YMD = str(now.year) + "0101"
  MLSV_TO_YMD = str(now.year) + "0328"

  params = {
    "KEY": KEY,
    "Type": TYPE,
    "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
    "SD_SCHUL_CODE": SD_SCHUL_CODE,
    "MMEAL_SC_CODE": "3",
    "MLSV_FROM_YMD": MLSV_FROM_YMD,
    "MLSV_TO_YMD": MLSV_TO_YMD
  }

  response = requests.get(URI, params=params)
  json_data = json.dumps(response.json(), ensure_ascii=False, indent=4, separators=(',', ': '))
  print(json_data)

  # count dinner
  count = 0
  for item in json_data["mealServiceDietInfo"][1]["row"]:
    if item["MMEAL_SC_CODE"] == "3":
      count += 1
  print(count)
get_food()