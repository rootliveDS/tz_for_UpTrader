from django import template
from menu_app.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(title=menu_name).first()
    if menu:
        return render_menu(menu)

def render_menu(menu_item):
    if menu_item:
        html = f'<ul><li><a href="{menu_item.url}">{menu_item.title}</a></li>'
        children = menu_item.children.all()
        if children:
            html += '<ul>'
            for child in children:
                html += render_menu(child)
            html += '</ul>'
        html += '</ul>'
        return html
    return ''

@register.filter
def is_active(url, request_url):
    if url == request_url:
        return 'active'
    return ''