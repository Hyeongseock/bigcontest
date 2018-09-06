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


## test_activity
def getTestActivity(path):
    return pd.read_csv(path+'test/test_activity.csv')

## test_label
def getTestLabel(path):
    return pd.read_csv(path+'test/test_label.csv')

## test_guild
def getTestGuild(path):
    return pd.read_csv(path+'test/test_guild.csv')

## test_party
def getTestParty(path):
    return pd.read_csv(path+'test/test_party.csv')

## test_payment
def getTestPayment(path):
    return pd.read_csv(path+'test/test_payment.csv')

## test_activity
def getTestTrade(path):
    return pd.read_csv(path+'test/test_trade.csv')
