$(document).ready(function(){
$(window).scroll(function(){
    if(this.scrollY > 20){
        $('.navbar').addClass("sticky")
    }else {
        $('.navbar').removeClass("sticky")
    }
});

// toggle menu/navbar script 
$('.menu-btn').click(function(){
    $('.navbar .menu').toggleClass("active");
    $('.menu-btn i').toggleClass("active")
})

// typing animation script 
let typed = new Typed(".typing",{
    strings: ["PAINLESS", "Make The Pain Go Away"],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
})
});

// Tag Canvas
window.onload = function() {
    // set colour of text and outline of active tag
    TagCanvas.textColour = '#blue'
    TagCanvas.outlineColour = '#ff9999';
    TagCanvas.Start('myCanvas') 
    TagCanvas.wheelZoom (false)
};
