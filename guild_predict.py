import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #bagging을 위해 호출
#%matplotlib inline
from sklearn import metrics


def read_file(file_name) :
    data = pd.read_csv(file_name + ".csv")
    return data

def save_file(data) :
    data.to_csv("train_guild_data(add_member_cnt).csv", index=False)

def guild_preprocess(data) :
    data = data.dropna()
    data.reset_index(inplace=True)
    for i in range(len(data["guild_member_acc_id"])):
        member = data.ix[i, "guild_member_acc_id"]
        member = member.split(",")
        data.ix[i, "member_cnt"] = len(member)

    return data

def rf_train(data) :
    label = data["label"]
    label = pd.get_dummies(label, drop_first=True)

    independent_variable = data[["member_cnt"]]

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


def get_plot(data) :
    data["member_cnt"].hist(by=data["label"])

def main() :
    data = read_file("train_guild_new")
    data = guild_preprocess(data)
    save_file(data)
    data = read_file("train_guild_data(add_member_cnt)")
    rf_train(data)

if __name__ == "__main__" :
    main()