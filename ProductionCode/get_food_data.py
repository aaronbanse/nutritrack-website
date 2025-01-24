import pandas as pd

def get_df():
    df = pd.read_csv("Data/food_nutrition_sample.csv")
    return df

def fetch_category(category):
    df = get_df()
    return df[df["Category"]==category]["Description"]

def health_facts(description):
    df = get_df()
    return df[df["Description"] == description].drop(columns=["Category","Description","Nutrient Data Bank Number"])