import pandas as pd


def read_file(file_name) :
    data = pd.read_csv(file_name + ".csv")
    return data


def merge_data(a, b) :
    data = pd.merge(a, b, on = "acc_id", how="left")
    data.drop(["index_x", "acc_id.1", "index_y","label_y","guild_id",
               "guild_member_acc_id"], axis=1, inplace=True)
    data.fillna(0, inplace=True)
    data["wk_cnt_dt_play_time"] = data["wk_cnt"] * data["cnt_dt"] * data["play_time"]
    data["wk_cnt_dt"] = data["wk_cnt"] * data["cnt_dt"]
    return data