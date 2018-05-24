import './sass/main.scss';

$(document).ready(function() {
  var $pageInfo = $('#page-info');
  if($pageInfo.data('background-image')) {
    $('body').css('background-image', 'url(' + $pageInfo.data('background-image') + ')')
              .css('background-size', 'cover')
              .css('background-position', 'center center');
  } else {
    $('body').css('background-color', $pageInfo.data('background-color'));
  }
  if($pageInfo.data('menu-font-color')) {
    $('.navigation-menu__item a').css('color', $pageInfo.data('menu-font-color'));
  }
  if($pageInfo.data('menu-font-color-hover')) {
    $('.navigation-menu__item a').hover(function(e) {
      $(this).css('color', e.type === 'mouseenter' ? $pageInfo.data('menu-font-color-hover') : $pageInfo.data('menu-font-color'));
    });
  }

  $('.album-container__link').featherlight($('.album-container__img'), {});
});