import os
import sys
sys.path.insert(1, '../')
import lib.j_generator as jg

if not os.path.isdir("models"):
    os.mkdir("models")
weight_path = 'models/model_1.hdf5'
weights_id = '1qb5gLroAlDfFg0Ujo5BZ1DZySkKPg_Ha'

jg.download_file_from_google_drive(weights_id, weight_path)

model = jg.get_empty_model()
jg.load_weights_to_model(model, path=weight_path)
model.save('models/no_w_model_1.h5')
