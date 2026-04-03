---
layout: news
title: Album
permalink: /album
---

<style>
.album-carousel, .album-single {
  width: 50%;
  margin: 0 auto;
}
.album-carousel {
  position: relative;
  padding-bottom: 28.125%;
  height: 0;
}
.album-carousel .carousel-inner {
  position: absolute;
  inset: 0;
}
.album-carousel .carousel-item img, .album-single img {
  width: 100%;
  display: block;
}
</style>

# Album

---

{% if site.data.album %}
{% for yearGroup in site.data.album %}
### {{ yearGroup.year }}

{% for item in yearGroup.items %}
#### {{ item.date }}
{% include album_entry.html item=item %}
<hr>
{% endfor %}
{% endfor %}
{% else %}
No photos yet.
{% endif %}
