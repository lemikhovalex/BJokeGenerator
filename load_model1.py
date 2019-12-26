import os
import sys
sys.path.insert(1, '../')
import lib.j_generator as jg
import lib.constants as c
if not os.path.isdir("models"):
    os.mkdir("models")

jg.download_file_from_google_drive(c.W_ID, c.W_PATH)

model = jg.get_empty_model()
jg.load_weights_to_model(model, path=c.W_PATH)
model.save(c.NO_W_PATH)
