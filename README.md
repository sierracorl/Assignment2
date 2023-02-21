** I used Visual Studio Code and installed these extensions:
~ Flask Framework (Flask Snippets) 
~ flask-vgs
~ Python (IntelliSense)
~ Python Extension Pack
~ Python Indent
~ Json (json for Visual Studio Code)
~ Azure API Management
~ REST API

NOTE:
This implementation works on Pycharm/Postman as well 

---My implementation uses Flask framework which creates REST APIs that reads and manipulates JSON. 

Instructions: 
1. Download and extract file
2. Install Visual Studio Code or Pycharm/Postman
3. Install Extensions I have listed above if you are using Visual Studio Code
4. Open Json.py file in Visual Studio Code or Pycharm
4. Use Postman or any other HTTP client to send requests to the endpoint 
5. Example: Run script as  http://127.0.0.1:5000/tweets

------------------------------------------------------------------------------------------------

What each function does: 
1. users - returns profile info in detail of the user with screen name w/their name, followers count, favroties count, friends count, and description 
2. tweets - returns a list of all tweets in the JSON file with ID, create time, and tweet text
3. tweet_id - returns details of the tweet with text, ID, language, screen name, and create time. 
4. links - returns a list of all external links grouped by ID. The immplementation extracts the links from the tweet text 
