import pandas as pd
import numpy as np
import matplotlib as plt

## label,activity,payment를 합하여 하나의 데이터를 만듭니다.
activity_df=pd.read_csv('E:/NCsoft/champion_data/train/train_activity.csv')

## activity_df에서 아이디별 평균을 구하여 다시 저장합니다. acc_id는 고유값이기 때문에 다른 df들과 결합을 위해 반드시 정렬을 해줍니다.
## (열 개수가 10000개 임을 확인할 수 있습니다.)
activity_df=activity_df.sort_values(by='acc_id')

activity_df["count"] = 1
print(activity_df.shape)
activity_df.head()
activity_df1=activity_df.groupby('acc_id').sum() #컬럼 추가하여 합계

print(activity_df1.shape)
activity_df1.head()

activity_df1["play_time_sum"]=1
print(activity_df1.shape)
activity_df1.head()

activity_df1["play_time_sum"]= activity_df1["wk"].sum() * activity_df1["cnt_dt"].mean()
print(activity_df1.shape)
activity_df1.head()

activity_df2=activity_df1.groupby('acc_id').mean()

print(activity_df2.shape)
activity_df2.head()

## activity_df와 label을 합쳐야하기 때문에 중복되는 acc_id 열을 제거하기 위해 인덱스를 초기화하고 acc_id를 drop 시킵니다.
activity_df2=activity_df2.reset_index().drop(columns=['acc_id'])
activity_df2.head()

## label_df 를 불러와 acc_id로 정렬합니다.
label_df=pd.read_csv('E:/NCsoft/champion_data/train/train_label.csv')
label_df=label_df.sort_values(by='acc_id')
label_df.head()


## activity와 label을 합쳐 df_one을 만듭니다.
df_one=pd.concat([label_df, activity_df2],axis=1)
df_one.shape
df_one.head()


## 다음 payment를 df_one과 합치기 위해 불러와 마찬가지로 정렬, acc_id로 그룹별 평균을 구한 뒤 같은 방법으로 index 초기화, acc_id를 제거합니다
payment_df=pd.read_csv('E:/NCsoft/champion_data/train/train_payment.csv')
payment_df=payment_df.sort_values(by='acc_id')
print(payment_df.shape)
payment_df.head()

payment_df["count"] = 1
print(payment_df.shape)
payment_df.head()

payment_df1=payment_df.groupby('acc_id').sum()
print(payment_df1.shape)
payment_df1.head()

payment_df1["payment_amount_sum"]=payment_df1["payment_week"]* payment_df1["payment_amount"]
print(payment_df1.shape)
payment_df1.head()

payment_df2=payment_df1.groupby('acc_id').mean()

print(payment_df2.shape)
payment_df2.head()

payment_df2=payment_df2.reset_index().drop(columns=['acc_id'])

df_one=pd.concat([df_one, payment_df2],axis=1)

## df_one의 열을 확인합니다.
df_one.columns
print(df_one.shape)
df_one.head()

## df_one을 csv파일로 저장합니다.
df_one.to_csv('df_one.csv')
df_one