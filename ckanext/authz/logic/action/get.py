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

def roles_list(context,data_dict):
    '''
    Returns the any current roles
    
    :returns: roles
    :rtype: dictionary
    '''      
    if( check_access('roles_list',context,data_dict) == True):
    
        user_name = data_dict.get('user_name')
        log.info('Creating admin role for user: %r', user_name)
        try:
            user = model.User.get(user_name)
            
            admin_s = authz._user_query(user, u'admin', model.System())
            admin_p = authz._user_query(user, u'admin', model.Package())
            admin_g = authz._user_query(user, u'admin', model.Group())
            
            result = admin_s +admin_p + admin_g
            
            #authz.add_user_to_role(user,u'admin',model.System())
            #model.Session.commit()
            return {'success': True,
                    'result' : result}
        except:
            return{'success' : False,
                   'error' : traceback.print_exc()} 
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}
    


