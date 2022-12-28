# Import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


model: KNeighborsClassifier
def knn(file, label_column, test_percentage, neighbors, distance_power):
    X = file.drop(columns=[label_column])
    y = file[label_column]
    test_ratio = test_percentage / 100

    train_features, test_features, train_labels, test_answers = train_test_split(X, y, test_size=test_ratio)
    model = KNeighborsClassifier(n_neighbors=neighbors, p=distance_power)

    model.fit(train_features, train_labels)

    predictions = model.predict(test_features)

    accuracy = accuracy_score(test_answers, predictions)
    precision = precision_score(test_answers, predictions, average='weighted')
    recall = recall_score(test_answers, predictions, average='weighted')

    return accuracy, precision, recall
