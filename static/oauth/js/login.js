$(function(){
    /* 登录验证码验证 */
    $('#verification').click(function () {
        $.getJSON("refresh_captcha/", function (result) {
            $('#verification').attr('src', result['image_url']);
            $('#id_captcha_0').val(result['hashkey'])
        });
    });
});
