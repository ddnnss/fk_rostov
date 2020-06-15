

$(document).ready(function () {
    const body = document.querySelector('body');
    let isMobile = false; //initiate as false
    // device detection
    if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent)
        || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0,4))) {
        isMobile = true;
        body.classList.add('mobile-device');
    }
    // input placeholder animation
    if (document.querySelector('.type-input')){
        $('.type-input input').focus(function(){
            $(this).parents('.type-input').addClass('focused');
        });

        $('.type-input input').blur(function(){
            var inputValue = $(this).val();
            if ( inputValue == "" ) {
                $(this).removeClass('filled');
                $(this).parents('.type-input').removeClass('focused');
            } else {
                $(this).addClass('filled');
            }
        });

        $('.type-input textarea').focus(function(){
            $(this).parents('.type-input').addClass('focused');
        });
        $('.type-input textarea').blur(function(){
            var inputValue = $(this).val();
            if ( inputValue == "" ) {
                $(this).removeClass('filled');
                $(this).parents('.type-input').removeClass('focused');
            } else {
                $(this).addClass('filled');
            }
        });
    }
    // swiper matches init
    if (document.querySelector('.matches__slider')) {
        let matchesSwiper = new Swiper('.matches__slider', {
           slidesPerView: 1,
           spaceBetween: 0 ,
            navigation: {
                nextEl: '.matches__slider-next',
                prevEl: '.matches__slider-prev',
            },
            effect: 'fade',
            fadeEffect: {
                crossFade: true
            },
            speed:950,

        });
    }
    //swiper news init
    if (document.querySelector('.news-slider')) {
        let matchesSwiper = new Swiper('.news-slider', {
            slidesPerView: 3,
            spaceBetween: 33 ,
            navigation: {
                nextEl: '.news__slider-next',
                prevEl: '.news__slider-prev',
            },
            speed:950,
            breakpoints: {
                950: {
                    slidesPerView: 3,
                    spaceBetween: 33 ,
                },
                1: {
                    slidesPerView: 'auto',
                    spaceBetween: 33 ,
                }
            }

        });
    }
    // swiper photos init
    if (document.querySelector('.actual-picture__slider')) {
        let matchesSwiper = new Swiper('.actual-picture__slider', {
            slidesPerView: 5,
            spaceBetween: 30,
            navigation: {
                nextEl: '.actual-picture__slider-next',
                prevEl: '.actual-picture__slider-prev',
            },
            speed:950,
            breakpoints: {
                950: {
                    slidesPerView: 5,
                    spaceBetween: 30,
                },
                1: {
                    slidesPerView: 'auto',
                    spaceBetween: 30,
                }
            }
        });
    }
    // swiper stadium init
    if (document.querySelector('.our-stadium__slider')) {
        let matchesSwiper = new Swiper('.our-stadium__slider', {
            slidesPerView: 1,
            spaceBetween: 0,
            pagination: {
                el: '.our-stadium__slider-pagination',
                clickable: true,
            },
            speed:660,
            effect: 'fade',
            fadeEffect: {
                crossFade: true
            },
        });
    }
    // open menu
    if (document.querySelector('.open-menu')){
        const button = document.querySelector('.open-menu > a');
        $(button).on('click',function (e) {
            e.preventDefault();
            let heightWindow = window.innerHeight;
            let heightDocument = $(body).height();
            let topCss = document.querySelector('header').offsetHeight -  $(window).scrollTop() ;;
            if ((heightDocument - heightWindow) > 0 ) {
                    $(body).toggleClass('no-scroll');
            }
            if (body.classList.contains('menu-opened')){
                $(body).removeClass('no-scroll');
            }
            $(body).toggleClass('menu-opened');
            $('.header__hidden').css('top',topCss +'px');
        });
    }
    //slides seo list
    if (document.querySelector('.place-seo__slides')){
        let items = document.querySelectorAll('.place-seo__slides-item');
        for (let i = 0 ; i <items.length; i++){
            items[i].querySelector('.place-seo__slides-item-title').addEventListener('click' ,function () {
               if (!(this.parentNode.classList.contains('active'))) {
                   $(items[i]).parent().find('.active').removeClass('active');
                   $(this).parent().addClass('active');
               }
            });
        }
    }
    // contacts map
    if (document.getElementById('map')){
        ymaps.ready(init);

        function init() {
            var myMap = new ymaps.Map("map", {
                    center: [47.20918820872907,39.73786247323844],
                    zoom: 15,
                    controls: []
                }),
                myPlacemark1 = new ymaps.Placemark([47.20918820872907,39.73786247323844], {
                    // Свойства.
                }, {
                    // Опции.
                    iconLayout: 'default#image',
                    // Своё изображение иконки метки.
                    iconImageHref: 'img/map-icon.png',
                    // Размеры метки.
                    iconImageSize: [50, 50],
                    // Смещение левого верхнего угла иконки относительно
                    // её "ножки" (точки привязки).
                });

            //myMap.controls.add('smallZoomControl');
            // // Добавляем все метки на карту.
            myMap.geoObjects.add(myPlacemark1);

        }

    }
    // close fancy on click
    if (document.querySelector('.modal')){
        let modals = document.querySelectorAll('.modal');
        for (let i = 0 ; i < modals.length ; i++){
            modals[i].querySelector('.modal__close > a').addEventListener('click',function (e) {
               e.preventDefault();
                $.fancybox.close()
            });
        }
    }
    //players swiper init logic
    if (document.querySelector('.line-up__slider')){
        let sliders = document.querySelectorAll('.line-up__slider');
        for (let i = 0 ; i < sliders.length; i++) {
            let initParam = sliders[i].querySelectorAll('.swiper-slide').length > 4;
            if (initParam) {
                sliders[i].parentNode.parentNode.classList.add('inited');
            }
            let playersSwiper = new Swiper(sliders[i] , {
                slidesPerView: 4,
                spaceBetween: 20,
                init: initParam,
                navigation: {
                    nextEl: sliders[i].parentNode.parentNode.querySelector('.line-up__slider-next'),
                    prevEl: sliders[i].parentNode.parentNode.querySelector('.line-up__slider-prev'),
                },
                speed:950,
                breakpoints: {
                    1: {
                        slidesPerView: 'auto',
                        spaceBetween: 17,
                    },
                    759: {
                        spaceBetween: 17,
                        slidesPerView:3,
                    },
                    950: {
                        slidesPerView: 4,
                        spaceBetween: 20,
                    }
                }
            });
            if (window.innerWidth < 951 ) {
                sliders[i].parentNode.parentNode.classList.add('inited');
                playersSwiper.init();
            }
        }

    }
    //remove filled class om input change
    if (document.querySelector('.type-input')){
        let inputs = document.querySelectorAll('.type-input input , .type-input textarea');
        for (let i = 0 ; i < inputs.length ; i++){
            inputs[i].addEventListener('input',function (e) {
                if (this.value.length <= 0){
                    this.parentNode.classList.remove('filled');
                }
                else {
                    this.parentNode.classList.add('filled');
                }
            });
        }
    }
    // bilet form logic
    if (document.querySelector('.bilet-form')){
            let sectors = document.querySelectorAll('.sector-item:not(.reserved)');
            let sectorsModal = document.querySelector('.stadium-map__select .stadium-map__modal');
            let places  = document.querySelectorAll('.type-place:not(.type-place_type-reserved)');
            let placesModal = document.querySelector('.bilet-form__place-map-body .stadium-map__modal');
            $('.sector-item:not(.reserved)').on('click',function (e) {
                let sector = this ;
              let child = $(this).children()[0];
              let childObj = child.getBBox();
                if (childObj.x < 1 || childObj.y < 1 ) {
                    $(sectorsModal).css('top',child.transform.baseVal[0].matrix.f+'px');
                    $(sectorsModal).css('left',child.transform.baseVal[0].matrix.e+'px');
                }
                else {
                    $(sectorsModal).css('top',childObj.y+'px');
                    $(sectorsModal).css('left',childObj.x+'px');
                }
                $('.sector-item').removeClass('clicked');
                $(this).addClass('clicked');
                $(sectorsModal).addClass('visible');
                let timerId = setTimeout(function () {
                    if (sector.classList.contains('clicked')) {
                        $(sectorsModal).removeClass('visible');
                        $(sector).removeClass('clicked');
                    }
                },3500);
            });
            $('#choose-sector').on('click',function (e) {
                e.preventDefault();
                $('.bilet-form__sector').removeClass('active');
                $('.bilet-form__place').addClass('active');
            });
            $('.back-to-sector').on('click',function (e) {
                e.preventDefault();
                $('.bilet-form__sector').addClass('active');
                $('.bilet-form__place').removeClass('active');
            });
            $('.type-place:not(.type-place_type-reserved) > *').on('click',function (e) {
                e.preventDefault();
                let place = this.parentNode;
                $(placesModal).addClass('visible');
                let rect = this.parentNode.getBoundingClientRect();
                let childPos = $(this.parentNode).offset();
                let parentPos = $(this.parentNode.parentNode.parentNode).offset();
                let childOffset = {
                    top: childPos.top - parentPos.top,
                    left: childPos.left - parentPos.left
                };
                let square = this.parentNode.offsetWidth;
                $(placesModal).css('left',childOffset.left  +'px' );
                $(placesModal).css('top',+(childOffset.top + square) +'px');
                $('.type-place').removeClass('clicked');
                $(this).parent().addClass('clicked');
                let timerId = setTimeout(function () {
                    if (place.classList.contains('clicked')) {
                        $(placesModal).removeClass('visible');
                        $(place).removeClass('clicked');
                    }
                },3500);
            })
        }
    // sticky blocks
    if (document.querySelector('.sticky')) {
        let blocks = document.querySelectorAll('.sticky');
        for (let i = 0 ; i < blocks.length ; i++){
            $(blocks[i]).sticky({topSpacing:0});
        }
    }
});


