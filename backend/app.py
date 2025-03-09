from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def search_word(word):
    conn = sqlite3.connect("backend/data/dictionary.db")
    cursor = conn.cursor()
    cursor.execute("SELECT meaning FROM words WHERE word = ?", (word,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

@app.route('/search', methods=['GET'])
def search():
    word = request.args.get("word")
    if not word:
        return jsonify({"error": "No word provided"}), 400

    meaning = search_word(word)
    if meaning:
        return jsonify({"word": word, "meaning": meaning})
    else:
        return jsonify({"error": "Word not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
