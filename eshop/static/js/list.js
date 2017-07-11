/**
 * Created by gogo on 17-7-12.
 */
$(function () {
    var add_url = $('#add_url').text();
    var $show_count = $('#show_count');
    $('.add_goods').click(function () {
        // 在列表也点击购物车
        var goods_num = parseInt($show_count.text());
        var total_num = $show_count.text(goods_num + 1);
        data = {'total_num': total_num, 'buy_num': 1};
        $.get(add_url, data, function (data) {
            console.log(data);
        })

    });
});