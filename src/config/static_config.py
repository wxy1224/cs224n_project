

class StaticConfig:
    labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    model_names = ["{}".format(i) for i in range(18)]
    max_features = 50000
    maxlen = 100
    patience = 20
    validation_split = 0.1
    model_save_name = "weights_base.best.hdf5"
    ensemble_model_save_name = "weights_ensemble.best.hdf5"
    tokenizer_save_name = "tokenizer_save.p"
    original_label_file_name = "original_label_save.csv"
    predict_save_name = "predict_save.csv"
    average_predict_save_name = "average_predict_save.csv"
    ensembled_predict_file_name = "ensembled_predict_file.csv"
    ensembled_submission_file_name = "submission_predict_file.csv"
    is_debug = True
    auc_file_name = "auc.json"
    lstm_embed_size = 35
    data_balancing_sampling_attempt = 5
    enable_rebalancing_sampling = False

    batch_size = 32
    epoches = 2


