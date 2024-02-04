function previewImage() {
    console.log('previewImage function called');
    var input = document.getElementById('image');
    var previewContainer = document.getElementById('image-preview-container');
    var previewImage = document.createElement('img');

    while (previewContainer.firstChild) {
        previewContainer.removeChild(previewContainer.firstChild);
    }

    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            console.log('Image URL:', e.target.result);
            previewImage.src = e.target.result;
            previewImage.classList.add('clothe-image'); 
            previewImage.style.width = '500px'; 
            previewImage.style.margin = '0 auto';
            previewImage.style.height = 'auto'; 
        }
        reader.readAsDataURL(input.files[0]);
        previewContainer.appendChild(previewImage);
    }
}

function submitSortForm() {
    document.getElementById("sortForm").submit();
}

