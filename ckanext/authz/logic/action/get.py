# -*- coding: utf-8 -*-
import logging
from sqlalchemy import or_
from ckan.model import User

from ckan import logic
from ckan.plugins import PluginImplementations

import ckan.plugins as p
import traceback
import ckan.model.authz as authz
from ckan.logic import NotFound, check_access
import ckan.model as model



log = logging.getLogger(__name__)

def roles_user_list(context,data_dict):
    '''
    Returns the roles of the given user
    
    :returns: roles
    :rtype: dictionary
    '''      
    if( check_access('roles_user_list',context,data_dict) == True):
    
        user_name = data_dict.get('user_name')
        log.info('Looking up roles for user %r ...', user_name)
        try:
            user = model.User.get(user_name)
            
            roles = {'System' : [],
                     'Group': [],
                     'Package': []}
            
            if(authz.user_has_role(user, u'admin', model.System())):
                roles['System'].append('admin')
            if(authz.user_has_role(user, u'admin', model.Package())): 
                roles['Group'].append('admin')
            if(authz.user_has_role(user, u'admin', model.Group())): 
                roles['Package'].append('admin')
                
                
            if(authz.user_has_role(user, u'editor', model.System())):
                roles['System'].append('editor')
            if(authz.user_has_role(user, u'editor', model.Package())): 
                roles['Package'].append('editor')
            if(authz.user_has_role(user, u'editor', model.Group())): 
                roles['Group'].append('editor')
                           
                
            if(authz.user_has_role(user, u'reader', model.System())):
                roles['System'].append('reader')
            if(authz.user_has_role(user, u'reader', model.Package())): 
                roles['Package'].append('reader')
            if(authz.user_has_role(user, u'reader', model.Group())): 
                roles['Group'].append('reader')
                
            
            result = roles
            return {'success': True,
                    'result' : result}
        except:
            return{'success' : False,
                   'msg' : traceback.print_exc()} 
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}
    


