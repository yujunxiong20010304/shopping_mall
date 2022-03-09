$(function () {
    // 求轮播页数
    $('#carouselExampleCaptions').on('slid.bs.carousel', function () {
        let	active=$(this).find(".active");
	    let index=active.index();
	    $('.index').text(index+1)
    })
})
