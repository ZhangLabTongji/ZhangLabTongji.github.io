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

{% assign labImages = site.static_files | where_exp: "file", "file.path contains '/assets/img/lab/' and file.name contains 'lab20'" | sort: "name" %}
{% assign albumGroups = labImages | group_by_exp: "file", "file.basename | slice: 3, 8" | sort: "name" | reverse %}
{% assign currentYear = "" %}

{% for group in albumGroups %}
{% assign dateKey = group.name %}
{% assign year = dateKey | slice: 0, 4 %}
{% capture dateIso %}{{ year }}-{{ dateKey | slice: 4, 2 }}-{{ dateKey | slice: 6, 2 }}{% endcapture %}
{% assign dateLabel = dateIso | date: site.date_format %}
{% if year != currentYear %}
### {{ year }}
{% assign currentYear = year %}
{% endif %}
#### {{ dateLabel }}
{% include album_entry.html carouselId=dateKey dateLabel=dateLabel images=group.items %}
<hr>
{% endfor %}
{% if albumGroups.size == 0 %}
No photos yet.
{% endif %}
