---
layout: default
title: All Essays
permalink: /essays/
---
<p class="nav-back"><a href="{{ '/' | relative_url }}">← home</a></p>

<h1>All Essays</h1>
<p class="tagline">{{ site.essays | size }} essays, sorted by date</p>

<ul class="essay-index">
{% assign sorted = site.essays | sort: 'date' | reverse %}
{% for essay in sorted %}
    <li>
        {% if essay.date %}<span class="date">{{ essay.date | date: "%Y-%m-%d" }}</span>{% endif %}
        <a href="{{ essay.url | relative_url }}">{{ essay.title }}</a>
        {% if essay.day %}<span class="quiet"> · Day {{ essay.day }}</span>{% endif %}
    </li>
{% endfor %}
</ul>
