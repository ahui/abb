Title: 相关文章Related Posts by Category的配置
Date: 2010-07-30 12:07
Author: ahui
Category: Linux, 网络
Tags: blog, Network
Slug: related-posts-by-category

编辑single.php,放到comments\_template之前.

~~~~ {.brush:php}
<br />

相关文章


   <?php do_action(
    'related_posts_by_category',
    array(
      'orderby' => 'post_date',
      'order' => 'DESC',
      'limit' => 5,
      'echo' => true,
      'before' => '<li>',
      'inside' => '» ',
      'outside' => '',
      'after' => '</li>',
      'rel' => 'nofollow',
      'type' => 'post',
      'image' => array(50, 50),
      'hidden' => 'image',
      'message' => '没有相关文章.'
    )
  ) ?>
~~~~

其中'hidden' =\> 'image'防止自动显示相关图片.
