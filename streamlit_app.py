#Packages import

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import plotly.graph_objects as go
import streamlit as st

#Data read

df = pd.read_csv("./Data/MotoGP_Round01_RaceResults.csv")
#df.head()


# Color/Team/Hierarchy definition

def RiderColor2022(RiderName):
    if RiderName == "Maverick VINALES" or RiderName == "Aleix ESPARGARO":
        return("#2DB914")
    elif RiderName == "Jack MILLER" or RiderName == "Francesco BAGNAIA":
        return("#F92515")
    elif RiderName == "Enea BASTIANINI" or RiderName == "Fabio DI GIANNANTONIO":
        return("#A1B7E5")
    elif RiderName == "Takaaki NAKAGAMI" or RiderName == "Alex MARQUEZ":
        return("#BBBBBB")
    elif RiderName == "Fabio QUARTARARO" or RiderName == "Franco MORBIDELLI":
        return("#183DC7")
    elif RiderName == "Luca MARINI" or RiderName == "Marco BEZZECHI":
        return("#CBEC00")
    elif RiderName == "Johann ZARCO" or RiderName == "Jorge MARTIN":
        return("#CC3333")
    elif RiderName == "Brad BINDER" or RiderName == "Miguel OLIVEIRA":
        return("#E05A17")
    elif RiderName == "Marc MARQUEZ" or RiderName == "Pol ESPARGARO":
        return("#FF9912")
    elif RiderName == "Joan MIR" or RiderName == "Alex RINS":
        return("#4294C1")
    elif RiderName == "Remy GARDNER" or RiderName == "Raul FERNANDEZ":
        return("#B7340B")
    elif RiderName == "Andrea DOVIZIOSO" or RiderName == "Darryn BINDER":
        return("#154A72")

def TeamColor2022(TeamName):
    if TeamName == "Aprilia Racing":
        return("#2DB914")
    elif TeamName == "Ducati Lenovo Team" :
        return("#F92515")
    elif TeamName == "Gresini Racing MotoGP™":
        return("#A1B7E5")
    elif TeamName == "LCR Honda":
        return("#BBBBBB")
    elif TeamName == "Monster Energy Yamaha MotoGP™" :
        return("#183DC7")
    elif TeamName == "Mooney VR46 Racing Team":
        return("#CBEC00")
    elif TeamName == "Pramac Racing":
        return("#CC3333")
    elif TeamName == "Red Bull KTM Factory Racing":
        return("#E05A17")
    elif TeamName == "Repsol Honda Team" :
        return("#FF9912")
    elif TeamName == "Team SUZUKI ECSTAR":
        return("#4294C1")
    elif TeamName == "Tech3 KTM Factory Racing":
        return("#B7340B")
    elif TeamName == "WithU Yamaha RNF MotoGP™ Team" :
        return("#154A72")
    
def BikeColor2022(BikeName):
    if BikeName == "Aprilia":
        return("#2DB914")
    elif BikeName == "Ducati" :
        return("#F92515")
    elif BikeName == "Yamaha" :
        return("#183DC7")
    elif BikeName == "KTM":
        return("#E05A17")
    elif BikeName == "Honda" :
        return("#FF9912")
    elif BikeName == "Suzuki":
        return("#4294C1")  
    
def TeamName2022(RiderName):
    if RiderName == "Maverick VINALES" or RiderName == "Aleix ESPARGARO":
        return("Aprilia Racing")
    elif RiderName == "Jack MILLER" or RiderName == "Francesco BAGNAIA":
        return("Ducati Lenovo Team")
    elif RiderName == "Enea BASTIANINI" or RiderName == "Fabio DI GIANNANTONIO":
        return("Gresini Racing MotoGP™")
    elif RiderName == "Takaaki NAKAGAMI" or RiderName == "Alex MARQUEZ":
        return("LCR Honda")
    elif RiderName == "Fabio QUARTARARO" or RiderName == "Franco MORBIDELLI":
        return("Monster Energy Yamaha MotoGP™")
    elif RiderName == "Luca MARINI" or RiderName == "Marco BEZZECHI":
        return("Mooney VR46 Racing Team")
    elif RiderName == "Johann ZARCO" or RiderName == "Jorge MARTIN":
        return("Pramac Racing")
    elif RiderName == "Brad BINDER" or RiderName == "Miguel OLIVEIRA":
        return("Red Bull KTM Factory Racing")
    elif RiderName == "Marc MARQUEZ" or RiderName == "Pol ESPARGARO":
        return("Repsol Honda Team")
    elif RiderName == "Joan MIR" or RiderName == "Alex RINS":
        return("Team SUZUKI ECSTAR")
    elif RiderName == "Remy GARDNER" or RiderName == "Raul FERNANDEZ":
        return("Tech3 KTM Factory Racing")
    elif RiderName == "Andrea DOVIZIOSO" or RiderName == "Darryn BINDER":
        return("WithU Yamaha RNF MotoGP™ Team")
    
def Bike2022(RiderName):
    if RiderName == "Maverick VINALES" or RiderName == "Aleix ESPARGARO":
        return("Aprilia")
    elif RiderName == "Jack MILLER" or RiderName == "Francesco BAGNAIA":
        return("Ducati")
    elif RiderName == "Enea BASTIANINI" or RiderName == "Fabio DI GIANNANTONIO":
        return("Ducati")
    elif RiderName == "Takaaki NAKAGAMI" or RiderName == "Alex MARQUEZ":
        return("Honda")
    elif RiderName == "Fabio QUARTARARO" or RiderName == "Franco MORBIDELLI":
        return("Yamaha")
    elif RiderName == "Luca MARINI" or RiderName == "Marco BEZZECHI":
        return("Ducati")
    elif RiderName == "Johann ZARCO" or RiderName == "Jorge MARTIN":
        return("Ducati")
    elif RiderName == "Brad BINDER" or RiderName == "Miguel OLIVEIRA":
        return("KTM")
    elif RiderName == "Marc MARQUEZ" or RiderName == "Pol ESPARGARO":
        return("Honda")
    elif RiderName == "Joan MIR" or RiderName == "Alex RINS":
        return("Suzuki")
    elif RiderName == "Remy GARDNER" or RiderName == "Raul FERNANDEZ":
        return("KTM")
    elif RiderName == "Andrea DOVIZIOSO" or RiderName == "Darryn BINDER":
        return("Yamaha")
    
def Hierarch2022(RiderName):
    if RiderName == "Maverick VINALES":
        return(2)
    elif RiderName == "Aleix ESPARGARO":
        return(1)
    elif RiderName == "Jack MILLER":
        return(2)
    elif RiderName == "Francesco BAGNAIA":
        return(1)
    elif RiderName == "Enea BASTIANINI":
        return(1)
    elif RiderName == "Fabio DI GIANNANTONIO":
        return(2)
    elif RiderName == "Takaaki NAKAGAMI":
        return(1)
    elif RiderName == "Alex MARQUEZ":
        return(2)
    elif RiderName == "Fabio QUARTARARO":
        return(1)
    elif RiderName == "Franco MORBIDELLI":
        return(2)
    elif RiderName == "Luca MARINI":
        return(1)
    elif RiderName == "Marco BEZZECHI":
        return(2)
    elif RiderName == "Johann ZARCO":
        return(2)
    elif RiderName == "Jorge MARTIN":
        return(1)
    elif RiderName == "Brad BINDER":
        return(1)
    elif RiderName == "Miguel OLIVEIRA":
        return(2)
    elif RiderName == "Marc MARQUEZ":
        return(1)
    elif RiderName == "Pol ESPARGARO":
        return(2)
    elif RiderName == "Joan MIR":
        return(1)
    elif RiderName == "Alex RINS":
        return(2)
    elif RiderName == "Remy GARDNER":
        return(1)
    elif RiderName == "Raul FERNANDEZ":
        return(2)
    elif RiderName == "Andrea DOVIZIOSO":
        return(1)
    elif RiderName == "Darryn BINDER":
        return(2)
      
      
# Dataframe tweaks

df["Color"] = df.apply(lambda row : RiderColor2022(row["Rider"]), axis=1)
df["TeamName"] = df.apply(lambda row : TeamName2022(row["Rider"]), axis=1)
df["Bike"] = df.apply(lambda row : Bike2022(row["Rider"]), axis=1)
df["Hierarch"] = df.apply(lambda row : Hierarch2022(row["Rider"]), axis=1)
teamgrouped_df = df.groupby(["TeamName", "Lap"], as_index=False).mean()
bikegrouped_df = df.groupby(["Bike", "Lap"], as_index=False).mean()



# Plotly

#Mode selection: Riders, Teams, Bike
modes = ["Rider", "Team", "Bike"]
plots = ["Lap Time", "T1", "T2", "T3", "T4"]
riderlist = pd.unique(df["Rider"])
teamlist = pd.unique(df["TeamName"])
bikelist = pd.unique(df["Bike"])


mode = st.sidebar.selectbox('Pick a mode', modes)
#mode = "Rider"

if mode == "Bike":
    #Bike average mode
    
    selectY = st.sidebar.selectbox("Pick a section" , plots)
    #selectY = "Lap Time"
    bikechosen = st.sidebar.multiselect('Select one (or more) bikes', bikelist)
    #bikechosen = ["Aprilia", "KTM"]


    fig = go.Figure()

    for bike in bikelist:

        plotX = bikegrouped_df.loc[bikegrouped_df['Bike']==bike]["Lap"]
        plotY = bikegrouped_df.loc[bikegrouped_df['Bike']==bike][selectY][1:]
        if bike in bikechosen:
            fig.add_trace(go.Scatter(x = plotX, y = plotY,
                    mode='lines+markers',
                    line=dict(color=BikeColor2022(bike), width=3),
                    marker=dict(size=8),
                    name=bike,
                    ))                
        else:
            fig.add_trace(go.Scatter(x = plotX, y = plotY,
                            mode='lines',
                            line=dict(color="#8c8c8c", width=0.5),         
                            name=bike))

    if selectY == "Lap Time" :
        Yaxistitle = "Lap"
    else:
        Yaxistitle = selectY
    
    fig.update_layout(
        width = 1000,
        height = 800,
        title= selectY + " Pace",
        xaxis_title = "Lap",
        yaxis_title = Yaxistitle + " time [s]"
    )

elif mode == "Team":
    #Team average mode

    selectY = st.sidebar.selectbox("Pick a section" , plots)
    #selectY = "Lap Time"
    teamchosen = st.sidebar.multiselect('Select one (or more) teams', teamlist)
    #teamchosen = ["Aprilia Racing", "Tech3 KTM Factory Racing"]


    fig = go.Figure()

    for team in teamlist:

        plotX = teamgrouped_df.loc[teamgrouped_df['TeamName']==team]["Lap"]
        plotY = teamgrouped_df.loc[teamgrouped_df['TeamName']==team][selectY][1:]
        if team in teamchosen:
            fig.add_trace(go.Scatter(x = plotX, y = plotY,
                    mode='lines+markers',
                    line=dict(color=TeamColor2022(team), width=3),
                    marker=dict(size=8),
                    name=team,
                    ))                
        else:
            fig.add_trace(go.Scatter(x = plotX, y = plotY,
                            mode='lines',
                            line=dict(color="#8c8c8c", width=0.5),         
                            name=team))

    if selectY == "Lap Time" :
        Yaxistitle = "Lap"
    else:
        Yaxistitle = selectY
    
    fig.update_layout(
        width = 1000,
        height = 800,
        title= selectY + " Pace",
        xaxis_title = "Lap",
        yaxis_title = Yaxistitle + " time [s]"
    )
    
else:
    #Rider mode
    
    selectY = st.sidebar.selectbox("Pick a section" , plots)
    #selectY = "Lap Time"
    riderchosen = st.sidebar.multiselect('Select one (or more) riders', riderlist)
    #riderchosen = ["Marc MARQUEZ", "Francesco BAGNAIA", "Pol ESPARGARO"]


    fig = go.Figure()

    for rider in riderlist:

        plotX = df.loc[df['Rider']==rider]["Lap"]
        plotY = df.loc[df['Rider']==rider][selectY][1:]
        if rider in riderchosen:
            if Hierarch2022(rider) == 2:
                fig.add_trace(go.Scatter(x = plotX, y = plotY,
                                mode='lines+markers',
                                line=dict(color=RiderColor2022(rider), width=3, dash='dash'),
                                marker=dict(size=8),
                                name=rider,
                                ))
            else:
                fig.add_trace(go.Scatter(x = plotX, y = plotY,
                                mode='lines+markers',
                                line=dict(color=RiderColor2022(rider), width=3),
                                marker=dict(size=8),
                                name=rider))
                
        else:
            fig.add_trace(go.Scatter(x = plotX, y = plotY,
                            mode='lines',
                            line=dict(color="#8c8c8c", width=0.5),         
                            name=rider))

if selectY == "Lap Time" :
    Yaxistitle = "Lap"
else:
    Yaxistitle = selectY
    
fig.update_layout(
    width = 800,
    height = 1000,
    title= selectY + " Pace per " + mode,
    xaxis_title = "Lap",
    yaxis_title = Yaxistitle + " time [s]"
)

st.plotly_chart(fig, use_container_width=False)
#fig.show()
