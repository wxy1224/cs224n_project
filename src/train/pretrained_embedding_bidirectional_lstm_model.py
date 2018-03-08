
from src.train.abstract_model import BaseModel
from keras.models import Model
from keras.layers import Dense, Embedding, Input
from keras.layers import LSTM, Bidirectional, GlobalMaxPool1D, Dropout
from keras.preprocessing import text, sequence
from keras.callbacks import EarlyStopping, ModelCheckpoint
from src.config.static_config import StaticConfig
from src.config.dynamic_config import DynamicConfig
from keras import metrics
from numpy import zeros

from numpy import asarray
class Bidirectional_LSTM_Model(BaseModel):
    def __init__(self):
        # self._model = None
        self.global_config = StaticConfig()
        self.dynamic_config = DynamicConfig()
        # self.num_called = 0
    def embedding_index(self):
        self.embeddings_index = dict()
        f = open('./input/glove.6B.100d.txt')
        for line in f:
            values = line.split()
            word = values[0]
            coefs = asarray(values[1:], dtype='float32')
            self.embeddings_index[word] = coefs
        f.close()

        # print('Loaded %s word vectors.' % len(embeddings_index))

    def get_model(self, count, lstm_length=50, dense_dim=30, drop_out = 0.1, preprocessor=None):
        # if not self._model is None:
        #     return self._model
        # if self.num_called == 1:
        #     lstm_length = 35
        # elif self.num_called == 2:
        #     lstm_length = 75
        # elif self.num_called == 3:
        #     dense_dim = 50
        # elif self.num_called == 4:
        #     dense_dim = 70
        # elif self.num_called == 5:
        #     self.drop_out = 0.5
        # self.num_called += 1
        self.embedding_index()
        tokenizer = preprocessor.tokenizer
        voc_size = len(tokenizer.word_index) + 1

        lstm_length = self.dynamic_config.config[count]['lstm_length']
        dense_dim = self.dynamic_config.config[count]['dense_dim']
        drop_out = self.dynamic_config.config[count]['drop_out']
        embed_size = self.global_config.lstm_embed_size
        max_features = self.global_config.max_features
        maxlen = self.global_config.maxlen

        embedding_matrix = zeros((voc_size, 100))
        for word, i in t.word_index.items():
            embedding_vector = self.embeddings_index.get(word)
            if embedding_vector is not None:
                embedding_matrix[i] = embedding_vector

        inp = Input(shape=(maxlen,))
        x = Embedding(max_features, embed_size, weights=[embedding_matrix])(inp)
        x = Bidirectional(LSTM(lstm_length, return_sequences=True))(x)
        x = GlobalMaxPool1D()(x)
        x = Dropout(drop_out)(x)
        x = Dense(dense_dim, activation="relu")(x)
        x = Dropout(drop_out)(x)
        x = Dense(6, activation="sigmoid")(x)
        model = Model(inputs=inp, outputs=x)
        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=[metrics.categorical_accuracy])
        # print(model.summary())
        # self._model = model
        return model