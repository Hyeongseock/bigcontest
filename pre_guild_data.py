import pandas as pd

#---------------------------------------------------------------
#csv 파일을 dataframe 형태로 불러들임
#기본으로 불러올 경우 1행은 컬럼으로 지정됨
#파일 혹은 파일명을 포함하여 path를 입력하면 사용 가능
def read_file(filename) :
    data = pd.read_csv(filename + ".csv", encoding="cp949")
    return data



#---------------------------------------------------------------
#guild_member_acc_id를 ,로 나눈 후 각 acc_id를 하나의 로우로 만드는 함수
#기본으로 불러올 경우 1행은 컬럼으로 지정됨
#파일 혹은 파일명을 포함하여 path를 입력하면 사용 가능

def get_guild_member_cnt(data) :
    new_data = pd.DataFrame()
    new_data.append({"acc_id": "", "member_cnt": ""},ignore_index=True)
    for i in range(len(data)) :
        member = data.ix[i, "guild_member_acc_id"].split(",")
        temp_data = pd.DataFrame()
        temp_data.append({"acc_id":"","member_cnt":""},ignore_index=True)
        for j in range(0, len(member)) :
            #print(member[j], j)
            temp_data.loc[j,"acc_id"] = str(member[j])
        temp_data["member_cnt"] = len(data.ix[i, "guild_member_acc_id"].split(","))
        new_data = new_data.append([temp_data],ignore_index=True)
        #print(new_data)

    return new_data


# --------------------------------------------------------------
# 유저가 가입한 길드가 2개 이상인 경우 가입한 길드들의 평균 길드원 수 구하기
# get_guild_member_cnt를 먼저 수행한 후 가능
def get_guild_member_avg(data):
    new_data = data.groupby(["acc_id"], as_index=False)["member_cnt"].mean()
    new_data = pd.DataFrame(new_data)

    return new_data



#--------------------------------------------------------------
#유저별 가입한 길드 수 구하기
# get_guild_member_cnt를 먼저 수행한 후 가능
def get_join_guild_cnt(data) :
    data["guild_cnt"] = 1
    new_data = data.groupby(["acc_id"], as_index=False)["guild_cnt"].sum()
    new_data = pd.DataFrame(new_data)

    return new_data



#--------------------------------------------------------------
#acc_id를 기반으로 두 데이터 프레임 합치기
#a 기반으로 b가 붙는거니 순서 유의해주세요.
#여기서는 a가 label데이터 b가 길드데이터가 되어야 함
def concat_data(a,b) :
    data = pd.merge(a, b, on="acc_id", how="left")

    return data


#--------------------------------------------------------------
#test쪽에는 label_data가 없으므로, test_activity를 활용하여 acc_id를 얻음
#id 하나당 여러 행이 있으므로 중복되는 acc_id는 제거

def get_acc_id(label) :
    label = label[["acc_id"]]
    label = label.drop_duplicates().reset_index(drop=True)
    return label


#--------------------------------------------------------------
def save_file(data, filename) :
    filename = str(filename) + ".csv"
    data.to_csv(filename, index=False)