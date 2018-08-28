import pandas as pd

def read_file(filename) :
    data = pd.read_csv(filename + ".csv", encoding="cp949")
    return data

def get_play_wk_cnt(data) :
    data["wk_cnt"] = 1
    wk_data = data.groupby(["acc_id"], as_index=False)["wk_cnt"].sum()
    wk_data = pd.DataFrame(wk_data)
    return wk_data

def get_play_cnt_dt(data) :
    week_cnt_data = data.groupby(["acc_id"], as_index=False)["cnt_dt","play_time","npc_exp", "npc_hongmun",
                                                             "quest_exp","quest_hongmun","item_hongmun","game_combat_time",
                                                             "get_money", "duel_cnt",	"duel_win", "partybattle_cnt",
                                                             "partybattle_win", "cnt_enter_inzone_solo",
                                                             "cnt_enter_inzone_light", "cnt_enter_inzone_skilled",
                                                             "cnt_enter_inzone_normal",	"cnt_enter_raid",	"cnt_enter_raid_light",
                                                             "cnt_enter_bam",	"cnt_clear_inzone_solo",	"cnt_clear_inzone_light",
                                                             "cnt_clear_inzone_skilled",	"cnt_clear_inzone_normal",	"cnt_clear_raid",
                                                             "cnt_clear_raid_light",	"cnt_clear_bam",	"normal_chat",	"whisper_chat",
                                                             "district_chat",	"party_chat",	"guild_chat",	"faction_chat",
                                                             "cnt_use_buffitem",	"gathering_cnt",	"making_cnt"].mean()
    week_cnt_data = pd.DataFrame(week_cnt_data)

    return week_cnt_data


def concat_data(a, b) :
    data = pd.concat([a, b], axis=1)
    return data

def save_file(data, filename) :
    data.to_csv(filename, index=False)

def main() :
    activity = read_file("test_activity")
    a = get_play_wk_cnt(activity)
    b = get_play_cnt_dt(activity)
    data = concat_data(a, b)
    save_file(data, "pre_test_activity_data.csv")

if __name__ =="__main__":
    main()