---
layout: page
title: Blog
subtitle: ramblings of me
---

<div>
{% assign postsCategory = site.posts | group_by_exp:"post", "post.categories"  %}
{% for category in postsCategory %}
<h4 class="post-teaser__month">
<span class="color_strong">
{% if category.name %} 
<br>
<span class="category-name">- - - - - - {{ category.name }} - - - - - -</span>
{% else %} 
{{ Print }} 
{% endif %}
</span>
</h4>
<ul class="list-posts">
{% for post in category.items %}
<li class="post-teaser">
<a href="{{ post.url | relative_url }}" class="no-target-blank">
<span class="post-teaser__title">{{ post.title }}</span>
<span class="post-teaser__date">{{ post.date | date: "%d %B %Y" }}</span>
</a>
</li>
{% endfor %}
</ul>
{% endfor %}
</div>