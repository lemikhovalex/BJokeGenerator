from flask import Flask, request, render_template
import subprocess
import time
import sys
sys.path.insert(1, '../')
import lib.j_generator as jg

model = jg.get_empty_model()
jg.load_weights_to_model(model, path='models/model_1.hdf5')





app = Flask(__name__)

@app.route("/")
def index(for_print = [], error = 0):
    return render_template('index.html',for_print = for_print,error = error)





@app.route("/rnn", methods=['POST'])
def rnn():
    command = request.form['text1']
    command2 = request.form['text2']

    # return request.form['text'] + " Command executed via subprocess"
    if command.isdigit():
        for_print = jg.get_jokes(model, init_word=command2, jokes_num=int(command), joke_len=20)
        return index(for_print = for_print)
    else:

        return index(error = 1)





if __name__ == "__main__":
    app.run(debug='True')
