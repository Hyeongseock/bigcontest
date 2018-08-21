import pandas as pd

## train_activity
def getTrainActivity(path):
    return pd.read_csv(path+'train/train_activity.csv')

## train_label
def getTrainLabel(path):
    return pd.read_csv(path+'train/train_label.csv')

## train_guild
def getTrainGuild(path):
    return pd.read_csv(path+'train/train_guild.csv')

## train_party
def getTrainParty(path):
    return pd.read_csv(path+'train/train_party.csv')

## train_payment
def getTrainPayment(path):
    return pd.read_csv(path+'train/train_payment.csv')

## train_activity
def getTrainTrade(path):
    return pd.read_csv(path+'train/train_trade.csv')
