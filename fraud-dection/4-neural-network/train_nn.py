import argparse
import numpy as np
import os
import tensorflow as tf
from tensorflow.contrib.eager.python import tfe
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score,accuracy_score

tf.logging.set_verbosity(tf.logging.ERROR)

max_features = 20000
maxlen = 400
embedding_dims = 300
filters = 250
kernel_size = 3
hidden_dims = 250


def parse_args():

    parser = argparse.ArgumentParser()

    # hyperparameters sent by the client are passed as command-line arguments to the script
    parser.add_argument('--epochs', type=int, default=1)
    parser.add_argument('--batch_size', type=int, default=64)

    # data directories
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAINING'))
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_VALIDATION'))

    # model directory: we will use the default set by SageMaker, /opt/ml/model
    parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR'))

    return parser.parse_known_args()


def get_train_data(train_dir):
    
    #print('train_dir = ',train_dir)
    
    train = pd.read_csv(os.path.join(train_dir,'train.csv'), delimiter=',')
    #print(train.head(10))

    x_train = train.iloc[:, 0:28]
    y_train = train.iloc[:,28:29]
    
    #print('x train', x_train.shape,'y train', y_train.shape)
    

    return x_train, y_train


def get_test_data(test_dir):
    
    test = pd.read_csv(os.path.join(test_dir,'validation.csv'), delimiter=',')
    #print(test.head(10))

    x_test = test.iloc[:,0:28]
    y_test = test.iloc[:,28:29]
    #print('x test', x_test.shape,'y test', y_test.shape)

    return x_test, y_test


def get_model():
    
    model = tf.keras.models.Sequential([
      tf.keras.layers.Dense(28, input_dim=28, activation='relu'),
      tf.keras.layers.Dense(8, activation='relu'),
      tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    print(model.summary)
    
    model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
    

    return model


if __name__ == "__main__":

    args, _ = parse_args()
    
    print(args)

    x_train, y_train = get_train_data(args.train)
    x_test, y_test = get_test_data(args.test)

    model = get_model()
    
    model.summary()
    
    model.fit(
            x_train, 
            y_train, 
            epochs=args.epochs,
            batch_size=args.batch_size,
            validation_data=(x_test, y_test)
            )

    # create a TensorFlow SavedModel for deployment to a SageMaker endpoint with TensorFlow Serving
    
    tf.contrib.saved_model.save_keras_model(model, args.model_dir)