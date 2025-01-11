const fileUpload = document.getElementById("file_upload");
const fileName = document.getElementById("file_name");

fileUpload.addEventListener("change", () => {
    if (fileUpload.files.length > 0) {
        fileName.textContent = fileUpload.files[0].name;
    } else {
        fileName.textContent = "No file chosen";
    }
});