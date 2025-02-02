import pandas as pd

"""returns formatted error message"""
def error(message):
    return f"Error: {message}"

"""returns csv file in the form of a dataframe"""
def get_data(dummy: bool = False):
    if type(dummy) != bool:
        raise(TypeError)
    # set dataset name based on if dummy data requested
    dataset_name = f"food_nutrition{'_sample' if dummy else ''}.csv"
    data = pd.read_csv(f"Data/{dataset_name}")
    return data

"""fetches appropriate columns via categories as strings"""
def fetch_category(category: str):
    if type(category) != str:
        raise(TypeError)
    data = get_data(dummy=True)
    return data[data["Category"]==category]["Description"]

"""fetches appropriate columns via categories as strings"""
def health_facts(description: str):
    if type(description) != str:
        raise(TypeError)
    data = get_data(dummy=True)
    return data[data["Description"] == description].drop(columns=["Category","Description","Nutrient Data Bank Number"])