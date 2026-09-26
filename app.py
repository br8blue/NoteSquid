from flask import Flask, request, jsonify
from notes import createNote, getNotes, deleteNote, updateNote

app = Flask(__name__)

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    note_id = createNote(data['title'], data['content'])
    return jsonify({'id': note_id}), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = getNotes()
    return jsonify(notes)

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    deleteNote(note_id)
    return '', 204

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    updateNote(note_id, data['title'], data['content'])
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)