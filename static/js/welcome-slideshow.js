window.addEventListener('load', function() {
    var images = ["static/img/welcome_slideshow/garage2.jpg", "static/img/welcome_slideshow/garage3.jpg", "static/img/welcome_slideshow/garage1.jpg"];
    var currentIndex = 0;
    var slideshowImage = document.getElementById("slideshow-image");

    console.log(images);
  
    function nextImage() {
        currentIndex = (currentIndex + 1) % images.length;
        slideshowImage.style.opacity = 0; // fade out --> aktuális kép
        setTimeout(function() {
          slideshowImage.src = images[currentIndex];
          slideshowImage.style.opacity = 1; // fade --> köv. kép
        }, 3000);
    }      
      
  
    setInterval(nextImage, 7000); //kep valtasa 8mp-enkent
});  