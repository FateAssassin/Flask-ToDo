function OpenAddTodo() {
    var ToDo = document.getElementsByClassName("AddTodoForm")[0]; // Access the first element in the collection
 
    if (ToDo) {
       ToDo.style.display = "block"; // Show the element
    }
}

var errorElements = document.getElementsByClassName("errorMessage");

if (errorElements.length !== 0) {

    var inputArea = document.getElementsByClassName("TodoInput")[0];
    inputArea.style.border = "2px solid rgba(248, 17, 0, 0.7)";

}

function openEditMode(id) {
    var idElement = document.getElementsByClassName(id)[0];
    var editTodo = idElement.getElementsByClassName("editTodo");
    var TodoParagraph = idElement.getElementsByClassName("TodoParagraph")[0];
    var actionTodo = idElement.getElementsByClassName("actionTodo")[0];

    if (editTodo.length > 0) {
        editTodo[0].style.display = "inline";
        editTodo[1].style.display = "inline";
        TodoParagraph.style.display = "none";
        actionTodo.style.display = "none";
    }
}