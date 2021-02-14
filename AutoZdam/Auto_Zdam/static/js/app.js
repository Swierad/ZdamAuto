

// Slider

$(function(){
  $('.bxslider').bxSlider({
    mode: 'fade',
    captions: true,
    slideWidth: 600
  });
});


// burger menu

$(function(){
        var burger = document.querySelector('.burger');
        var nav = document.querySelector('#'+burger.dataset.target);

        burger.addEventListener('click', function(){
            burger.classList.toggle('is-active');
            nav.classList.toggle('is-active');
        });
    })


