from sklearn.metrics import mean_absolute_error
# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split

# fill in and uncomment
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
