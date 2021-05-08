from selenium import webdriver
import time
import re
import csv

def generate_table(url, league):
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url) 
    time.sleep(5)
    container = chrome.find_element_by_id('container-h2h')
    home_stats = container.find_element_by_id('h2h-team1').find_elements_by_class_name('odd')
    row = [e.text for e in home_stats]
    row_ = [r.split() for r in row]
    list_of_lists_home = [[e[1:-8],e[-8],e[-4],e[-3]] for e in row_]
    with open(f'{league}_home.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['team', 'games', 'goals_scored', 'goals_conceded'])
        [writer.writerow(r) for r in list_of_lists_home]
    container_a = chrome.find_element_by_id('container-h2h')
    away_stats = container_a.find_element_by_id('h2h-team2').find_elements_by_class_name('odd')
    row2 = [e.text for e in away_stats]
    row_2 = [r.split() for r in row2]
    list_of_lists_away = [[e[1:-8],e[-8],e[-4],e[-3]] for e in row_2]
    with open(f'{league}_away.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['team', 'games', 'goals_scored', 'goals_conceded'])
        [writer.writerow(r) for r in list_of_lists_away]
    chrome.quit()

def get_matches(url):
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url) 
    time.sleep(5)
    container = chrome.find_element_by_id('btable').find_elements_by_class_name('odd')
    rows = [el.text for el in container]
    for i in range(len(container)):
        try:    
            test = container[i].text.split(':')
            home = (test[0].split())[3:-1]
            away = (test[1].split())[1:-1]
            liss.append([home,away])
        except:
            continue
    chrome.quit()

liss = []

def get_away_gf_mean(league):
    with open(f'{league}_away.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        gf = 0
        gp = 0
        for i in range(1, len(list[0])):
            try:
                gf += int(list[0][i][2])
                gp += int(list[0][i][1])
            except:
                continue
        return gf/gp

def get_away_ga_mean(league):
    with open(f'{league}_away.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        ga = 0
        gp = 0
        for i in range(1, len(list[0])):
            try:
                ga += int(list[0][i][3])
                gp += int(list[0][i][1])
            except:
                continue
        return ga/gp

def get_home_gf_mean(league):
    with open(f'{league}_home.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        gf = 0
        gp = 0
        for i in range(1, len(list[0])):
            try:
                gf += int(list[0][i][2])
                gp += int(list[0][i][1])
            except:
                continue
        return gf/gp

def get_home_ga_mean(league):
    with open(f'{league}_home.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        ga = 0
        gp = 0
        for i in range(1, len(list[0])):
            try:
                ga += int(list[0][i][3])
                gp += int(list[0][i][1])
            except:
                continue
        return ga/gp

def get_away_stats_gf(league,index):
    with open(f'{league}_away.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        for i in range(len(list[0])):
            for j in range(len(liss)):
                try:
                    if str(list[0][i][0]) == str(index):
                        gp = int(list[0][i][1])
                        gf = int(list[0][i][2])
                        mean_away_gf = gf / gp
                        tmpgf = mean_away_gf / get_away_gf_mean(league)
                        return tmpgf       
                except:
                    continue

def get_away_stats_ga(league,index):
    with open(f'{league}_away.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        for i in range(len(list[0])):
            for j in range(len(liss)):
                try:
                    if str(list[0][i][0]) == str(index):
                        gp = int(list[0][i][1])
                        ga = int(list[0][i][3])
                        mean_away_ga = ga / gp
                        tmpga = mean_away_ga / get_away_ga_mean(league)
                        return tmpga       
                except:
                    continue

def get_home_stats_gf(league,index):
    with open(f'{league}_home.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        for i in range(len(list[0])):
            for j in range(len(liss)):
                try:
                    if str(list[0][i][0]) == str(index):
                        gp = int(list[0][i][1])
                        gf = int(list[0][i][2])
                        mean_home_gf = gf / gp
                        tmpgf = mean_home_gf / get_home_gf_mean(league)
                        return tmpgf       
                except:
                    continue

def get_home_stats_ga(league,index):
    with open(f'{league}_home.csv', 'r') as csvfile:
        reader = [csv.reader(csvfile)]
        list = [[e for e in r] for r in reader]
        for i in range(len(list[0])):
            for j in range(len(liss)):
                try:
                    if str(list[0][i][0]) == str(index):
                        gp = int(list[0][i][1])
                        ga = int(list[0][i][3])
                        mean_home_ga = ga / gp
                        tmpga = mean_home_ga / get_home_ga_mean(league)
                        return tmpga       
                except:
                    continue

def get_preds(league):
    with open(f'{league}_home.csv', 'r') as csvfileh:
        readerh = [csv.reader(csvfileh)]
        listh = [[e for e in r] for r in readerh]
    with open(f'{league}_away.csv', 'r') as csvfilea:
        readera = [csv.reader(csvfilea)]
        lista = [[e for e in r] for r in readera]
    home_stats_gf = []
    home_stats_ga = []
    away_stats_gf = [] 
    away_stats_ga = []
    for j in range(len(liss)):
        for i in range(len(listh[0])):
            try:
                if str(liss[j][0]) == str(listh[0][i][0]):
                    gph = int(listh[0][i][1])
                    gfh = int(listh[0][i][2])
                    gah = int(listh[0][i][3])
                    mean_h_f = gfh / gph
                    mean_h_a = gah / gph
                    home_stats_gf.insert(0, get_home_stats_gf(league,(listh[0][i][0])))
                    home_stats_ga.insert(0, get_home_stats_ga(league,(listh[0][i][0])))
            except:
                continue
        for k in range(len(lista[0])):
              try:
                if str(liss[j][1]) == str(lista[0][k][0]):
                   gpa = int(lista[0][k][1])
                   gfa = int(lista[0][k][2])
                   gaa = int(lista[0][k][3])
                   mean_a_f = gfa / gpa
                   mean_a_a = gaa / gpa
                   away_stats_gf.insert(0, get_away_stats_gf(league,(lista[0][k][0])))
                   away_stats_ga.insert(0, get_away_stats_ga(league,(lista[0][k][0])))
              except:
                   continue
        print(f'{(liss[j][0])} {round(home_stats_gf[0] * away_stats_ga[0] * get_home_gf_mean(league),1)} : {(liss[j][1])} {round(away_stats_gf[0] * home_stats_ga[0] * get_away_gf_mean(league),1)}')
        sum = home_stats_gf[0] * away_stats_ga[0] * get_home_gf_mean(league) + away_stats_gf[0] * home_stats_ga[0] * get_away_gf_mean(league)
        print(sum)
    print('\n') 
    liss.clear()

def get(league, table_url, matchday_url):
    generate_table(table_url, league)
    get_matches(matchday_url)
    get_preds(league)

import math

def poisson(target, avg):
    p = ((pow(avg, target))*(pow(2.71828,-avg)))/math.factorial(target)
    return p

def get_prob_over(avg):
    tmp = poisson(7,avg) + poisson(8,avg) + poisson(9,avg) + poisson(2,avg)
    sum = poisson(3,avg) + poisson(4,avg) + poisson(5,avg) + poisson(6,avg) + tmp
    return round(sum * 100)

print(f'3+ {get_prob_over(3.5)} %')

get('england','https://www.soccerstats.com/homeaway.asp?league=england','https://www.soccerstats.com/results.asp?league=england&pmtype=round98')
get('france','https://www.soccerstats.com/homeaway.asp?league=france','https://www.soccerstats.com/results.asp?league=france&pmtype=round98')
get('italy','https://www.soccerstats.com/homeaway.asp?league=italy','https://www.soccerstats.com/results.asp?league=italy&pmtype=round35')
get('spain','https://www.soccerstats.com/homeaway.asp?league=spain','https://www.soccerstats.com/results.asp?league=spain&pmtype=round98')
get('portugal','https://www.soccerstats.com/homeaway.asp?league=portugal','https://www.soccerstats.com/results.asp?league=portugal&pmtype=round98')

