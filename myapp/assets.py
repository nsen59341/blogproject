from django_assets import Bundle, register
js = Bundle('common/jquery.js', 'site/base.js', 'site/widgets.js',
            filters='jsmin', output='gen/packed.js')
register('js_all', js)