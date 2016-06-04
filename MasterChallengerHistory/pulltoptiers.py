#! python3.

import requests
import apiconfig
from summoner import Summoner


def pullEntireTier(url):
    res = requests.get(url)
    res = res.json()
    tier = res['tier']
    league_name = res['name']
    summoners = res['entries']
    sums = []
    for summoner in summoners:
        s = Summoner(summoner)
        s.tier = tier
        s.league_name = league_name
        sums.append(s)
        s.printAll()


tier_url = "https://na.api.pvp.net/api/lol/na/v2.5/league/master?type=RANKED_SOLO_5x5&api_key=" + apiconfig.APIKEY

pullEntireTier(tier_url)

tier_url = "https://na.api.pvp.net/api/lol/na/v2.5/league/challenger?type=RANKED_SOLO_5x5&api_key=" + apiconfig.APIKEY

pullEntireTier(tier_url)

print('Done.')
