import os
import sys
sys.path.insert(1, '../')
from lib.j_generator import download_file_from_google_drive as lo

if not os.path.isdir("models"):
    os.mkdir("models")
weight_path = 'models/model_1.hdf5'
weights_id = '1qb5gLroAlDfFg0Ujo5BZ1DZySkKPg_Ha'
lo(weights_id, weight_path)
