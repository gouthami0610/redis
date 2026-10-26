from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (Docker container)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route("/")
def home():
    r.incr("visits")
    count = r.get("visits")
    return f"Hello Gouthami! This page was visited {count} times."

if __name__ == "__main__":
    app.run(debug=True)