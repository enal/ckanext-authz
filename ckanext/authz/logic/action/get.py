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
                
            for role in [u'admin',u'editor', u'reader']:      
                if(authz.user_has_role(user, role, model.System())):
                    roles['System'].append(role)
                if(authz.user_has_role(user, role, model.Package())): 
                    roles['Package'].append(role)
                if(authz.user_has_role(user, role, model.Group())): 
                    roles['Group'].append(role)
                
            
            result = roles
            return {'success': True,
                    'result' : result}
        except:
            return{'success' : False,
                   'msg' : traceback.print_exc()} 
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}
        
     
        
def roles_all_list(context,data_dict):
    '''
    Returns the roles of the given user
    
    :returns: roles
    :rtype: dictionary
    '''      
    if( check_access('roles_all_list',context,data_dict) == True):
    
        user_name = data_dict.get('user_name')
        log.info('Looking up roles for user %r ...', user_name)
        try:
            all_roles = []
            users = model.User.all()          
            for user in users:
                user_roles = {'name' : user.name}
                
                roles = {'System' : [],
                         'Group': [],
                         'Package': []} 
         
                for role in [u'admin',u'editor', u'reader']:      
                    if(authz.user_has_role(user, role, model.System())):
                        roles['System'].append(role)
                    if(authz.user_has_role(user, role, model.Package())): 
                        roles['Package'].append(role)
                    if(authz.user_has_role(user, role, model.Group())): 
                        roles['Group'].append(role)
                                                
                user_roles['roles'] = roles
                
                all_roles.append(user_roles)

            result = all_roles
            return {'success': True,
                    'result' : result}
        except:
            return{'success' : False,
                   'msg' : traceback.print_exc()} 
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}


