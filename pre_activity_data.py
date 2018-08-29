import pandas as pd

#---------------------------------------------------------------
#csv 파일을 dataframe 형태로 불러들임
#기본으로 불러올 경우 1행은 컬럼으로 지정됨
#파일 혹은 파일명을 포함하여 path를 입력하면 사용 가능
def read_file(filename) :
    data = pd.read_csv(filename + ".csv", encoding="cp949")
    return data

#--------------------------------------------------------------
#유저(acc_id)별로 총 8주 중 몇 주를 방문했는지 cnt하는 함수
#기존의 activity_data의 경우 acc_id로 groupby가 되어있지 않으므로,
#기존의 activity_data에서 사용할 변수들만 groupby로 만든 후, merge나 concat하여 예측에 사용
def get_play_wk_cnt(data) :
    data["wk_cnt"] = 1
    wk_data = data.groupby(["acc_id"], as_index=False)["wk_cnt"].sum()
    wk_data = pd.DataFrame(wk_data)
    #print(wk_data)
    return wk_data

#--------------------------------------------------------------
#유저(acc_id)별로 활동지수를 계산하는 함수
#사용할 변수 별로 sum 이나 mean function 중 골라서 사용할 것
#저는 귀찮아서 다 mean()해서 사용했습니다. 원래는 이럼 안됩니당.
def get_play_cnt_dt(data, columns) :
    week_cnt_data = data.groupby(["acc_id"], as_index=False)[columns].mean()#sum()으로 해도 됩니다.
    week_cnt_data = pd.DataFrame(week_cnt_data)

    return week_cnt_data

#--------------------------------------------------------------
#acc_id를 기반으로 두 데이터 프레임 합치기
#a 기반으로 b가 붙는거니 순서 유의해주세요.
def concat_data(a, b) :
    data = pd.merge(a, b, on="acc_id", how="left")

    return data


#--------------------------------------------------------------
#파일 저장하기
def save_file(data, filename) :
    data.to_csv(filename + ".csv", index=False)