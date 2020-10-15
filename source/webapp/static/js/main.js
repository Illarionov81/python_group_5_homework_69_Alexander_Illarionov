
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
    }
    else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

window.addEventListener('load', function() {
    // const add = document.getElementById('add');
    // const subtract = document.getElementById('subtract');
    // const divide = document.getElementById('divide');
    // const multiply = document.getElementById('multiply');
    //
    // add.onclick = onLike;
    // subtract.onclick = onLike;
    // divide.onclick = onLike;
    // multiply.onclick = onLike;

});
async function Click(url) {
    const A = document.getElementById('a').value;
    const B = document.getElementById('b').value;
    const text = document.getElementById('output');
    try {
        let response = await makeRequest(url, 'POST', {"A": A, "B": B});
        text.innerText =  response['answer'];
        text.style.background = 'green';
    }
    catch (error) {
        error = await error.response;
        error= error.json();
        error = await error;
        text.innerText =  error['error'];
        text.style.background = 'red';
    }
}

 function onClick(event) {
    event.preventDefault();
    let aId = event.target.dataset['a'];
    let a = document.getElementById(aId);
    let url = a.href;
    console.log(url);
    Click(url);

}