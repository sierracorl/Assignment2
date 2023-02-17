from flask import Flask, jsonify, request
import json, urllib
import re

app = Flask(__name__)
# Load the JSON file from the URL
with open("https://foyzulhassan.github.io/files/favs.json") as f:
    data_json = json.loads(f)

    
# Get all tweets
@app.route('/tweets', methods=['GET'])
def get_tweets():
    tweets = []
    for tweet in data_json:
        tweet_inf = {
            'created_at': tweet['created_at'],
            'id': tweet['id'],
            'text': tweet['text']
        }
        tweets.append(tweet_inf)
    return jsonify(tweets)


# Get a list of all external links grouped by tweet id
@app.route('/lines', methods=['GET'])
def get_link():
    link_id = {}
    for tweet in data_json:
        link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                          tweet['text'])
        link_id[tweet['id']] = link
    return jsonify(link_id)


# Get profile info about a Twitter user
@app.route('/users/<screen_name>', methods=['GET'])
def get_user(screen_name):
    for tweet in data_json:
        if tweet['user']['screen_name'] == screen_name:
            user_inf = {
                'name': tweet['user']['name'],
                'follow_count': tweet['user']['follow_count'],
                'friend_count': tweet['user']['friend_count'],
                'description': tweet['user']['description'],
                'fav_count': tweet['user']['fav_count']
            }
            return jsonify(user_inf)
    return jsonify({'error': 'User not found'})


# Get details about a tweet
@app.route('/tweets/<tweet_id>', methods=['GET'])
def get_tweet(tweet_id):
    for tweet in data_json:
        if tweet['id'] == int(tweet_id):
            tweet_inf = {
                'created': tweet['created'],
                'text': tweet['text'],
                's.name': tweet['user']['s.name'],
                'lang': tweet['lang']
            }
            return jsonify(tweet_inf)
    return jsonify({'error': 'Tweet not found'})


if __name__ == "__main__":
    app.run(debug=True)
