# -*- coding: utf-8 -*-
import logging

from ckan import logic
import ckan.model as model
import ckan.model.authz as authz
import traceback
from ckan.logic import NotFound, check_access

log = logging.getLogger(__name__)

def admin_role_delete(context,data_dict):
    '''
    Deletes admin role for the given user
    
    :param user_name: the name of the user 
    
    :returns: on success True otherwise False
    :rtype: string
    '''   
        
    if( check_access('admin_role_create',context,data_dict) == True):
    
        user_name = data_dict.get('user_name')
        log.info('Creating admin role for user: %r', user_name)
        try:
            user = model.User.get(user_name)
            authz.remove_user_from_role(user,u'admin',model.System())
            model.Session.commit()
            return {'success': True}
        except:
            return{'success' : False}
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}
        

def editor_role_delete(context,data_dict):
    '''
    Deletes editor role for the given user
    
    :param user_name: the name of the user 
    
    :returns: on success True otherwise False
    :rtype: string
    '''
    if( check_access('admin_role_create',context,data_dict) == True):
    
        user_name = data_dict.get('user_name')
        log.info('Creating editor role for user: %r', user_name)
        try:
            user = model.User.get(user_name)
            authz.remove_user_from_role(user,u'editor',model.System())
            model.Session.commit()
            return {'success': True}
        except:
            return{'success' : False,
                   'msg' : traceback.print_exc()}
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}      
        


def reader_role_delete(context,data_dict):
    '''
    Deletes reader role for the given user
    
    :param user_name: the name of the user 
    
    :returns: on success True otherwise False
    :rtype: string
    '''
    if( check_access('admin_role_create',context,data_dict) == True):
    
        user_name = data_dict.get('user_name')
        log.info('Creating reader role for user: %r', user_name)
        try:
            user = model.User.get(user_name)
            authz.remove_user_from_role(user,u'reader',model.System())
            model.Session.commit()
            return {'success': True}
        except:
            return{'success' : False,
                   'error' : traceback.print_exc()}    
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}
         
        
        
def anon_editor_role_delete(context,data_dict):
    '''
    Deletes reader role for the given user
    who gets editor role 
    
    :returns: on success True otherwise False
    :rtype: string
    '''
    if( check_access('admin_role_create',context,data_dict) == True):
    
        user_name = data_dict.get('user_name')
        log.info('Creating reader role for user: %r', user_name)
        try:
            user = model.User.get(user_name)
            authz.remove_user_from_role(user,u'anon_editor',model.System())
            model.Session.commit()
            return {'success': True}
        except:
            return{'success' : False,
                   'error' : traceback.print_exc()}    
    else:
        return{'success' : False,
                   'msg' : 'authentication failed'}
            



