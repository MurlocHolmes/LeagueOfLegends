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

    def printAll(self):
        print("Name: " + self.getName())
        print("LP: " + self.getLP())
        print("New: " + self.getNew())
        print("Hot Streak: " + self.getHotStreak())
        print("Veteran: " + self.getVeteran())
        print("Player ID: " + self.getPlayerID())
        print("Wins: " + self.getWins())
        print("Losses: " + self.getLosses())
