#!/usr/bin/python

class Summoner:
    'Common base class for all summoners(players)'

    def __init__(self, jsonSummoner):
        self.name = jsonSummoner['playerOrTeamName']
        self.lp = jsonSummoner['leaguePoints']
        self.new = jsonSummoner['isFreshBlood']
        self.hot_streak = jsonSummoner['isHotStreak']
        self.veteran = jsonSummoner['isVeteran']
        self.player_id = jsonSummoner['playerOrTeamId']
        self.wins = jsonSummoner['wins']
        self.losses = jsonSummoner['losses']
        self.league_name = None
        self.tier = None

    def getName(self):
        return self.name

    def getLP(self):
        return self.lp

    def getNew(self):
        return self.new

    def getHotStreak(self):
        return self.hot_streak

    def getVeteran(self):
        return self.veteran

    def getPlayerID(self):
        return self.player_id

    def getWins(self):
        return self.wins

    def getLosses(self):
        return self.losses

    def getTier(self):
        return self.tier

    def getLeagueName(self):
        return self.league_name

    def printAll(self):
        print("Name: " + str(self.getName()))
        print("LP: " + str(self.getLP()))
        print("New: " + str(self.getNew()))
        print("Hot Streak: " + str(self.getHotStreak()))
        print("Veteran: " + str(self.getVeteran()))
        print("Player ID: " + str(self.getPlayerID()))
        print("Wins: " + str(self.getWins()))
        print("Losses: " + str(self.getLosses()))
        print("Tier: " + str(self.getTier()))
        print("League Name: " + str(self.getLeagueName()))
        print("\n")
