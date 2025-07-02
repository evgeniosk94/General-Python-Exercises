import numpy as np
from sklearn.naive_bayes import BernoulliNB

def NaiveBayes_dummy():
    X_train = np.array([
        [0,1,1],
        [0,0,1],
        [0,0,0],
        [1,1,0]
    ])

    Y_train = ['Y','N','Y','Y']
    X_test = np.array([[1,1,0]])
    
    clf = BernoulliNB(alpha=1, fit_prior=True) # alpha is the smoothing parameter, fit_prior is whether to learn class prior probabilities from the data
    clf.fit(X_train, Y_train)
    pred_prob = clf.predict_proba(X_test)
    print('[scikit-learn] Predicted probabilities:\n', pred_prob)
    
    pred = clf.predict(X_test)
    print('[scikit-learn] Prediction:\n', pred)

if __name__ == '__main__':
    NaiveBayes_dummy()