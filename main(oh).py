import pre_activity_data as act
import pre_guild_data as gld

def main() :
    '''
#---------------activity_data 전처리하기-----------------------------------------------
    #train_activity 데이터 전처리 하기
    activity = "C:/Users/ohs/Downloads/final_data_rev/train/train_activity"
    label = "C:/Users/ohs/Downloads/final_data_rev/train/train_label"
    activity_data = act.read_file(activity)
    label_data = act.read_file(label)

    wk_data = act.get_play_wk_cnt(activity_data)#유저(acc_id)별로 총 8주 중 몇 주를 방문했는지 cnt하는 함수


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

    other_data = act.get_play_cnt_dt(activity_data, columns)#유저(acc_id)별로 columns의 활동지수를 계산하는 함수

    data = act.concat_data(wk_data, other_data)#wk + other data 합치기
    data = act.concat_data(data, label_data)  # data + label달기
    new_activity = "C:/Users/ohs/Downloads/final_data_rev/train/new_train_activity"
    act.save_file(data, new_activity)

    # test_activity데이터 전처리 하기
    activity = "C:/Users/ohs/Downloads/final_data_rev/test/test_activity"
    activity_data = act.read_file(activity)
    wk_data = act.get_play_wk_cnt(activity_data)  # 유저(acc_id)별로 총 8주 중 몇 주를 방문했는지 cnt하는 함수
    other_data = act.get_play_cnt_dt(activity_data, columns)  # 유저(acc_id)별로 활동지수를 계산하는 함수
    data = act.concat_data(wk_data, other_data)  # wk + other data 합치기
    new_activity = "C:/Users/ohs/Downloads/final_data_rev/test/new_test_activity"
    act.save_file(data, new_activity)
    '''

#---------------guild_data 전처리하기-----------------------------------------------
    #train_data 전처리하기
    guild = "C:/Users/ohs/Downloads/final_data_rev/train/train_guild"
    label = "C:/Users/ohs/Downloads/final_data_rev/train/train_label"
    guild_data = gld.read_file(guild)
    label_data = gld.read_file(label)

    guild_data = gld.get_guild_member_cnt(guild_data)
    guild_member_avg = gld.get_guild_member_avg(guild_data)
    guild_member_cnt = gld.get_join_guild_cnt(guild_data)
    guild_data = gld.concat_data(guild_member_avg,guild_member_cnt)
    guild_data = gld.concat_data(label_data, guild_data)
    guild_data.fillna(0, inplace=True)

    new_guild = "C:/Users/ohs/Downloads/final_data_rev/train/new_train_guild"
    gld.save_file(guild_data, new_guild)


    #test_data 전처리하기
    guild = "C:/Users/ohs/Downloads/final_data_rev/test/test_guild"
    label = "C:/Users/ohs/Downloads/final_data_rev/test/test_activity"#acc_id가져오기위해사용
    guild_data = gld.read_file(guild)
    label_data = gld.read_file(label)
    label_data = gld.get_acc_id(label_data)

    guild_data = gld.get_guild_member_cnt(guild_data)
    guild_member_avg = gld.get_guild_member_avg(guild_data)
    guild_member_cnt = gld.get_join_guild_cnt(guild_data)
    guild_data = gld.concat_data(guild_member_avg,guild_member_cnt)
    guild_data = gld.concat_data(label_data, guild_data)
    guild_data.fillna(0, inplace=True)

    new_guild = "C:/Users/ohs/Downloads/final_data_rev/test/new_test_guild"
    gld.save_file(guild_data, new_guild)





if __name__ == "__main__" :
    main()