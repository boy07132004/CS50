document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('#form').onsubmit = ()=>{
        // init new request
        const request = new XMLHttpRequest();
        const username = document.querySelector('#username').value;
        request.open('POST','/search');
        request.onload = ()=>{
                const data = JSON.parse(request.responseText);
            if (data.success){
                const contents = `ID: ${data.id} Username:${username}.`
                document.querySelector('#result').innerHTML = contents ;
            }
            else {
                document.querySelector('#result').innerHTML = "Error" ;
            }
        }
        const data = new FormData();
        data.append('username',username);
        request.send(data);
        return false;}
});