import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #bagging을 위해 호출
#%matplotlib inline
from sklearn import metrics

def read_file(file_name) :
    data = pd.read_csv(file_name + ".csv")
    return data

def get_play_wk_cnt(data) :
    data["wk_cnt"] = 1
    wk_data = data.groupby(["acc_id","label"], as_index=False)["wk_cnt"].sum()
    wk_data = pd.DataFrame(wk_data)
    return wk_data

def get_play_wk_cnt_for_test(data) :
    data["wk_cnt"] = 1
    wk_data = data.groupby(["acc_id"], as_index=False)["wk_cnt"].sum()
    wk_data = pd.DataFrame(wk_data)
    return wk_data


def get_play_cnt_dt(data) :

    week_cnt_data = data.groupby(["acc_id"], as_index=False)["cnt_dt","play_time"].mean()
    week_cnt_data = pd.DataFrame(week_cnt_data)
    #print(week_cnt_data)
    return week_cnt_data

def concat_data(a, b) :
    data = pd.concat([a, b], axis=1)
    return data

def rf_train(train_data, test_data) :
    label = train_data["label"]
    train_label = pd.get_dummies(label, drop_first=True)
    #print(label[0:10], train_label[0:10])

    train_data = train_data[["wk_cnt","cnt_dt","play_time"]]
    test_data = test_data[["wk_cnt","cnt_dt","play_time"]]
    #print('Training Features Shape:', independent_variable.shape)
    #print('Training Labels Shape:', label.shape)

    #train_data, test_data, train_label, test_label = \
        #train_test_split(independent_variable, label)

    clf_rf = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                    max_depth=None, max_features="auto", max_leaf_nodes=None,
                                    min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2,
                                    min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
                                    oob_score=False, random_state=None, verbose=0, warm_start=False)
    clf_rf.fit(train_data, train_label)
    rf_pre = clf_rf.predict(test_data)
    #as_score_rf = metrics.accuracy_score(test_label, rf_pre)
    #print(as_score_rf*100)
    rf_pre = pd.DataFrame(rf_pre)
    #result_data = rf_pre
    #print(rf_pre[0:10])
    #result_data = pd.concat([test_data["acc_id"],re_pre[1,2,3]])
    return rf_pre



def get_result_data(test_data, rf_pre) :

    rf_pre.columns = ["month", "retained","week"]
    #rf_pre = rf_pre.rename(columns={'0': 'month', '1': 'retained','2': 'week'})
    rf_pre.loc[rf_pre["month"]==1, "label"] = "month"
    rf_pre.loc[rf_pre["retained"] == 1, "label"] = "retained"
    rf_pre.loc[rf_pre["week"] == 1, "label"] = "week"
    rf_pre.fillna("2month", inplace=True)
    result = pd.concat([test_data,rf_pre], axis=1)
    result.drop(["wk","1","2"], axis=1, inplace=True)
    return result

def save_file(data) :
    data.to_csv("result.csv", index=False)

def main() :
    train_data =read_file("train_acitivity_new")
    #rf_train(data)
    a = get_play_wk_cnt(train_data)
    b = get_play_cnt_dt(train_data)
    train_data = concat_data(a, b)
    test_data = read_file("test_activity")
    c = get_play_wk_cnt_for_test(test_data)
    d = get_play_cnt_dt(test_data)
    test_data = concat_data(c, d)
    result = rf_train(train_data, test_data)
    result = get_result_data(test_data,result)
    save_file(result)


if __name__ == "__main__" :
    main()