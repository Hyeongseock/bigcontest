import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #bagging을 위해 호출
#%matplotlib inline
from sklearn import metrics
def read_file(file_name) :
    data = pd.read_csv(file_name + ".csv")
    return data

def merge_data(a, b) :
    data = pd.merge(a, b, on = "acc_id", how="left")

    data.fillna(0, inplace=True)
    data["wk_cnt_dt_play_time"] = data["wk_cnt"] * data["cnt_dt"] * data["play_time"]
    data["wk_cnt_dt"] = data["wk_cnt"] * data["cnt_dt"]
    return data

def save_file(data) :
    data.to_csv("result_test_activity_guild.csv", index=False)

def rf_train(data) :
    label = data["label_x"]
    label = pd.get_dummies(label, drop_first=True)

    independent_variable = data[["wk_cnt","cnt_dt","play_time","wk_cnt_dt","member_cnt","wk_cnt_dt_play_time",
                                "npc_exp", "npc_hongmun",
                                "quest_exp", "quest_hongmun", "item_hongmun", "game_combat_time",
                                "get_money", "duel_cnt", "duel_win", "partybattle_cnt",
                                "partybattle_win", "cnt_enter_inzone_solo",
                                "cnt_enter_inzone_light", "cnt_enter_inzone_skilled",
                                "cnt_enter_inzone_normal", "cnt_enter_raid", "cnt_enter_raid_light",
                                "cnt_enter_bam", "cnt_clear_inzone_solo", "cnt_clear_inzone_light",
                                "cnt_clear_inzone_skilled", "cnt_clear_inzone_normal", "cnt_clear_raid",
                                "cnt_clear_raid_light", "cnt_clear_bam", "normal_chat", "whisper_chat",
                                "district_chat", "party_chat", "guild_chat", "faction_chat",
                                "cnt_use_buffitem", "gathering_cnt", "making_cnt" ]]

    #print('Training Features Shape:', independent_variable.shape)
    #print('Training Labels Shape:', label.shape)

    train_data, test_data, train_label, test_label = \
        train_test_split(independent_variable, label)
    clf_rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                    max_depth=None, max_features="auto", max_leaf_nodes=None,
                                    min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2,
                                    min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
                                    oob_score=False, random_state=None, verbose=0, warm_start=False)
    #print('Training Features Shape:', train_data.shape)
    #print('Training Labels Shape:', train_label.shape)
    #print('Training Features Shape:', test_data.shape)
    #print('Training Labels Shape:', test_label.shape)
    clf_rf.fit(train_data, train_label)
    rf_pre = clf_rf.predict(test_data)
    as_score_rf = metrics.accuracy_score(test_label, rf_pre)
    print(as_score_rf*100)


def rf_predict(train_data, test_data) :
    train_label = train_data["label_x"]
    train_label = pd.get_dummies(train_label, drop_first=True)
    #print(train_label)

    train_data = train_data[["wk_cnt","cnt_dt","play_time","wk_cnt_dt","member_cnt","wk_cnt_dt_play_time",
                                "npc_exp", "npc_hongmun",
                                "quest_exp", "quest_hongmun", "item_hongmun", "game_combat_time",
                                "get_money", "duel_cnt", "duel_win", "partybattle_cnt",
                                "partybattle_win", "cnt_enter_inzone_solo",
                                "cnt_enter_inzone_light", "cnt_enter_inzone_skilled",
                                "cnt_enter_inzone_normal", "cnt_enter_raid", "cnt_enter_raid_light",
                                "cnt_enter_bam", "cnt_clear_inzone_solo", "cnt_clear_inzone_light",
                                "cnt_clear_inzone_skilled", "cnt_clear_inzone_normal", "cnt_clear_raid",
                                "cnt_clear_raid_light", "cnt_clear_bam", "normal_chat", "whisper_chat",
                                "district_chat", "party_chat", "guild_chat", "faction_chat",
                                "cnt_use_buffitem", "gathering_cnt", "making_cnt" ]]

    #print('Training Features Shape:', independent_variable.shape)
    #print('Training Labels Shape:', label.shape)

    clf_rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                    max_depth=None, max_features="auto", max_leaf_nodes=None,
                                    min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2,
                                    min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
                                    oob_score=False, random_state=None, verbose=0, warm_start=False)
    #print('Training Features Shape:', train_data.shape)
    #print('Training Labels Shape:', train_label.shape)
    #print('Training Features Shape:', test_data.shape)
    #print('Training Labels Shape:', test_label.shape)
    clf_rf.fit(train_data, train_label)
    test_id = test_data["acc_id"]
    test_data = test_data[["wk_cnt", "cnt_dt", "play_time", "wk_cnt_dt", "member_cnt", "wk_cnt_dt_play_time",
                             "npc_exp", "npc_hongmun",
                             "quest_exp", "quest_hongmun", "item_hongmun", "game_combat_time",
                             "get_money", "duel_cnt", "duel_win", "partybattle_cnt",
                             "partybattle_win", "cnt_enter_inzone_solo",
                             "cnt_enter_inzone_light", "cnt_enter_inzone_skilled",
                             "cnt_enter_inzone_normal", "cnt_enter_raid", "cnt_enter_raid_light",
                             "cnt_enter_bam", "cnt_clear_inzone_solo", "cnt_clear_inzone_light",
                             "cnt_clear_inzone_skilled", "cnt_clear_inzone_normal", "cnt_clear_raid",
                             "cnt_clear_raid_light", "cnt_clear_bam", "normal_chat", "whisper_chat",
                             "district_chat", "party_chat", "guild_chat", "faction_chat",
                             "cnt_use_buffitem", "gathering_cnt", "making_cnt"]]

    rf_pre = clf_rf.predict(test_data)
    rf_pre = pd.DataFrame(rf_pre)

    return rf_pre

def get_result_data(test_data, rf_pre) :
    #print(rf_pre)

    rf_pre.columns = ["month", "retained","week"]
    #rf_pre = rf_pre.rename(columns={'0': 'month', '1': 'retained','2': 'week'})
    rf_pre.loc[rf_pre["month"]==1, "label"] = "month"
    rf_pre.loc[rf_pre["retained"] == 1, "label"] = "retained"
    rf_pre.loc[rf_pre["week"] == 1, "label"] = "week"
    rf_pre.fillna("2month", inplace=True)
    result = pd.concat([test_data["acc_id"],rf_pre], axis=1)
    #print(result)
    result.drop(["month", "retained","week"], axis=1, inplace=True)
    result = result.drop_duplicates(subset="acc_id", keep="first")
    print(result)

    return result


def main() :
    train_activty_data = read_file("activity_data")
    train_guild_data = read_file("train_guild_data(add_member_cnt)")

    train_activty_data.reset_index(inplace=True)
    train_guild_data.reset_index(inplace=True)
    train_data = merge_data(train_activty_data, train_guild_data)
    #save_file(data)
    rf_train(train_data)
    '''
    test_activty_data = read_file("pre_test_activity_data")
    test_guild_data = read_file("pre_test_guild_data")

    test_activty_data.reset_index(inplace=True)
    test_guild_data.reset_index(inplace=True)
    test_data = merge_data(test_activty_data, test_guild_data)

    data = read_file("train_new_activity_guild")
    rf_train(data)
    result = rf_predict(train_data, test_data)

    #result = get_result_data(test_data,result)
    #save_file(result)
    '''
if __name__ == "__main__" :
    main()


