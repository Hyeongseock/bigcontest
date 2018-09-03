import pre_activity_data as act
import pre_guild_data as gld
import csv_utils
import logging as log
import pandas as pd
import mask
log.basicConfig(level=log.DEBUG)

def main() :
    ######################################### 전처리 시작 #########################################
    # 파일 경로
    root_path = "E:/NCsoft/champion_data/"

    #train_activity 데이터 전처리 하기
    # train_activity_data = train_activity_preprocessing(root_path)

    # new_activity = "E:/NCsoft/champion_data/train_preprocessing/new_train_activity"
    # act.save_file(train_activity_data, new_activity)

    # train_guild 데이터 전처리 하기
    # train_guild_data = train_guild_preprocessing(root_path)

    # new_guild = "E:/NCsoft/champion_data/train_preprocessing/new_train_guild"
    # gld.save_file(train_guild_data, new_guild)
    ######################################### 전처리 끝 #########################################


# train_guild 데이터 전처리 하기
def train_guild_preprocessing(root_path):
    # train_data 전처리하기
    train_guild_data = csv_utils.getTrainGuild(root_path)
    train_label_data = csv_utils.getTrainLabel(root_path)

    guild_data = gld.get_guild_member_cnt(train_guild_data)
    guild_member_avg = gld.get_guild_member_avg(guild_data)
    guild_member_cnt = gld.get_join_guild_cnt(guild_data)
    guild_data = gld.concat_data(guild_member_avg, guild_member_cnt)
    guild_data = gld.concat_data(train_label_data, guild_data)
    guild_data.fillna(0, inplace=True)

    return guild_data

#train_activity 데이터 전처리 하기
def train_activity_preprocessing(root_path) :
    # train_activity 원본
    train_activity_data = csv_utils.getTrainActivity(root_path)
    train_label_data = csv_utils.getTrainLabel(root_path)

    wk_data = act.get_play_wk_cnt(train_activity_data)  # 유저(acc_id)별로 총 8주 중 몇 주를 방문했는지 cnt하는 함수

    columns = ["cnt_dt", "play_time", "npc_exp", "npc_hongmun",
               "get_money", "duel_cnt", "duel_win", "partybattle_cnt",
               "partybattle_win", "cnt_enter_inzone_solo",
               "cnt_enter_inzone_light", "cnt_enter_inzone_skilled",
               "cnt_enter_inzone_normal", "cnt_enter_raid", "cnt_enter_raid_light",
               "cnt_enter_bam", "cnt_clear_inzone_solo", "cnt_clear_inzone_light",
               "cnt_clear_inzone_skilled", "cnt_clear_inzone_normal", "cnt_clear_raid",
               "cnt_clear_raid_light", "cnt_clear_bam", "normal_chat", "whisper_chat",
               "district_chat", "party_chat", "guild_chat", "faction_chat",
               "cnt_use_buffitem", "gathering_cnt", "making_cnt"]  # 변환하고자하는 컬럼만 넣으세요.

    other_data = act.get_play_cnt_dt(train_activity_data, columns)  # 유저(acc_id)별로 columns의 활동지수를 계산하는 함수

    data = act.concat_data(wk_data, other_data)  # wk + other data 합치기
    data = act.concat_data(data, train_label_data)  # data + label달기

    return data


if __name__ == "__main__" :
    main()





