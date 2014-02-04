title: "相关文章Related Posts by Category的配置"
id: 170
date: 2010-07-30 12:07:07
tags: 
- blog
- Network
categories: 
- Linux
- 网络
---

编辑single.php,放到comments_template之前.

<pre class="brush:php">
&lt;br />
<div class="entry-title"">
相关文章
</div>
<div id="related_posts" class="box">
   &lt;?php do_action(
    'related_posts_by_category',
    array(
      'orderby' => 'post_date',
      'order' => 'DESC',
      'limit' => 5,
      'echo' => true,
      'before' => '&lt;li>',
      'inside' => '&raquo; ',
      'outside' => '',
      'after' => '&lt;/li>',
      'rel' => 'nofollow',
      'type' => 'post',
      'image' => array(50, 50),
      'hidden' => 'image',
      'message' => '没有相关文章.'
    )
  ) ?>
</div>
</pre>

 其中'hidden' => 'image'防止自动显示相关图片.