from flask import Flask, jsonify, request
import json
import re

app = Flask(__name__)

# Define URL for Twitter favorites JSON file
json_url = "https://foyzulhassan.github.io/files/favs.json"

# Read and parse JSON file from URL
data_json = request.get(json_url).json()
 
# Get tweets w/ time, ID & text
@app.route('/tweets', methods=['GET'])
def get_tweets():
    tweets = []
    for item in data_json:
        tweet = {}
        tweet['timeCreated'] = item['createdAt']
        tweet['id'] = item['id_str']
        tweet['text'] = item['txt']
        tweets.append(tweet)
    return jsonify(tweets)

# Get external links by tweet ID
@app.route('/link', methods=['GET'])
def get_link():
    link = {}
    for item in data_json:
        tweetLink = []
        matches = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', item['full_text'])
        for match in matches:
            tweetLink.append(match)
        link[item['id_str']] = tweetLink
    return jsonify(link)

# Get details of a tweet with ID
@app.route('/tweets/<tweet_id>', methods=['GET'])
def get_tweet(tweet_id):
    for item in data_json:
        if item['id_str'] == tweet_id:
            tweet = {}
            tweet['timeCreated'] = item['createdAt']
            tweet['text'] = item['txt']
            tweet['screenName'] = item['user']['screenName']
            tweet['lang'] = item['lang']
            return jsonify(tweet)
    return "Tweet not found"

# Get profile info from a user 
@app.route('/users/<screenName>', methods=['GET'])
def get_user(screenName):
    for screenName in data_json:
            user = {}
            user['name'] = screenName['name']
            user['description'] = screenName['description']
            user['follower_count'] = screenName['follower_count']
            user['friend_count'] = screenName['friend_count']
            user['favorite_count'] = screenName['favorite_count']
            return jsonify(user)
    else:
            return "User not found"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)