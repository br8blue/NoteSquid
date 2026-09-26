from flask import Flask, request, jsonify
from notes import createNote as createNoteFunc
from notes import getNotes as getNotesFunc, deleteNote as deleteNoteFunc, updateNote as updateNoteFunc




app = Flask(__name__)

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    createNoteFunc(
        data['title'],
        data['content']
        data['user']
    )
    return jsonify({'message': 'Note created successfully'}), ({"status": "success"}), 201


@app.route('/notes', methods=['GET'])
def get_notes():
    user = request.args.get('user')
    notes = getNotesFunc()
    return jsonify({'notes': notes}), 200

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    deleteNoteFunc(note_id)
    return jsonify({'message': 'Note deleted successfully'}), ({"status": "deleted, success"}), 200



if __name__ == '__main__':  
    app.run(debug=True)