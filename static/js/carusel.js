$(document).ready(function() {
    var carousel = $("#movie-carousel");
    var carouselList = carousel.find("ul");
    var carouselItems = carouselList.find("li");
    var carouselItemWidth = carouselItems.first().outerWidth(true);
  
    var leftArrow = $("");
    var rightArrow = $("");
    carousel.append(leftArrow).append(rightArrow);
  
    var scrollLeft = function() {
      carouselList.animate({scrollLeft: "-=" + carouselItemWidth}, 500);
    };
  
    var scrollRight = function() {
      carouselList.animate({scrollLeft: "+=" + carouselItemWidth}, 500);
    };
  
    leftArrow.on("click", scrollLeft);
    rightArrow.on("click", scrollRight);
});
  

