# twitter-mongodb
Thist project is to insert tweets into mongodb

## Getting Started
### Prerequisites
* Python 2.7+
* Tweepy
* Pymongo
* Textblob
* Twitter Developer Account: https://developer.twitter.com/

### Installing
```
pip install pymongo tweepy textblob
```
After install the prerequisites, you need to execute a code with arguments, the first argument is a word to search and the second argument is a quantity of results that the search returns
```
python twitter_mongodb.py Hadoop 50
```
In this example my code go search 50 results with the word Hadoop in twitter
