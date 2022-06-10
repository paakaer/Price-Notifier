import json
import requests
import typer
import random
#import pandas as panda


from typing import List
from time import sleep
from loguru import logger
import datetime# import datetime

from collections import defaultdict

#logger.

app = typer.Typer()

'''
 = typer.Argument(help="The name of the product you want to find")
  = typer.Argument(help="Enter the websites in which you would like to search")
'''
@app.command("get")
def get():
    #productName: str
    productName = "oppo reno 6 pro" 
    if not productName:
        err = "ERROR, empty string as product name"
        typer.echo(err)
        logger.error(err)
    else:
        logger.info("enterd....")
        amazon(productName)

        ebay(productName)

        unieuro(productName)

        mediaWorld(productName)

        trony(productName)

        comet(productName)

        aliexpress(productName)

def amazon(keyword: str):
    amazonMarketPlaceList = ["com", "uk", "fr", "de", "it", "es"]
    keyword = "oppo reno 6 pro"
    for marketPlace in amazonMarketPlaceList:
        data = json.loads(amazonConnection(keyword, marketPlace).content)
        with open(f"{datetime.date.today()} {marketPlace}.json", "a") as file:
            amazonJSONParser(data, keyword)
            file.write(json.dumps(data))
        sleepTime = random.uniform(69, 96)
        logger.info(f"thread suspend time {sleepTime}")
        sleep(sleepTime)

def amazonConnection(kw: str, 
                     mp: str, 
                    ) -> requests.Response:
        url = "https://amazon24.p.rapidapi.com/api/product"
        query = {"keyword":kw,"country":mp.upper(),"page":"1"}
        headers = {
            "X-RapidAPI-Host": "amazon24.p.rapidapi.com",
            "X-RapidAPI-Key": "af75f00c9amsh6b0643d68c0508ep103142jsn7156563d2229"
        }
        print("making connection...")
        return requests.request("GET", url, headers=headers, params=query)
'''
def amazonJSONParserWithFilter(s: str, kw: str, *filters: List[str]) -> str:#filters containers strings that shouldn't be in product_title
    logger.info("parsing json...")
    for i in range(len(s["docs"])):
        for f in filters: #TODO i think you should remove filters; it's not used
            if f in s["docs"][i]["product_title"] or kw not in s["docs"][i]["product_title"]:
                logger.info("deleting {0}".format(s["docs"][i]))
                s["docs"][i].pop()
    logger.info("finished parsing json")
'''
def amazonJSONParser(s: str, kw: str) -> str:
    logger.info("parsing json...")
    print('\n')
    #s["docs"] = [i for i in s["docs"] if kw in i["product_title"]]
    for x, i in enumerate(s["docs"]):
        if kw not in i["product_title"]:
            logger.info("deleting \n\t{0}".format(i))
            del s["docs"][x]
    print('\n')
    logger.info("finished parsing json")

def ebay(keyword: str):
    pass

def unieuro(keyword: str):
    pass

def mediaWorld(keyword: str):
    pass

def trony(keyword: str):
    pass

def comet(keyword: str):
    pass

def aliexpress(keyword: str):
    pass

if __name__ == "__main__":
    app()    
