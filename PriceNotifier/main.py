from time import sleep
from typing import List
import requests
import typer
import random
import logging as logger

logger.basicConfig(format="%(asctime)s %(process)d-%(thread)d %(levelname)s=>%(message)s")

app = typer.Typer()


@app.command()
def get(productName: str, sites: List[str]):
    if not productName:
        err = "ERROR, empty string as product name"
        typer.echo(err)
        logger.error(err)
    else:#TODO create an enum
        for s in sites:
            if(s.lower() == "amazon"):
                amazon(s)
            elif(s.lower() == "ebay"):
                ebay(s)
            elif(s.lower() == "unieuro"):
                unieuro(s)
            elif(s.lower() == "mediaworld"):
                mediaWorld(s)
            elif(s.lower() == "trony"):
                trony(s)
            elif(s.lower() == "comet"):
                comet(s)

def amazon(keyword: str):
    amazonMarketPlaceList = ["com", "uk", "fr", "de", "it", "es"]
    searchURL = "https://amazon-price1.p.rapidapi.com/search"
    priceURL = "https://amazon-price1.p.rapidapi.com/priceReport"
    
    for marketPlace in amazonMarketPlaceList:
        logger.info(amazonConnection(keyword, marketPlace).text)
        sleepTime = random.uniform(69, 96)
        sleep(sleepTime)
        logger.info(f"thread suspend time {sleepTime}")

def amazonConnection(kw: str, 
                     mp: str, 
                     sURL: str, 
                     pURL: str, 
                     sQuery: dict[str, str], 
                     pQuery: dict[str, str]
                    ) -> List[requests.Response]:
    url = "https://amazon-price1.p.rapidapi.com/search"
    querystring = {"keywords":kw,"marketplace":mp}
    headers = {
        "X-RapidAPI-Host": "amazon-price1.p.rapidapi.com",
        "X-RapidAPI-Key": "af75f00c9amsh6b0643d68c0508ep103142jsn7156563d2229"
    }
    return requests.request("GET", 
                            sURL, 
                            headers=headers, 
                            params=querystring), requests.request("GET", 
                                                                  pURL, 
                                                                  headers=headers, 
                                                                  params=querystring)

    '''
        ###price reporting
        import requests

            url = "https://amazon-price1.p.rapidapi.com/priceReport"

            querystring = {"asin":"<REQUIRED>","marketplace":"ES"}

            headers = {
                "X-RapidAPI-Host": "amazon-price1.p.rapidapi.com",
                "X-RapidAPI-Key": "af75f00c9amsh6b0643d68c0508ep103142jsn7156563d2229"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
    '''

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

if __name__ == "__main__":
    app()    
