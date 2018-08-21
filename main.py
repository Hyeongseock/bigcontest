import csv_utils
import logging as log
import pandas as pd
import mask
log.basicConfig(level=log.DEBUG)

# def addGroupByCount(df):
#     # df.sort_values(by='acc_id')
#     df["count"] = 1
#     return df.groupby('acc_id').sum()  # 컬럼 추가하여 합계
#
# def addPlayTimeMean(df):
#     ## groupby('acc_id') 추가함
#     df["play_time_sum"] = df["count"].groupby('acc_id') * df["cnt_dt"].groupby('acc_id').mean()
#     df = df.groupby('acc_id').mean()
#     return df

def getPlayTimeMean(df):
    result_data = pd.DataFrame(df[['acc_id', 'cnt_dt']].groupby('acc_id')['cnt_dt'].mean(), columns=['cnt_dt'])
    # print(result_data.head())
    return result_data


def getGroupByCount(df):
    result_data = pd.DataFrame(columns=['acc_id', 'count'])
    result_data['acc_id'] = df['acc_id']
    result_data["count"] = 1
    result_data = result_data.groupby('acc_id').sum()
    # print(result_data.head())
    return result_data

if __name__ == "__main__" :
    log.info("main start")
    pd.DataFrame = mask.apply_masks()

    # 파일 경로
    root_path ="E:/NCsoft/champion_data/"

    # train_activity 원본
    train_activity = csv_utils.getTrainActivity(root_path)

    # train_activity => acc_id별 row 수
    train_activity_count = getGroupByCount(train_activity)

    # train_activity => acc_id별 playtime 평균
    train_activity_playtime_mean = getPlayTimeMean(train_activity)

    # print(getGroupByCount(train_activity).head())
    # log.debug(train_activity.gen_mask("count"))
    # log.debug(train_activity.columns)

    # train_activity_count = addGroupByCount(train_activity)
    # # log.debug(train_activity_count.head())
    # print(train_activity_count.head())
    #
    # train_activity_playtime = addPlayTimeMean(train_activity_count)
    # print(train_activity_playtime.head())

    # activity_df2 = activity_df1.groupby('acc_id').mean()

    # print(activity_df2.shape)
    # activity_df2.head()

    # train_label = csv_utils.getTrainLabel(root_path)
    # log.debug(train_label.columns)
    #
    # train_guild = csv_utils.getTrainGuild(root_path)
    # log.debug(train_guild.columns)
    #
    # train_party = csv_utils.getTrainParty(root_path)
    # log.debug(train_party.columns)
    #
    # train_payment = csv_utils.getTrainPayment(root_path)
    # log.debug(train_payment.columns)
    #
    # train_trade = csv_utils.getTrainTrade(root_path)
    # log.debug(train_trade.columns)

    log.info("main end")
