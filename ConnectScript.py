#TODO: move to a class structure for easier maintainability
#pandas is the stats library and sqlite3 is a sql database library
import pandas as pd
import sqlite3

#imports a csv and makes a table in a sql database
#prints out sample rows if successful
def Import_SSD():
    ssd = pd.read_csv("CS_ScannedSurveyData.csv")
    conn = sqlite3.connect("surveyDb")
    ssd.to_sql("ScannedSurveyData", conn, if_exists="replace")
    conn.commit()
    ssd_table = pd.io.sql.read_sql("SELECT * FROM ScannedSurveyData;", conn, index_col='index')
    print(ssd_table.head())


#converts nulls to 0 and tranposes numbers
def Create_SR():
    conn = sqlite3.connect("surveyDb")
    ssd_table = pd.io.sql.read_sql("SELECT * FROM ScannedSurveyData;", conn, index_col='index')
    filled = ssd_table.fillna(0)
    sr = pd.melt(filled, id_vars=['Unique Response Number'], value_vars=list(filled.columns[1:]))
    sr.to_sql("ScannedResponses", conn, if_exists="replace")
    conn.commit()
    sr_table = pd.io.sql.read_sql("SELECT * FROM ScannedResponses;", conn, index_col='index')
    print(sr_table.head())

#create
def Create_Columns(qCount):
    conn = sqlite3.connect("surveyDb")
    ssd_table = pd.io.sql.read_sql("SELECT * FROM ScannedSurveyData;", conn, index_col='index')
    qCount += 1
    print(qCount)

Create_Columns(236)



