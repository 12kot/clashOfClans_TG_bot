import SheetsAPI
import Parser
import gspread

gc = gspread.service_account(filename='D:/Projects/Python/CoC/service_nik.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WXli0D45kkwCV1fq2zB3WSkuzT0XPiMrhYDrk-zypQA/').sheet1
data = Parser.GetRaidsInfo()

SheetsAPI.setRaidResults(sh, data)
SheetsAPI.checkPlayers(sh)