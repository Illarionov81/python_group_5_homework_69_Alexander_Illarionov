
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};
    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
        console.log(opts.body);
    }
    let response = await fetch(url, opts);
    if (response.ok) {  // нормальный ответ
        return response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function onLike(event) {
    const A = document.getElementById('a').value;
    const B = document.getElementById('b').value;
    console.log(A, B);
    const text = document.getElementById('output');
    event.preventDefault();
    let action = event.target;
    console.log(action)
    let url = action.href;
    console.log(url);

    try {
        let response = await makeRequest(url, 'POST', {"A": A, "B": B});
        console.log(response);
        text.innerText =  response['answer'];
    }
    catch (error) {
        console.log(error);
    }
}

window.addEventListener('load', function() {
    const add = document.getElementById('add');
    const subtract = document.getElementById('subtract');
    const divide = document.getElementById('divide');
    const multiply = document.getElementById('multiply');

    add.onclick = onLike;
    subtract.onclick = onLike;
    divide.onclick = onLike;
    multiply.onclick = onLike;

});