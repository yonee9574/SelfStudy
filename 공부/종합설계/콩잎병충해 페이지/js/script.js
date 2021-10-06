// ----------------------------------파일 업로드------------------------------------//
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('.image-upload-wrap').hide();
            $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();
            $('.image-title').html(input.files[0].name);
        };
        reader.readAsDataURL(input.files[0]);
    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
});
$('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});  
// --------------------------------모델 불러오기--------------------------------------//

const URL = "./my_model/";

let model, webcam, labelContainer, maxPredictions;

async function init() {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";
    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // or files from your local hard drive
    // Note: the pose library adds "tmImage" object to your window (window.tmImage)
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();
    labelContainer = document.getElementById("label-container");
    for (let i = 0; i < maxPredictions; i++) { // and class labels
        labelContainer.appendChild(document.createElement("div"));
    }
    print
}

// --------------------------------결과--------------------------------------//

// run the webcam image through the image model
async function predict() {
    // predict can take in an image, video or canvas html element
        var image = document.getElementById("bean-image")
        const prediction = await model.predict(image, false);
        if(prediction[0].className == "점무늬병" && prediction[0].probability.toFixed(2)==1.00){
            labelContainer.childNodes[0].innerHTML += "병 : 점무늬병 <br> 증상 : 개구리눈과 같은 원형의 갈색반점이 형성. 구멍이 남 <br> 원인 : 감염식물체에서 균사상태로 월동하여 전염 됨 <br> 방제 : 저항성 품종을 심거나 건전종자를 사용하며, 돌려짓기 티오파네이트메틸, 트리플루미졸 수화제 살포"
        } else if(prediction[1].className == "불마름병" && prediction[1].probability.toFixed(2)==1.00){
            labelContainer.childNodes[0].innerHTML += "병 : 불마름병 <br> 증상 : 옅은 녹색 점무늬가 담갈색으로 변하고 주의가 노랗게 변함, 잎 뒷면에 돌기를 형성 <br> 원인 : 감염종자나 감영식물체의 잔재에서 월동 빗물에 의해 주변의 잎으로 전파 <br> 방제 : 저항성 품종을 심고, 수확 후 잔재물을 깨끗이 제거 발병초기에 아그리마이신 및 싸이클린 약제 살포"
        } else {
            labelContainer.childNodes[0].innerHTML = "알 수 없음"
        }
    }
    
    document.getElementById("test").style.display="none";
    document.getElementById("test").style.display="block";