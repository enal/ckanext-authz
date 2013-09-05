# -*- coding: utf-8 -*-
import os
import re
from logging import getLogger
from pylons import config
from pylons.i18n import _
from genshi.input import HTML
from genshi.filters import Transformer

import ckan.lib.helpers as h

from ckan.lib.search import SearchError
from ckan.lib.helpers import json

from ckan import model

from ckan.plugins import implements, SingletonPlugin
import ckan.plugins as p
import ckanext.authz.logic.action.create as a


log = getLogger(__name__)


class Authz(SingletonPlugin):

    p.implements(p.IActions)


    def get_actions(self):

        return {'editor_role_create': a.editor_role_create}
        module_root = 'ckanext.authz.logic.action'
        action_functions = self._get_logic_functions(module_root)
        
        fobj_out = open('/home/administrator/pyenv/out.txt', 'wb')
        fobj_out.write('These are the actions that were exported: ' +  str(action_functions))
        fobj_out.close()
        log.debug('These are the actions that were exported: %s', action_functions)

        return action_functions
    
    
    def _get_logic_functions(self,module_root, logic_functions = {}):
    
        for module_name in ['get', 'create']:

            
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
                    
            fobj_out = open('/home/administrator/pyenv/out.txt', 'wb')
            fobj_out.write('module_path: ' + str(module_path))
            fobj_out.write('module_path: ' + str(module_path))
            fobj_out.close()
    
        return logic_functions