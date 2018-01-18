import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" # see issue #152
os.environ['CUDA_VISIBLE_DEVICES'] = '-1' # -1 !!!!


dataset = pandas.read_csv('combined_fastnmean.csv')
X = dataset.iloc[:, 0:9].values
y = dataset.iloc[:, 10].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y)
dummy_y = np_utils.to_categorical(encoded_Y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, dummy_y, test_size = 0.1, random_state = 0)

#preprocessing
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = Sequential()

classifier.add(Dense(units = 18, kernel_initializer = 'uniform', activation = 'relu', input_dim = 9))
classifier.add(Dense(units = 18, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'softmax'))
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

classifier.fit(X_train, y_train, batch_size = 50, epochs = 3000)

y_pred = classifier.predict(X_train)
#y_pred = (y_pred > 0.5)


test_dataset = pandas.read_csv('final_test_withoutimagename.csv')
X_testimagenp = sc.transform(test_dataset)
new_pred = classifier.predict(X_testimagenp)
b = numpy.zeros_like(new_pred)
b[numpy.arange(len(new_pred)), new_pred.argmax(1)] = 1


#pandas.DataFrame([x for x in numpy.where(cameraname ==1, cameraname.columns,'').flatten().tolist() if len(x) >0],columns= (["cameraname"]) )

#predicts = classifier.predict(sc.transform(X_testimage))
#predicts = numpy.argmax(predicts, axis=1)
#pred1=classifier.predict(sc.transform(numpy.array([[111.37601090000001,125.1912682,0.257425032,91.24418259,121.60658590000001,0.595537069,106.4606247,123.5783165,0.34289348299999994]])))


my_df = pandas.DataFrame(b)
my_df.to_csv('onehot.csv', index=False, header=False)

cols = ['a', 'b', 'c','d','e','f','g','h','i','j','k']
names =  ['Sony-NEX-7','Samsung-Galaxy-S4','Samsung-Galaxy-Note3','HTC-1-M7','iPhone-4s','iPhone-6','LG-Nexus-5x','Motorola-Droid-Maxx','Motorola-Nexus-6','Motorola-X']
df = pandas.read_csv('onehot.csv', names = cols)
count = 0
for i in range(0,10):
    count +=1
    print(count)
    c = cols[i]
    a = df[c]
    indexes = [i for i,x in enumerate(a) if x == 1]
    for j in indexes:
        df['k'][j] = names[i]

df = pandas.DataFrame(b)
df.to_csv('submission.csv', index=False, header=False)
