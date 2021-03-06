# -*- coding: utf-8 -*-
import os
import re
from logging import getLogger
from ckan.plugins import implements, SingletonPlugin
import ckan.plugins as p


log = getLogger(__name__)


class Authz(SingletonPlugin):

    p.implements(p.IActions)
    p.implements(p.IAuthFunctions)


    # for IActions
    def get_actions(self):

        module_root = 'ckanext.authz.logic.action'
        action_functions = self._get_functions(module_root)

        return action_functions
    
    
    # for IAuthFunctions
    def get_auth_functions(self):

        module_root = 'ckanext.authz.logic.authz'
        auth_functions = self._get_functions(module_root)

        return auth_functions
    
    
    def _get_functions(self,module_root, logic_functions = {}):
    
        for module_name in ['get', 'create', 'delete']:
            
            module_path = '%s.%s' % (module_root, module_name,)
            try:
                module = __import__(module_path)
            except ImportError:
                log.debug('No auth module for action "{0}"'.format(module_name))
                continue
    
            for part in module_path.split('.')[1:]:
                module = getattr(module, part)
    
            for key, value in module.__dict__.items():
                if not key.startswith('_') and (hasattr(value, '__call__')
                            and (value.__module__ == module_path)):
                    logic_functions[key] = value
    
        return logic_functions