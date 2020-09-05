{% if messages %}
    {% for message in messages %}
        alert("{{message.message}}"); //alert는 "~"로 적어주는 것 까먹지 말자 ! 
    {% endfor %}
{% endif %}