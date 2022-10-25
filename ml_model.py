from joblib import load
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

class Model:

    def __init__(self):
        self.features = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']
        self.pipeline = Pipeline(
            [
                ('feature_selection', ColumnTransformer(
                    [
                        ('selector', 'passthrough', self.features),
                        ('poly', PolynomialFeatures(degree = 2, include_bias = False), ['GRE Score', 'TOEFL Score', 'SOP', 'LOR ', 'CGPA'])
                    ]
                )),
                ('scaler', StandardScaler()),
                ('model', LinearRegression())
            ]
        )
        self.model = load("assets/modelo.joblib")

    def fit(self, data):
        data.dropna(subset=['Admission Points'], inplace=True)
        X_train, X_test, Y_train, Y_test = train_test_split(data, data["Admission Points"], test_size=0.2, random_state=1)
        error_dict = {
            "Mean_Absolute_Error_Train": mean_absolute_error(Y_train, self.pipeline.predict(X_train)),
            "Root_Mean_Squared_Error_Train": mean_squared_error(Y_train, self.pipeline.predict(X_train)),
            "Mean_Absolute_Error_Test": mean_absolute_error(Y_test, self.pipeline.predict(X_test)),
            "Root_Mean_Squared_Error_Test": mean_squared_error(Y_test, self.pipeline.predict(X_test)),
        }
        return error_dict

    def predict(self, data):
        result = self.model.predict(data)
        return result
