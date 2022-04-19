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
                    $('.place').css('zIndex', -1)
                },
                'mouseout': function () {
                    cover.css('display', 'none')
                    big_box.css('display', 'none')
                    $('.place').css('zIndex', 1)
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
    })();


    // 地址ajax请求发送函数
    function sendOutAjax (id, type) {
        $.ajax({
            url: '/shopping/get_address/',
            data: {"id":id,"type":type},
            type: 'POST',
            // dataType: 'json',
            success: function (data) {
                // 动态创建元素
                let container = $('#ui-area-content-list')
                try {
                    let t = $('.select-address').attr('data-i')
                    for (i of data.data.address) {
                        // 进行切换时展示对应的已选的颜色
                        if (parseInt(t)===parseInt(i.id)) {
                            let li = $('<li><a class="current-address" data-id="'+i.id+'" href="javascript:void(0)">'+i.name+'</a></li>')
                            container.append(li)
                        } else {
                            let li = $('<li><a data-id="'+i.id+'" href="javascript:void(0)">'+i.name+'</a></li>')
                            container.append(li)
                        }
                    }
                } catch (e) {
                    // 如果没有请求到数据，那么就要清楚最后一个选项并且关闭选择，填充组合字段
                    $("#choice-address").css('display', 'none')
                    $('.select-address').remove()
                    $('#ui-area-tab>li:last').addClass('select-address')
                    let str = $('#ui-area-tab>li').text()
                    let reg = new RegExp("","g")
                    let result = str.replace(reg,"")
                    $('#address').html(result+'<i class="iconfont" style="font-size: 16px;">&#xe611;</i>')
                    // 发送请求获取地址列表
                    let index = $("#ui-area-tab>li").length-1
                    let id = $("#ui-area-tab>li").eq(index).attr("data-i")
                    sendOutAjax(id)
                    $("#address").removeClass("address-hover")
                }
            },
            timeout: 2000,
            error: function () {
                console.log('失败')
            }
        })
    }


    // 进行地址请求
    (function getAddress () {
        // 发送请求获取地址列表
        let index = $("#ui-area-tab>li").length-1
        let id = $("#ui-area-tab>li").eq(index).attr("data-i")
        sendOutAjax(id)
        function moveIn () {
            $("#address").addClass("address-hover")
            $("#choice-address").css('display', 'table')
        }
        function Remove () {
            $("#address").removeClass("address-hover")
            $("#choice-address").css('display', 'none')
        }
        // 地址选择显示与隐藏
        $(".place>div").on({
            mouseover: function () {
                moveIn ()
            },
            mouseout: function () {
                Remove ()
            }
        })
        // 地址选择
        $('#ui-area-tab').on('click','li',function(e) {
            let id = $(this).attr("data-i")
            let container = $('#ui-area-content-list')
            $(this).addClass('select-address')
            $(this).siblings('li').removeClass('select-address')
            container.empty('li')
            if (id) {
                sendOutAjax (id)
            } else {    // 次情况下id为空 获取最后一个li的前面li的data-i
                let id = $('#ui-area-tab>li').eq($('#ui-area-tab>li:last').index()-1).attr('data-i')
                sendOutAjax (id, 1)
            }
        })
        // 获取修改的地址进行填充并请求
        let container = $('#ui-area-content-list')
        container.on('click','a',function (e) {
            let choice = $('.select-address')
            choice.html(e.target.innerText+'<i class="iconfont" style="font-size: 16px;">&#xe611;</i>')
            choice.attr("data-i",e.target.getAttribute('data-id'))
            // 抹除在$('.select-address')后的所有元素
            choice.nextAll().remove()
            // 添加选择元素
            let li = $('<li>请选择<i class="iconfont" style="font-size: 16px;">&#xe611;</i></li>')
            choice.after(li)
            // 将$('.select-address')给到请选择
            $('#ui-area-tab>li:last').addClass('select-address').siblings('li').removeClass('select-address')
            // 清楚原本就有的数据
            let container = $('#ui-area-content-list')
            container.empty('li')
            // 发送请求获取 请选择的数据
            sendOutAjax (e.target.getAttribute('data-id'),1)
        })
    })()
})
