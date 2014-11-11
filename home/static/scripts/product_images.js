$(document).ready(function () {
    var isSwappable = true;
    
    $('.mainprodimg').click(function () {
        var $this = $(this);
        window.open($this.parent().children('a').first().attr('href'));
    });

    $('.thumbprodimg').click(function () {
        if (isSwappable) {
            isSwappable = false;
            // Swap with the main image.
            var $thumb = $(this)
            , $div = $thumb.parent().first()
            , $a = $div.children('a').first()
            , $img = $div.children('.mainprodimg').first()
            , origThumb = $thumb.attr('src')
            , origThumbAlt = $thumb.attr('alt')
            , origA = $a.attr('href')
            , origImg = $img.attr('src')
            , origImgAlt = $img.attr('alt')
            , $mainThumb = $('#prodimgs .thumbprodimg').first()
            , $mainA = $('#prodimgs > div > a').first()
            , $mainImg = $('#prodimgs .mainprodimg').first();
            
            $thumb.fadeOut(function () {
                $thumb.fadeIn();
            });

            $mainImg.fadeOut(function () {
                $thumb.attr('src', $mainThumb.attr('src'));
                $thumb.attr('alt', $mainThumb.attr('alt'));
                $a.attr('href', $mainA.attr('href'));
                $img.attr('src', $mainImg.attr('src'));
                $img.attr('alt', $mainImg.attr('alt'));

                $mainThumb.attr('src', origThumb);
                $mainThumb.attr('alt', origThumbAlt);
                $mainA.attr('href', origA);
                $mainImg.attr('src', origImg);
                $mainImg.attr('alt', origImgAlt);
                $mainImg.fadeIn(function () {
                    isSwappable = true;
                });
            });
        }
    });
});