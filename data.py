import lxml
from urllib.parse import urlencode
from bs4 import BeautifulSoup as bs
import csv as csv
import pandas as pd
class Data:
    def __init__(self, params):
        self.params = params
        self.pgcounter=0
    def playerdata1(self, pid, params, other):
        url="https://stats.espncricinfo.com/ci/engine/player/"+str(pid)+".html?class="+(params['class'])+";template=results;type="+(params['type'])+";"+other
        encodedp=urlencode(self.params)
        url=url.format(encodedp, str(self.pgcounter)) #to format to simple html
        df=pd.read_html(url) 
        data=df[2] #df is dataframe aka table in pandas
        rqdata1=data.loc[:] #tilde is "not"
        return rqdata1
    def playerdata2(self, pid, params, other):
        url="https://stats.espncricinfo.com/ci/engine/player/"+str(pid)+".html?class="+(params['class'])+";template=results;type="+(params['type']+";"+other)
        encodedp=urlencode(self.params)
        url=url.format(encodedp, str(self.pgcounter)) #to format to simple html
        df=pd.read_html(url) 
        data=df[3] #df is dataframe aka table in pandas
        rqdata2=data.loc[:] #tilde is "not"
        return rqdata2