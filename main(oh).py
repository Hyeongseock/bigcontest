import pre_activity_data as act


def main() :
#---------------activity_data 전처리하기-----------------------------------------------
    #train_activity 데이터 전처리 하기
    activity = "C:/Users/ohs/Downloads/final_data_rev/train/train_activity"
    label = "C:/Users/ohs/Downloads/final_data_rev/train/train_label"
    activity_data = act.read_file(activity)
    label_data = act.read_file(label)
    wk_data = act.get_play_wk_cnt(activity_data)#유저(acc_id)별로 총 8주 중 몇 주를 방문했는지 cnt하는 함수
    other_data = act.get_play_cnt_dt(activity_data)#유저(acc_id)별로 활동지수를 계산하는 함수
    data = act.concat_data(wk_data, other_data)#wk + other data 합치기
    data = act.concat_data(data, label_data)  # data + label달기
    new_activity = "C:/Users/ohs/Downloads/final_data_rev/train/new_train_activity"
    act.save_file(data, new_activity)

    # test_activity데이터 전처리 하기
    activity = "C:/Users/ohs/Downloads/final_data_rev/test/test_activity"
    activity_data = act.read_file(activity)
    wk_data = act.get_play_wk_cnt(activity_data)  # 유저(acc_id)별로 총 8주 중 몇 주를 방문했는지 cnt하는 함수
    other_data = act.get_play_cnt_dt(activity_data)  # 유저(acc_id)별로 활동지수를 계산하는 함수
    data = act.concat_data(wk_data, other_data)  # wk + other data 합치기
    new_activity = "C:/Users/ohs/Downloads/final_data_rev/test/new_test_activity"
    act.save_file(data, new_activity)



if __name__ == "__main__" :
    main()