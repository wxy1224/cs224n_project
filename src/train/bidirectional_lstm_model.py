
from src.train.abstract_model import BaseModel
from keras.models import Model
from keras.layers import Dense, Embedding, Input
from keras.layers import LSTM, Bidirectional, GlobalMaxPool1D, Dropout
from keras.preprocessing import text, sequence
from keras.callbacks import EarlyStopping, ModelCheckpoint
from src.config.static_config import StaticConfig
from keras import metrics
class Bidirectional_LSTM_Model(BaseModel):
    def __init__(self):
        # self._model = None
        self.global_config = StaticConfig()
        self.num_called = 0

    def get_model(self, lstm_length=50, dense_dim=30, drop_out = 0.1):
        # if not self._model is None:
        #     return self._model
        if self.num_called == 1:
            lstm_length = 35
        elif self.num_called == 2:
            lstm_length = 75
        elif self.num_called == 3:
            dense_dim = 50
        elif self.num_called == 4:
            dense_dim = 70
        elif self.num_called == 5:
            self.drop_out = 0.5
        self.num_called += 1

        embed_size = self.global_config.lstm_embed_size
        max_features = self.global_config.max_features
        maxlen = self.global_config.maxlen
        inp = Input(shape=(maxlen,))
        x = Embedding(max_features, embed_size)(inp)
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