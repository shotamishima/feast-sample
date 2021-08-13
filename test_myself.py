from datetime import datetime, timedelta

import pandas as pd

from feast import FeatureStore



def retrieve_from_offline():
    entity_df = pd.DataFrame(
        {
            "event_timestamp": [pd.Timestamp(dt, unit="ms", tz="UTC").round("ms") 
            # 過去３日間のデータをエンティティにする
            for dt in pd.date_range(
                start=datetime.now() - timedelta(days=1),
                end=datetime.now(),
                periods=3,
                )
            ],
            "driver_id": [1001, 1002, 1003]
        }
    )

    print('Retrieving training data...')
    print("-----------------------------")


    training_df = fs.get_historical_features(
        features=["driver_hourly_stats:conv_rate", "driver_hourly_stats:acc_rate"],
        entity_df=entity_df
    ).to_df()

    print(training_df.head(10))
    print("-----------------------------")

    return training_df

def load_online():
    print("Loading features into the online store...")
    print("-----------------------------")

    fs.materialize_incremental(end_date=datetime.now())
    # materialize_incrementalはend_dataのみ指定し、未更新分からend_dateまでのOfflineデータをonlineにコピーする
    # materializeは最初と最後のタイムスタンプを指定する

    print("Loading features into the online store has done")
    print("-----------------------------")

def retrieve_from_online():
    print("Retrieving online features...")
    print("-----------------------------")
    online_features = fs.get_online_features(
        features=["driver_hourly_stats:event_timestamp", "driver_hourly_stats:conv_rate", "driver_hourly_stats:acc_rate"],
        entity_rows=[{"driver_id": 1001}, {"driver_id": 1002}]
    ).to_dict()

    print(pd.DataFrame.from_dict(online_features))
    print("-----------------------------")



if __name__ == "__main__":
    fs = FeatureStore(repo_path=".") # data/registoryの場所
    training_df = retrieve_from_offline()
    load_online()
    retrieve_from_online()
    


