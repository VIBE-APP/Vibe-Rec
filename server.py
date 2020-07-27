from flask import Flask, request
import recommender as rec

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("You've hit the VIBE recommender API")

# return a list of video ids

@app.route('/recommend')
def recommend():
    n = request.args.get('num_videos', '')
    user_id = request.args.get('user_id', '')
    return rec.recommender.get_n_recommendations(user_id, n)