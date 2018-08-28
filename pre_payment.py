import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier #bagging을 위해 호출
#%matplotlib inline
from sklearn import metrics


def read_file(filename) :
    data = pd.read_csv(filename + ".csv", encoding="cp949")

    return data


def pre_payment(data, label) :

    data["cnt"] = 1
    new_data1 = pd.DataFrame(data.groupby("acc_id").sum()['cnt']).reset_index()
    new_data2 = pd.DataFrame(data.groupby("acc_id").mean()['payment_amount']).reset_index()
    new_data2.drop(["acc_id"], axis=1, inplace=True)
    data = pd.concat([new_data1, new_data2], axis=1)
    data = pd.merge(data, label, on="acc_id", how="left")

    return data

def rf_train(data) :
    label = data["label"]
    label = pd.get_dummies(label, drop_first=True)

    independent_variable = data[["payment_amount"]]

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



def save_file(data):
    data.to_csv("new_train_payment.csv", index=False)


def main() :
    data = read_file("train_payment")
    label = read_file("train_label")
    data = pre_payment(data, label)
    #save_file(data)

    rf_train(data)

if __name__ == "__main__":
    main()