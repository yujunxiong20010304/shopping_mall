$(function(){
    // 商品类别点击
    $('.a-choice').on('click', function () {
        $(this).addClass('ch-re')
        $(this).siblings('li').removeClass('ch-re')
        getPrice()
    })
    // 发送请求当前选择价格的函数
    function getPrice () {
        let i = $('.pic_num').hasClass('double')
        if (i) {
            // 获取所有当前已选择的项
            let result = {}
            let mapping = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six'}
            for (i of $('.ch-re')) {
                let id = i.getAttribute('data-id')
                let type = i.getAttribute('data-type')
                result[mapping[type]] = id
            }
            $.ajax({
                url: '/shopping/details/',
                data: {"result":JSON.stringify(result)},
                type: 'POST',
                // dataType: 'json',
                success: function (data) {
                    if (data.data) {
                        $('.price').html(data.data.price)
                    }
                },
                timeout: 2000,
                error: function () {
                    console.log('失败')
                }
            })
        }
    }

    // 展示图片的切换
    (function picture_switching () {
        $('.lh>li>img:eq(0)').css('border', '2px solid red')
        $('.lh>li>img').on('mouseover', function () {
            let src = $(this).prop('src')
            $('.s-i-img').prop('src', src)
            $('.big-img').prop('src', src)
            $('.lh>li>img').css('border', '2px solid #fafafa')
            $(this).css('border', '2px solid red')
        })
    })();

    // 放大镜
    (function enlarge_picture() {
            // 最大盒子
            let box = $('#spec-img')
            // 图片
            let img = $('.s-i-img')
            // 遮照层
            let cover = $('.move-cover')
            // 放大图片盒子容器
            let big_box = $('.box-img')
            // 放大图片
            let big_img = $('.big-img')
            // 遮照层+放大盒子容器的显示
            box.on({
                'mouseover': function () {
                    cover.css('display', 'block')
                    big_box.css('display', 'block')
                },
                'mouseout': function () {
                    cover.css('display', 'none')
                    big_box.css('display', 'none')
                },
                'mousemove': function (e) {
                    let mouseX = e.pageX-box.offset().left;
                    let mouseY = e.pageY-box.offset().top;
                    cover.css({'left':mouseX-cover.width()/2,'top':mouseY-cover.height()/2})
                    // 限制左右遮照层不会跑出去
                    if (cover.offset().left<box.offset().left) {
                        cover.css('left',0)
                    } else if (cover.offset().left>box.offset().left+box.width()-cover.width()) {
                        cover.css('left',box.width()-cover.width())
                    }
                    // 限制遮照层上下不会跑出去
                    if (cover.offset().top<box.offset().top) {
                        cover.css('top',0)
                    } else if (cover.offset().top>box.offset().top+box.height()-cover.height()) {
                        cover.css('top', box.height()-cover.height())
                    }

                    big_img.css({'left':-(cover.offset().left-box.offset().left)*2.5, 'top':-(cover.offset().top-box.offset().top)*2.5})
                }
            })
            big_box.on('mousemove', function () {
                big_box.css('display', 'none')
            })
    })();

    // 展示图片的底部轮播
    (function rotation () {
        let box = $('.lh-box')
        let ul = $('.lh')
        let li_len = $('.lh>li').length
        $('.sd:eq(0)').on('click', function () {
            // 限制
            if(ul.offset().left-box.offset().left) {
                // 判断进行长距离跳跃
                ul.css({'left': 0,'transition': 'all .7s'})
                // 单次移动长度
                // ul.css('left', 58+ul.offset().left-box.offset().left)
            }
        })
        $('.sd:eq(1)').on('click', function () {
            // 限制
            let x = ul.width()-box.width()
            if(box.offset().left-ul.offset().left-x) {
                // 单次移动长度
                ul.css({'left': -x,'transition': 'all .7s'})
                // ul.css('left', -58+ul.offset().left-box.offset().left)
            }

        })
    })()

})
