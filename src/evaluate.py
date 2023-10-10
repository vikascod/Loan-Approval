import sys
from src.exception import CustomException

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

def evaluate_models(models, params, X_train, y_train, X_test, y_test):
    """
    Evaluate a set of machine learning models using grid search and report their performance metrics.

    Parameters:
        models (dict): A dictionary of machine learning models to be evaluated.
        params (dict): A dictionary of hyperparameter grids for each model.
        X_train (array-like): Training feature matrix.
        y_train (array-like): Training target vector.
        X_test (array-like): Testing feature matrix.
        y_test (array-like): Testing target vector.

    Returns:
        report (dict): A dictionary containing the model names as keys and their test accuracy scores as values.

    Raises:
        CustomException: If an error occurs during the evaluation process.

    Example:
        models = {
            "Random Forest": RandomForestClassifier(),
            "Decision Tree": DecisionTreeClassifier(),
            "Gradient Boosting": GradientBoostingClassifier(),
            "Logistic Regression": LogisticRegression(),
            "XGBClassifier": XGBClassifier(),
            "CatBoostClassifier": CatBoostClassifier(verbose=False),
            "AdaBoost Classifier": AdaBoostClassifier(),
        }
        params = {
            "Random Forest": {
                'n_estimators': [8, 16, 32, 64, 128, 256],
                'criterion': ['gini', 'entropy'],
                'max_depth': [None, 5, 10, 15],
            },
            "Decision Tree": {
                'criterion': ['gini', 'entropy'],
                'splitter': ['best', 'random'],
                'max_depth': [None, 5, 10, 15],
            },
            "Gradient Boosting": {
                'learning_rate': [0.1, 0.01, 0.05, 0.001],
                'n_estimators': [8, 16, 32, 64, 128, 256],
                'max_depth': [3, 5, 7, 9],
            },
            "Logistic Regression": {},
            "XGBClassifier": {
                'learning_rate': [0.1, 0.01, 0.05, 0.001],
                'n_estimators': [8, 16, 32, 64, 128, 256],
                'max_depth': [3, 5, 7, 9],
            },
            "CatBoostClassifier": {
                'depth': [6, 8, 10],
                'learning_rate': [0.01, 0.05, 0.1],
                'iterations': [30, 50, 100],
            },
            "AdaBoost Classifier": {
                'learning_rate': [0.1, 0.01, 0.5, 0.001],
                'n_estimators': [8, 16, 32, 64, 128, 256],
            }
        }
        report = evaluate_models(models, params, X_train, y_train, X_test, y_test)
    """
    try:
        report = {}
        for model_name, model in models.items():
            # Define the hyperparameter grid for the current model.
            param_grid = params.get(model_name, {})
            
            # Create a GridSearchCV object for hyperparameter tuning.
            gs = GridSearchCV(model, param_grid, cv=3)
            
            # Fit the model to the training data with grid search.
            gs.fit(X_train, y_train)
            
            # Set the best hyperparameters found by grid search.
            model.set_params(**gs.best_params_)
            
            # Fit the model again with the best hyperparameters.
            model.fit(X_train, y_train)
            
            # Make predictions on the training and testing data.
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            # Calculate and print accuracy scores.
            y_train_score = accuracy_score(y_train, y_train_pred)
            y_test_score = accuracy_score(y_test, y_test_pred)
            print(f"Train score for {model_name}: {y_train_score}")
            print(f"Test score for {model_name}: {y_test_score}")
            
            # Store the test accuracy score in the report dictionary.
            report[model_name] = y_test_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
