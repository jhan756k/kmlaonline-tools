import requests
import json
import datetime

def get_food():
  food = dict()
  now = datetime.datetime.now()

  URI = "https://open.neis.go.kr/hub/mealServiceDietInfo"

  with open("./급식 정보/config.json") as f:
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
    "MLSV_FROM_YMD": MLSV_FROM_YMD,
    "MLSV_TO_YMD": MLSV_TO_YMD
  }

  response = requests.get(URI, params=params)
  json_data = json.loads(response.text)
  not_done = True

  while not_done:
    try:
      for item in json_data["mealServiceDietInfo"][1]["row"]:
        mealinfo = item["MLSV_YMD"]
        m = int(mealinfo[4:6])
        d = int(mealinfo[6:])
        mealtype = item["MMEAL_SC_CODE"]
        meal = item["DDISH_NM"]
        
        meal = ''.join(e for e in meal if e.isalpha())

        if mealtype == "1":
          mealtype = "breakfast"
        elif mealtype == "2":
          mealtype = "lunch"
        elif mealtype == "3":
          mealtype = "dinner"
        print(mealtype)
        if m not in food:
          food[m] = dict()
        if d not in food[m]:
          food[m][d] = dict()
        if mealtype not in food[m][d]:
          food[m][d][mealtype] = meal.split("br")
          
        elif mealtype in food[m][d]:
          not_done = False
          break

    except KeyError:
      pass

  # add dinner if not exist
  for month in food:
    for day in food[month]:
      print(month, day)
      try:
        print(food[month][day]["dinner"])
      except KeyError:
        food[month][day]["dinner"] = ["급식이 없습니다."]
        continue

  # json_obj = json.dumps(food, ensure_ascii=False, indent=4, separators=(',', ': '))
  with open("./급식 정보/data.json", "w", encoding='UTF-8') as outfile:
    json.dump(food, outfile, ensure_ascii=False, indent=4, separators=(',', ': '))

get_food()