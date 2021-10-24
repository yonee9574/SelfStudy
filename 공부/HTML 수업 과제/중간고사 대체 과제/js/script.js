// -------------------------------------------------------------------------------------------------------------------------------------------

// 외부 스크립트 (전반적인 메인페이지 스크립트)
$(document).ready(function() {
    var menuLink = $('.burger');
    var menu = $('.menu');
    var close = $('.btn-close');
    var navLink = $('ul li a');
    var content = $('.content');

    menuLink.click(function() {
        menu.toggleClass('menu_active');
    });

    close.click(function() {
        menu.toggleClass('menu_active');
    });

    navLink.on('click', function(event) {
        event.preventDefault();
        var target = $(this).attr('href');        
        var top = $(target).offset().top;        
        $('html, body').animate({scrollTop: top}, 500);
        menu.toggleClass('menu_active');
    });

    content.click(function() {
        menu.toggleClass('menu_active');
    });
});
// 외부 스크립트 (전반적인 메인페이지 스크립트) END

// -------------------------------------------------------------------------------------------------------------------------------------------

// 스킬바 스크립트

$('.skill-percent').each(function(){
    $(this).animate({
      width:$(this).attr('data-percent')},"fast");
    });

// 스킬바 스크립트 END

// -------------------------------------------------------------------------------------------------------------------------------------------