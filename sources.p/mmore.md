Title: 修改more标签
Date: 2010-07-16 00:40
Author: ahui
Category: 网络
Tags: blog, Linux, Network
Slug: mmore

参考地址　http://codex.wordpress.org/Customizing\_the\_Read\_More

修改loop.php  
查找第二处"continue reading"，该行改为


    <?php the_content("......点此阅读t " . get_the_title('', '', false) . " 全文......"); >


function.php底部加入脚本，用于跳转到文章开头.

    function remove_more_jump_link($link) { 
        $offset = strpos($link, '#more-');
        if ($offset) {
            $end = strpos($link, '"',$offset);
        }
        if ($end) {
            $link = substr_replace($link, '', $offset, $end-$offset);
        }
        return $link;
    }
    add_filter('the_content_more_link', 'remove_more_jump_link');
