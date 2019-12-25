import time
import sys
sys.path.insert(1, '../')
import lib.j_generator as jg

start_time = time.time()
model = jg.get_empty_model()
jg.load_weights_to_model(model, path='models/model_w.hdf5')
jokes = jg.get_jokes(model, init_word='шляпа ', jokes_num=1, joke_len=20)
print(jokes)

end_time = time.time()
print(end_time - start_time)
