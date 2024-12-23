import data
class Player1:
    def __init__(self, pid):
        self.query = {"template":"results"}
        self.playerid=pid
        self.pdata=[]

    def totalstats(self, params):
        self.query.update(params)
        process=data.Data(self.query)
        other=""
        totalstat=process.playerdata1(self.playerid, params, other, )
        return totalstat
    
    def innlist(self, params):
        self.query.update(params)
        process = data.Data(self.query)
        other="view=innings"
        inns = process.playerdata1(self.playerid, params, other)
        return inns

    def matchlist(self, params):
        self.query.update(params)
        other="view=matches"
        process = data.Data(self.query)
        matches = process.playerdata1(self.playerid, params, other)
        return matches

    def cavg(self, params):
        self.query.update(params)
        other="view= cumulative"
        process = data.Data(self.query)
        cum = process.playerdata1(self.playerid, params, other, params, other)
        return cum

    def savg(self, params):
        self.query.update(params)
        other="view=series"
        process = data.Data(self.query)
        savg = process.playerdata1(self.playerid, params, other)
        return savg

    def gavg(self, params):
        self.query.update(params)
        other="view=ground"
        process = data.Data(self.query)
        gavg = process.playerdata1(self.playerid, params, other)
        return gavg

    def results(self, params):
        self.query.update(params)
        other="view=results"
        process = data.Data(self.query)
        results = process.playerdata1(self.playerid, params, other)
        return results

    def maw(self, params):
        self.query.update(params)
        other="view=awards_match"
        process = data.Data(self.query)
        maw = process.playerdata1(self.playerid, params, other)
        return maw

    def saw(self, params):
        self.query.update(params)
        other="view=awards_series"
        process = data.Data(self.query)
        saw = process.playerdata1(self.playerid, params, other)
        return saw

#Batting list    
    def pship_total(self, params):
        self.query.update(params)
        other="view=fow_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            pships = process.playerdata1(self.playerid, params, other)
            return pships
        else:
            print("Available only for batting data")

    def pship_list(self, params):
        self.query.update(params)
        other="view=fow_list"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            pships = process.playerdata1(self.playerid, params, other)
            return pships
        else:
            print("Available only for batting data")

    def dis_total(self, params):
        self.query.update(params)
        other="view=dismissal_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            dis = process.playerdata1(self.playerid, params, other)
            return dis
        else:
            print("Available only for batting data")
    
    def bow_total(self, params):
        self.query.update(params)
        other="view=bowler_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            bt = process.playerdata1(self.playerid, params, other)
            return bt
        else:
            print("Available only for batting data")
    
    def fl_total(self, params):
        self.query.update(params)
        other="view=fielder_summary"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            flt = process.playerdata1(self.playerid, params, other)
            return flt
        else:
            print("Available only for batting data")
    
    def dis_list(self, params):
        self.query.update(params)
        other="view=dismissal_list"
        if self.query["type"]=="batting":
            process = data.Data(self.query)
            disl = process.playerdata1(self.playerid, params, other)
            return disl
        else:
            print("Available only for batting data")

#Bowling data
    def dis_sum(self, params):
        self.query.update(params)
        other="view=dismissal_summary"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            dism = process.playerdata1(self.playerid, params, other)
            return dism
        else:
            print("Available only for bowling data")
    
    def b_sum(self, params):
        self.query.update(params)
        other="view=batsman_summary"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            bats = process.playerdata1(self.playerid, params, other)
            return bats
        else:
            print("Available only for bowling data")

    def f_sum(self, params):
        self.query.update(params)
        other="view=fielder_summary"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            fsum = process.playerdata1(self.playerid, params, other)
            return fsum
        else:
            print("Available only for bowling data")
        
    def wlist(self, params):
        self.query.update(params)
        other="view=dismissal_list"
        if self.query["type"]=="bowling":
            process = data.Data(self.query)
            dlist = process.playerdata1(self.playerid, params, other)
            return dlist
        else:
            print("Available only for bowling data")
    
#Fielding data
    def fdis_sum(self, params):
        self.query.update(params)
        other="view=dismissal_summary"
        if self.query["type"]=="fielding":
            process = data.Data(self.query)
            dism = process.playerdata1(self.playerid, params, other)
            return dism
        else:
            print("Available only for fielding data")
    def fdis_bat(self, params):
        self.query.update(params)
        other="view=batsman_summary"
        if self.query["type"]=="fielding":
            process = data.Data(self.query)
            dism = process.playerdata1(self.playerid, params, other)
            return dism
        else:
            print("Available only for fielding data")
    def fdis_bow(self, params):
        self.query.update(params)
        other="view=bowler_summary"
        if self.query["type"]=="fielding":
            process = data.Data(self.query)
            dism = process.playerdata1(self.playerid, params, other)
            return dism
        else:
            print("Available only for fielding data")
    def fdis_list(self, params):
        self.query.update(params)
        other="view=dismissal_list"
        if self.query["type"]=="fielding":
            process = data.Data(self.query)
            dism = process.playerdata1(self.playerid, params, other)
            return dism
        else:
            print("Available only for fielding data")
    