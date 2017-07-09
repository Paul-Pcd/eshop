/**
 * Created by Administrator on 2017/7/9.
 */
$(function () {
    var $num_show = $('.num_show');
    var $total_price = $('.total em')
    var goods_price = parseFloat($('.show_pirze em').text());
    var $goods_ku_cun = $('.show_kucun');
    $('.add').click(function () {
        var goods_num = parseInt($num_show.val());
        if (goods_num >= 20) {
            alert("亲最多只能购买20个,给别人留点");
        } else {
            var total_num = parseInt($num_show.val(goods_num + 1).val());
            get_total_price(total_num)
        }
    });
    $('.minus').click(function () {
        var goods_num = parseInt($num_show.val());
        if (goods_num <= 1) {
            alert("亲就买一个吧 生活不易啊");
        } else {
            var total_num = $num_show.val(goods_num - 1).val();
            get_total_price(total_num)
        }
    });
    // 自己输入数量的判断
    $num_show.blur(function () {
        var inpunt_total_num = parseInt($num_show.val())
        if (isNaN(inpunt_total_num)) {
            alert("亲请输入一个整数可以啊");
            $num_show.val(1);
            inpunt_total_num = 1;
        } else if (inpunt_total_num < 1) {
            alert("亲就买一个吧 生活不易啊");
            $num_show.val(1);
            inpunt_total_num = 1;
        } else {
            if (inpunt_total_num >= 20) {
                alert("亲最多只能购买20个,给别人留点");
                $num_show.val(20);
                inpunt_total_num = 20;
            }
        }
        get_total_price(inpunt_total_num)

    });
    // 计算总的价格
    function get_total_price(total_num) {
        var total_price = new Number(total_num * goods_price).toFixed(2)
        $total_price.html(total_price + "元");
    }

    // 发送ajax请你
    function ajax() {
        $.get("{% url 'shop:detail' goods_info.id %}", function (data) {
            alert(data);
        });
    }

    // 加入购物车
    var $add_cart = $('#add_cart');
    var $show_count = $('#show_count');
    var $add_jump = $('.add_jump');
    var $add_top = $add_cart.offset().top;
    var $add_left = $add_cart.offset().left;

    var $to_top = $show_count.offset().top;
    var $to_left = $show_count.offset().left;
    var add_jump_top = $add_jump.offset().top;
    var add_jump_left = $add_jump.offset().left;
    //
    // $add_jump.css({
    //     'left': $add_left + 80,
    //     'top': $add_top + 10,
    //     'display': 'block'
    // });
    $add_cart.click(function () {
        var goods_total_num = parseInt($('.num_show').val());
        var goods_url = $("input[name='hidden']").val();
        $.get(goods_url, function (data) {
            num = data.data;
            $('.show_kucun em').html(num);
            if (goods_total_num < num) {
                $('#show_count').html(goods_total_num);
            }
        });
        $add_jump.css({
            'left': $add_left + 80,
            'top': $add_top + 10,
            'display': 'block'
        });
        $(".add_jump").stop().animate({
                'left': $to_left + 7,
                'top': $to_top + 7
            },
            "fast",
            function () {
                $(".add_jump").fadeOut('fast', function () {
                    // $('#show_count').html(2);
                    // $(".add_jump").css({
                    //     'left': add_jump_left,
                    //     'top':add_jump_top,
                    //     'display': 'none'
                    // });
                });

            });
    });

});