window.addEventListener('load', () => {
    document.getElementById('loading_image').style.display = "none";
    document.getElementById('page_content').style.display = "block";
});

let showloading = () => {
    document.getElementById('page_content').style.display = "none";
    document.getElementById('loading_image').style.display = "flex";
}