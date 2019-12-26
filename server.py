from flask import Flask, request, render_template
import sys
from tensorflow.python.keras.backend import set_session
import tensorflow as tf
sys.path.insert(1, '../')
import lib.j_generator as jg
import lib.constants as c

sess = tf.Session()
graph = tf.get_default_graph()
set_session(sess)
model = tf.keras.models.load_model(
    c.NO_W_PATH,
    custom_objects=None,
    compile=True)


app = Flask(__name__)


@app.route("/")
def index(for_print=[], error=0):
    return render_template('index.html', for_print=for_print, error=error)


@app.route("/rnn", methods=['POST'])
def rnn():
    command = request.form['text1']
    command2 = request.form['text2']
    global graph

    # return request.form['text'] + " Command executed via subprocess"
    if command.isdigit():

        global sess
        global graph
        with graph.as_default():
            set_session(sess)
            for_print = jg.get_jokes(model, init_word=command2, jokes_num=int(command), joke_len=40)
        # keras.backend.clear_session()
        return index(for_print=for_print)
    else:
        return index(error=1)


if __name__ == "__main__":
    app.run(debug='True')
