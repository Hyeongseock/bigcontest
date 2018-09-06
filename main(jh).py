import pre_activity_data as act
import pre_guild_data as gld
import pre_payment as pay
import csv_utils
import logging as log
import pandas as pd
import mask
log.basicConfig(level=log.DEBUG)

# def rf_train(data) :
#     label = data["label"]
#     label = pd.get_dummies(label, drop_first=True)
#
#     independent_variable = data[["member_cnt"]]
#
#     #print('Training Features Shape:', independent_variable.shape)
#     #print('Training Labels Shape:', label.shape)
#
#     train_data, test_data, train_label, test_label = \
#         train_test_split(independent_variable, label)
#     clf_rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#                                     max_depth=None, max_features="auto", max_leaf_nodes=None,
#                                     min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2,
#                                     min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#                                     oob_score=False, random_state=None, verbose=0, warm_start=False)
#     #print('Training Features Shape:', train_data.shape)
#     #print('Training Labels Shape:', train_label.shape)
#     #print('Training Features Shape:', test_data.shape)
#     #print('Training Labels Shape:', test_label.shape)
#     clf_rf.fit(train_data, train_label)
#     rf_pre = clf_rf.predict(test_data)
#     as_score_rf = metrics.accuracy_score(test_label, rf_pre)
#     print(as_score_rf*100)
#

def main() :
    pd.DataFrame = mask.apply_masks()
    pri_key = "acc_id"
    ######################################### 전처리 시작 #########################################
    # 파일 경로
    root_path = "E:/NCsoft/champion_data/"
    train_label_data = csv_utils.getTrainLabel(root_path)

    # week_data = train_label_data.set_index('label').filter(like="week", axis=0)
    # week_data['week_val']=1
    # retained_data = train_label_data.set_index('label').filter(like="retained", axis=0)
    # retained_data['retained_val'] = 1
    # month_data = train_label_data.set_index('label').filter(regex="^month", axis=0)
    # month_data['month_val'] = 1
    # month2_data = train_label_data.set_index('label').filter(regex="2month", axis=0)
    # month2_data['month2_val'] = 1
    #
    # train_label_data = gld.concat_data(train_label_data, week_data)
    # train_label_data = gld.concat_data(train_label_data, retained_data)
    # train_label_data = gld.concat_data(train_label_data, month_data)
    # train_label_data = gld.concat_data(train_label_data, month2_data)
    #
    # train_label_data.fillna(0, inplace=True)
    #
    # new_label = "E:/NCsoft/champion_data/train_preprocessing/new_train_label"
    # gld.save_file(train_label_data, new_label)



    # test_label_data = csv_utils.getTestLabel(root_path)
    #
    # final_label_data = pd.merge(test_label_data, train_label_data, how='left', on='acc_id')
    # print(final_label_data.head())



    # new_label = "E:/NCsoft/champion_data/result/result_label"
    # gld.save_file(final_label_data, new_label)

    #train_activity 데이터 전처리 하기
    # train_activity_data = train_activity_preprocessing(root_path)

    # new_activity = "E:/NCsoft/champion_data/train_preprocessing/new_train_activity"
    # act.save_file(train_activity_data, new_activity)

    # train_guild 데이터 전처리 하기
    # train_guild_data = train_guild_preprocessing(root_path)
    #
    # new_guild = "E:/NCsoft/champion_data/train_preprocessing/new_train_guild"
    # gld.save_file(train_guild_data, new_guild)

    # train_payment 데이터 전처리 하기
    train_payment_data = train_payment_preprocessing(root_path)

    new_payment = "E:/NCsoft/champion_data/train_preprocessing/new_train_payment"
    gld.save_file(train_payment_data, new_payment)
    ######################################### 전처리 끝 #########################################


#train_payment 데이터 전처리 하기
def train_payment_preprocessing(root_path) :
    # train_payment 원본
    train_payment_data = csv_utils.getTrainPayment(root_path)
    train_label_data = pd.read_csv(root_path+'train_preprocessing/new_train_label.csv')

    train_payment_data["cnt"] = 1
    # new_data1 = pd.DataFrame(train_payment_data.set_index('payment_amount').filter(like="149898470874251", axis=0).groupby("acc_id").sum()['cnt']).reset_index()
    new_data1 = pd.DataFrame(train_payment_data.groupby("acc_id").sum()['cnt']).reset_index()
    print(new_data1.size)
    new_data0 = pd.DataFrame(train_payment_data.set_index('payment_amount').filter(like="149898470874251", axis=0).groupby("acc_id").sum()['cnt']).reset_index()
    new_data0['cnt'] = 8 - new_data0['cnt']

    new_data2 = pd.DataFrame(train_payment_data.groupby("acc_id").mean()['payment_amount']).reset_index()
    new_data3 = pd.DataFrame(train_payment_data.groupby("acc_id").max()['payment_amount']).reset_index()
    new_data4 = pd.DataFrame(train_payment_data.groupby("acc_id").min()['payment_amount']).reset_index()
    # new_data0.drop(["acc_id"], axis=1, inplace=True)
    new_data2.drop(["acc_id"], axis=1, inplace=True)
    new_data3.drop(["acc_id"], axis=1, inplace=True)
    new_data4.drop(["acc_id"], axis=1, inplace=True)
    # data = pd.concat([new_data4, new_data1], axis=1)
    data = pd.merge(new_data1, new_data0, on="acc_id", how="left").fillna(0, inplace=True)
    data = pd.concat([data, new_data2], axis=1)
    data = pd.concat([data, new_data3], axis=1)
    data = pd.concat([data, new_data4], axis=1)
    data = pd.merge(data, train_label_data, on="acc_id", how="left")


    # pay_data = pay.pre_payment(train_payment_data, train_label_data)  # 유저(acc_id)별로 총 8주 중 몇 주를 방문했는지 cnt하는 함수


    return data

# train_guild 데이터 전처리 하기
def train_guild_preprocessing(root_path):
    # train_data 전처리하기
    train_guild_data = csv_utils.getTrainGuild(root_path)
    train_label_data = pd.read_csv(root_path+'train_preprocessing/new_train_label.csv')

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





