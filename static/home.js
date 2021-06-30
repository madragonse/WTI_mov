function loadText(text='testo') {
    var requestData = new XMLHttpRequest();
    requestData.responseType = "document";
    requestData.addEventListener("load", function () {
        if (requestData.status == 200) {
            location.reload();
        }
        else {
            
        }
    }, {once : true});
    requestData.open("post", window.location.href);
    requestData.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    requestData.send(JSON.stringify({ "text": text}));

}