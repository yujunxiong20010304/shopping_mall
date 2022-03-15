$(function () {
    // 切换商品图片
    $('.other_img>img').mouseover(function () {
        $(this).css('border','2px solid red');
        $(this).parents("li").children('.main_img').prop('src', $(this).prop('src'))
        $(this).siblings('img').css('border', '2px solid #fff');
    })
    let len = 20
    // 分页器
    $('#paging').on('click','.paging', function () {
        let len = 20    // 总页数
        let page = parseInt($(this).text())// 点击的页数
        if(page>5 && page<len-2) {
            // 新建...
            if(!$('.start').length) {
                $('.paging:eq(2)').text('...')
                $('.paging:eq(2)').removeClass('paging').addClass('start')
            }
            // 后四个li重新赋值
            let value = parseInt($(this).text())-2
            // 防止无限制添加最后一个li
            if ($('.paging').length<7) {
                $('.last').before($('<li class="paging">'+(value+4)+'</li>'))
            }
            $('.start').nextAll().each(function () {
                if (parseInt($(this).text())) {
                    $(this).text(value++)
                }
            })
            if(!$('.last').length) {
                $('.next').before($('<li class="last">...</li>'))
            }
            $('.paging').removeClass('active')
            $('.paging:eq(4)').addClass('active')
        } else if(parseInt($(this).text())<=5) {
            // 去除 ...
            let i = 1
            if($('.start').length) {
                $('.start').text(3).removeClass('start').addClass('paging')
                $('.paging').each(function () {
                    $(this).text(i++)
                })
                if (!$('.last').length) {
                    $('.next').before($('<li class="last">...</li>'))
                }
            }
            // 去除最后的li
            if ($('.paging').length>7) {
                $('.paging:last').remove()
            }
            $('.paging').removeClass('active')
            $(this).addClass('active')
            if (page===5) {
                $('.paging').removeClass('active')
                $('.paging:eq(4)').addClass('active')
            }
        } else {
            let val = 16
            if ($('.last').length) {
                let position = $(this).text()
                $('.start').nextAll().each(function () {
                    if (parseInt($(this).text())) {
                        $(this).text(val++)
                    }
                })
                $('.last').remove()
                $('.paging').removeClass('active')
                $('.paging:eq('+(parseInt(position)-14)+')').addClass('active')
            } else {
                $('.paging').removeClass('active')
                $(this).addClass('active')
            }

        }
    })

    // 分页下一页
    $('.next').on('click', function () {
        if(!($('.start').length&&$('.last').length)) {
            let index = $('.active').index('.paging')
            if (index<6) {
                index+=1
                $('.paging').removeClass('active')
                $('.paging:eq('+index+')').addClass('active')
                $('.active').click()
            }
        } else {
            $('.paging').removeClass('active')
            $('.paging:eq(5)').addClass('active')
            $('.active').click()
        }
    })

    // 分页上一页
    $('.prev').on('click', function () {
        if(!($('.start').length&&$('.last').length)) {
            let index = $('.active').index('.paging')
            if (index>0) {
                index -= 1
                $('.paging').removeClass('active')
                $('.paging:eq('+index+')').addClass('active')
                $('.active').click()
            }
        }else {
            $('.paging').removeClass('active')
            $('.paging:eq(3)').addClass('active')
            $('.active').click()
        }


    })

    // 分页跳转
    $('.jump').on('click',function() {
        let index = $('.jump_num').val()
        if(index <=5 ) {
            if($('.start').length) {

                let i =1
                $('.start').text(3).removeClass('start').addClass('paging')
                $('.paging').each(function () {
                    $(this).text(i++)
                })
                if (!$('.last').length) {
                    $('.next').before($('<li class="last">...</li>'))
                }
                $('.paging').removeClass('active')
                $('.paging:eq('+(index-1)+')').addClass('active')
            } else {
                $('.paging').removeClass('active')
                $('.paging:eq('+(index-1)+')').addClass('active')
            }
            if ($('.paging').length>7) {
                $('.paging:last').remove()
            }

        } else if (index<len-2) {

            if(!$('.start').length) {
                $('.paging:eq(2)').text('...')
                $('.paging:eq(2)').removeClass('paging').addClass('start')
            }
            // 后四个li重新赋值
            let value = index-2
            // 防止无限制添加最后一个li
            if ($('.paging').length<7) {
                $('.last').before($('<li class="paging">'+(value+4)+'</li>'))
            }
            $('.start').nextAll().each(function () {
                if (parseInt($(this).text())) {
                    $(this).text(value++)
                }
            })
            if(!$('.last').length) {
                $('.next').before($('<li class="last">...</li>'))
            }
            $('.paging').removeClass('active')
            $('.paging:eq(4)').addClass('active')







        } else {

            if (!$('.start').length) {

                $('.paging').removeClass('active')
                $('.paging:eq(5)').addClass('active')
                $('.paging:eq(5)').click()
            }


            let val = 16
            let position = $(this).text()
            $('.start').nextAll().each(function () {
                if (parseInt($(this).text())) {
                    $(this).text(val++)
                }
            })
            $('.last').remove()
            $('.paging').removeClass('active')
            $('.paging:eq(' + (index - 14) + ')').addClass('active')

        }
    })
})
