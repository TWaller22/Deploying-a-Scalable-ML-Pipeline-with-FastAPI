import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference,
from sklearn.model_selection import train_test_split


# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test if the model returens RandomForestClassifer
    """
    X_train = np.random.rand(20,5)
    y_train = np.random.randint(2, size 20)
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test to verify the data set has the expected number of columns 
    """
    df = pd.read_csv("data/census.csv")
    expected_column_count = 15
    assert len(df.columns) == expected_column_count, f"Expected {expected_column_count} columns, retrieved {len(df.columns)}"
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test if the nodel inference function 
    """
    X_train = np.random.rand(20,5)
    y_train = np.random.randint(2, size 20)
    model = train_model(X_train, y_train)
    y_preds = inference(model, X_train)
    assert y.shape == y_preds.shape
    pass
