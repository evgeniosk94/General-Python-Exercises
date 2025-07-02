from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer()
X = cancer_data.data
Y = cancer_data.target
print('Input data size:', X.shape)
print('Output data size:', Y.shape)
print('Label names:', cancer_data.target_names)
n_pos = (Y==1).sum()
n_neg = (Y==0).sum()
print(f'{n_pos} positive samples and {n_neg} negative samples')

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)

from sklearn.svm import SVC
clf = SVC(kernel='linear', C=1.0, random_state=42)
clf.fit(X_train, Y_train)

accuracy = clf.score(X_test, Y_test)
print(f'The accuracy of the model is {accuracy*100:.2f}%')