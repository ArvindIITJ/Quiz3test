import numpy as np
from sklearn.model_selection import train_test_split
X, y = np.arange(10).reshape((5, 2)), range(5)
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)
X_trains, X_tests, y_trains, y_tests = train_test_split( X, y, test_size=0.33, random_state=42)
X_trainss, X_testss, y_trainss, y_testss = train_test_split( X, y, test_size=0.33, random_state=43)
def test_sames():
    for i in range(0,2):
        for j in range (0,2):
            assert X_test[i][j] == X_tests[i][j]
            assert X_train[i][j] == X_trains[i][j]

        return "true"
print(test_sames())

def test_diffs():
    for i in range(0,2):
        for j in range (0,2):
            assert X_test[i][j] != X_testss[i][j]
            assert X_train[i][j] != X_trainss[i][j]
            
        return "false"
    
print(test_diffs())

