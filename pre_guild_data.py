import pandas as pd


def read_file(filename) :
    data = pd.read_csv(filename + ".csv", encoding="cp949")
    return data



def pre_guild_data(data) :
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

def save_data(data, filename) :
    filename = str(filename) + ".csv"
    data.to_csv(filename, index=False)

def main() :
    guild = read_file("test_guild")
    data = pre_guild_data(guild)
    save_data(data, "pre_test_guild_data")

if __name__ =="__main__":
    main()