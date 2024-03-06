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


