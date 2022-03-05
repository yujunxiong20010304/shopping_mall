$(function () {
    /* 发送ajax请求判断是否存在当前邮箱与用户名 */
    const input = $('input')
    const i = $('i')
    const btn = $('button')
    const span = $('span')
    let username_judge = false
    let password_judge = false
    let passwords_judge = false
    let email_judge = false
    let i_focus = [
        '4-20位字符，可由中文，英文数字或符号\'_\'组成',
        '6-20个大小写英文字母,符号或数字的组合',
        '请再次输入密码',
        '请填写正确的邮箱，以便激活账号，找回密码'
    ]

    let i_blur = [
        ['用户名不能为空','请输入正确的用户名，用户名应为4-20位字符','你输入的用户名已存在，请重新输入'],
        ['密码不能为空','请输入正确的密码，密码应为6-20位字符'],
        '两次输入密码不一致',
        ['格式错误请输入正确邮箱号','你输入的邮箱已存在，请重新输入']
    ]
    input.focus(function () {
        let index = $(this).index('input')  /* 第几个input */
        span.eq(index).css({'font-size': 12, lineHeight: '25px', transition: 'all .3s', color: 'red'})
        input.eq(index).css({'border': '1px solid green', borderRadius: 5})
        i.eq(index).css({'opacity': 1,transition: 'all 2s'}).text(i_focus[index])
    })

    input.blur (function () {
        let index = $(this).index('input')  /* 第几个input */
        span.eq(index).css({'font-size': 14, lineHeight: '30px', color: '#fff'})
        /*i.eq(index).css({'opacity': 0,transition: 'all .5s'})*/
        $(this).css({'border': '0', borderRadius: 0})
        /* 用户情况 */
        /* 用户名为空 */
        switch (index){
            /* 用户名情况 */
            case 0:
                if(!$(this).val()) {
                    i.eq(0).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[0][0])
                    username_judge = false
                } else if ($(this).val().length<4) {
                    i.eq(0).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[0][1])
                    username_judge = false
                } else {
                    $.post('/oauth/judge_email_username/',{username: $(this).val(), email: null}, function (data) {
                        if(data.msg.username==='username') {
                            i.eq(0).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[0][2])
                            username_judge = false
                        } else {
                            i.eq(0).css({'opacity': 0,transition: 'all .5s'})
                            username_judge = true
                        }
                    })
                }
                /* 此处需要jquery发送ajax请求获取数据 */
                break;
            case 1:
                if(!$(this).val()) {
                    i.eq(1).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[1][0])
                    password_judge = false
                } else if($(this).val().length<6){
                    i.eq(1).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[1][1])
                    password_judge = false
                }else {
                    i.eq(1).css({'opacity': 0,transition: 'all .5s'})
                    password_judge = true
                }
                break;
            case 2:
                if(!input.eq(1).val()) {
                    i.eq(1).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[1])
                    passwords_judge = false
                } else if($(this).val() !== input.eq(1).val()) {
                    i.eq(2).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[2])
                    passwords_judge = false
                } else {
                    i.eq(2).css({'opacity': 0,transition: 'all .5s'})
                    passwords_judge = true
                }
                break;
            case 3:
                let myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
                if (!myreg.test($(this).val())) {
                    i.eq(3).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[3][0])
                    email_judge = false
                }else {
                    $.post('/oauth/judge_email_username/',{username: null, email: $(this).val()}, function (data) {
                        if(data.msg.email==='email') {
                            i.eq(3).css({'opacity': 1,transition: 'all 2s'}).text(i_blur[3][1])
                            email_judge = false
                            console.log('if',data.msg,data.msg==='email')
                        }else {
                            i.eq(3).css({'opacity': 0,transition: 'all .5s'})
                            console.log('else',data.msg,data.msg==='email')
                            email_judge = true
                        }
                    })
                    // i.eq(3).css({'opacity': 0,transition: 'all .5s'})
                    // email_judge = true
                }
                break;
        }
    })
    btn.click(function () {
       if (username_judge&&password_judge&&passwords_judge&&email_judge) {
           $.post('/oauth/register/',
               {'username': input.eq(0).val(), 'password': input.eq(1).val(), 'email': input.eq(3).val()},
               function (data) {
                   if (data.msg==='success') {
                        swal({
                          title: "注册成功",
                          text: "请尽快前往邮箱进行账号激活",
                          icon: "success",
                          button: "前往邮箱",
                        });
                        $('.swal-button,.swal-button--confirm').click(function () {
                            $('.swal-button').attr('backgroundColor','#1DAB39')
                            location.replace('https://mail.qq.com/cgi-bin/frame_html?')
                        })
                   }
               })
        }
    });


})
