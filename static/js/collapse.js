var collapses = document.getElementsByClassName("collapse");

for(let i = 0; i < collapses.length; i++) {
    collapses[i].addEventListener("click", function() {
        this.classList.toggle("active");
        let content = this.nextElementSibling;
        if(content.style.maxHeight) {
            content.style.maxHeight = null;
        }else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}