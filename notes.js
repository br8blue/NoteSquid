document.getElementById("createNote").onclick = function() {
    document.getElementById("noteBox").style.display = "block";
};


document.getElementById("saveNote").onclick = function() {
    const title = document.getElementById("noteTitle").value;
    const content = document.getElementById("noteContent").value;

    fetch("http://127.0.0.1:5500/notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            user: "dummy",
            title: title,
            content: content
        })

        
    })

    .then(res => res.json())
    .then(data => {
        loadNotes()
        document.getElementById("noteBox").style.display = "none";
        document.getElementById("noteTitle").value = "";
        document.getElementById("noteContent").value = "";
    });

};






function loadNotes() {
    fetch("http://127.0.0.1:5500/notes?user=dummy")
        .then(res => res.json())
        .then(data => {
            const notes = data.notes;
            const grid = document.getElementById("notesGrid");

            grid.innerHTML = "";

            notes.forEach(note => {
                grid.innerHTML += `
                    <div>
                        <h4>${note.title}</h4>
                        <h5>${note.content}</h5>
                    
                    </div>

                `
            });
        });
     

}



window.onload = loadNotes;