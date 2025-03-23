function fetchTasks() {
    fetch("http://localhost:5000/api/tasks")
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById("task-list");
            taskList.innerHTML = "";
            data.forEach(task => {
                let li = document.createElement("li");
                li.textContent = task.title;
                taskList.appendChild(li);
            });
        });
}
