# Import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix



def naive_bayes(file, label_column, test_percentage, neighbors, distance_power):
    X = file.drop(columns=[label_column])
    y = file[label_column]
    test_ratio = test_percentage / 100

    train_features, test_features, train_labels, test_answers = train_test_split(X, y, test_size=test_ratio)
    knn = KNeighborsClassifier(n_neighbors=neighbors, p=distance_power)
    knn.fit(train_features, train_labels)

    predictions = knn.predict(test_features)

    accuracy = accuracy_score(test_answers, predictions)
    precision = precision_score(test_answers, predictions, average='weighted')
    recall = recall_score(test_answers, predictions, average='weighted')
    f1 = f1_score(test_answers, predictions, average='weighted')
    confusion = confusion_matrix(test_answers, predictions)

    print(f'Accuracy: {accuracy:.2f}')
    print(f'precision: {precision:.2f}')
    print(f'recall: {recall:.2f}')
    print(f'f1: {f1:.2f}')
    print(confusion)

    return accuracy, precision, recall, f1