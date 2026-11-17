from sklearn import tree
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from fetch import get_cars


data = get_cars()

x = [list(row[:-1]) for row in data]

y = [row[-1] for row in data]



# ستون‌های متنی
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OrdinalEncoder(handle_unknown='use_encoded_value',
                               unknown_value=-1), [0, 1])
    ],
    remainder='passthrough'
)

# ساخت مدل
clf = Pipeline([
    ('preprocessor', preprocessor),
    ('model', tree.DecisionTreeRegressor())
])

clf.fit(x, y)
new_data = [
    ['لکسوس، LX', '700h', 2023, 0],
    ['پژو، 207', 'اتوماتیک TU5P', 1401, 45000]
]
answer = clf.predict(new_data)

print(answer)