import pandas as pd

def get_df():
    """returns csv file in the form of a dataframe"""
    df = pd.read_csv("Data/food_nutrition_sample.csv")
    return df

def fetch_category(category):
    """fetches appropriate columns via categories as strings"""
    df = get_df()
    return df[df["Category"]==category]["Description"]

def health_facts(description):
    """fetches appropriate columns via categories as strings"""
    df = get_df()
    return df[df["Description"] == description].drop(columns=["Category","Description","Nutrient Data Bank Number"])