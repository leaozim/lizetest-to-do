const checkboxes = document.querySelectorAll('.checkbox-class');
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        handleCheckboxChange(checkbox);
    });
});

async function handleCheckboxChange(checkbox) {
    const taskId = checkbox.getAttribute("data-task-id");
    try {
        const response = await fetch(`http://localhost:8000/api/tasks/${taskId}/`, {
            method: 'PUT',
            mode: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body: JSON.stringify({ completed: checkbox.checked }),
        });
    } catch (error) {
        console.error("Error:", error);
    }
}

function getCookie(name) {
    const cookies = document.cookie.split(';').map(cookie => cookie.trim());
    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) {
            return cookieValue;
        }
    }
    return null;
}

$(document).ready(function () {
    const detailsModal = $("#detailsModal");
    $(".details-btn").on("click", function () {
        const taskTitle = this.getAttribute("data-task-title");
        const taskDescription = this.getAttribute("data-task-desc");
        const taskCategory = this.getAttribute("data-task-category");

        detailsModal.find("#modal-task-title").text(taskTitle);
        detailsModal.find("#modal-task-description").text(taskDescription);
        const modalTaskCategory = detailsModal.find("#modal-task-category");

        if (taskCategory !==  "None"){
            detailsModal.find("#modal-task-category").text(taskCategory);
            modalTaskCategory.closest("p").show(); 
        } else {
            modalTaskCategory.closest("p").hide();
        }
        detailsModal.modal("show");
    });
});

let taskId;
$(document).ready(function () {
    $(".edit-btn").on("click", function () {
        taskId = $(this).data("task-id");
        console.log(taskId)
        editUrl =  "task/" + taskId + "/edit/"
        $.get(editUrl, function (data) {
            console.log("Data received:", data);
            console.log("Edit URL:", editUrl);
            $("#editTaskFormContainer").html(data);
            $("#editTaskModal").modal("show");
        });
    });
    $(document).on("submit", ".edit-task-form", function (e) {
        e.preventDefault();
        console.log(taskId);
        $(this).attr("action", "task/" + taskId + "/edit/");
        this.submit();
    });
    $.post(url, form.serialize(), function (data) {
        // Se houver erros, recarregue o modal com os erros
        if (data.includes("class=\"alert alert-danger\"")) {
            $("#editTaskFormContainer").html(data);
            $("#editTaskModal").modal("show");
        } else {
            // Se não houver erros, pode redirecionar para a página de sucesso
            window.location.reload();
        }
    });

});


