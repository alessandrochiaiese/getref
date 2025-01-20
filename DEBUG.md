2025-01-20 15:22:52,567: Error running WSGI application
2025-01-20 15:22:52,568: django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
2025-01-20 15:22:52,568: Did you install mysqlclient?
2025-01-20 15:22:52,568:   File "/var/www/myuser_pythonanywhere_com_wsgi.py", line 22, in <module>
2025-01-20 15:22:52,569:     application = get_wsgi_application()
2025-01-20 15:22:52,569: 
2025-01-20 15:22:52,569:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/core/wsgi.py", line 12, in get_wsgi_application
2025-01-20 15:22:52,569:     django.setup(set_prefix=False)
2025-01-20 15:22:52,570: 
2025-01-20 15:22:52,570:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/__init__.py", line 24, in setup
2025-01-20 15:22:52,571:     apps.populate(settings.INSTALLED_APPS)
2025-01-20 15:22:52,571: 
2025-01-20 15:22:52,571:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/apps/registry.py", line 114, in populate
2025-01-20 15:22:52,571:     app_config.import_models()
2025-01-20 15:22:52,571: 
2025-01-20 15:22:52,572:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/apps/config.py", line 301, in import_models
2025-01-20 15:22:52,572:     self.models_module = import_module(models_module_name)
2025-01-20 15:22:52,572: 
2025-01-20 15:22:52,572:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/contrib/auth/models.py", line 3, in <module>
2025-01-20 15:22:52,572:     from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
2025-01-20 15:22:52,573: 
2025-01-20 15:22:52,573:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/contrib/auth/base_user.py", line 48, in <module>
2025-01-20 15:22:52,573:     class AbstractBaseUser(models.Model):
2025-01-20 15:22:52,573: 
2025-01-20 15:22:52,574:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/db/models/base.py", line 122, in __new__
2025-01-20 15:22:52,574:     new_class.add_to_class('_meta', Options(meta, app_label))
2025-01-20 15:22:52,574: 
2025-01-20 15:22:52,574:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/db/models/base.py", line 326, in add_to_class
2025-01-20 15:22:52,574:     value.contribute_to_class(cls, name)
2025-01-20 15:22:52,575: 
2025-01-20 15:22:52,575:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/db/models/options.py", line 207, in contribute_to_class
2025-01-20 15:22:52,576:     self.db_table = truncate_name(self.db_table, connection.ops.max_name_length())
2025-01-20 15:22:52,576: 
2025-01-20 15:22:52,576:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/utils/connection.py", line 15, in __getattr__
2025-01-20 15:22:52,576:     return getattr(self._connections[self._alias], item)
2025-01-20 15:22:52,577: 
2025-01-20 15:22:52,577:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/utils/connection.py", line 62, in __getitem__
2025-01-20 15:22:52,577:     conn = self.create_connection(alias)
2025-01-20 15:22:52,577: 
2025-01-20 15:22:52,577:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/db/utils.py", line 204, in create_connection
2025-01-20 15:22:52,578:     backend = load_backend(db['ENGINE'])
2025-01-20 15:22:52,578: 
2025-01-20 15:22:52,578:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/db/utils.py", line 111, in load_backend
2025-01-20 15:22:52,578:     return import_module('%s.base' % backend_name)
2025-01-20 15:22:52,578: 
2025-01-20 15:22:52,579:   File "/home/myuser/.virtualenvs/myuser.pythonanywhere.com/lib/python3.6/site-packages/django/db/backends/mysql/base.py", line 20, in <module>
2025-01-20 15:22:52,579:     ) from err
2025-01-20 15:22:52,579: ***************************************************
2025-01-20 15:22:52,579: If you're seeing an import error and don't know why,
2025-01-20 15:22:52,580: we have a dedicated help page to help you debug: 
2025-01-20 15:22:52,580: https://help.pythonanywhere.com/pages/DebuggingImportError/