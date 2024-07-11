from flask import Flask, request, jsonify

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

app = Flask(__name__)

def binary_search(alist, inittarget):
    alist.sort()
    target = inittarget.lower()
    low = 0
    high = len(alist) - 1

    while low <= high:
        mid = (low + high) // 2
        if alist[mid].lower() == target:
            return f'Found target "{inittarget}" at index {mid} in the provided list.'
        elif alist[mid].lower() < target:
            low = mid + 1
        else:
            high = mid - 1
    return 'Target not found'

@app.route('/search_name', methods=['GET'])
def search_name():
    name = request.args.get('name')
    if name:
        result = binary_search(video_titles, name)
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Name parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
