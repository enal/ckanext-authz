# -*- coding: utf-8 -*-
from ckan.plugins import toolkit as pt
import ckan.model as model
from ckanext.harvest.logic.auth import user_is_sysadmin



def admin_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''    
    if not user_is_sysadmin(context):
        return {'success': False, 'msg': pt._('Only sysadmins can create new roles')}
    else:
        return {'success': True}
    
            

def editor_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''
    if not user_is_sysadmin(context):
        return {'success': False, 'msg': pt._('Only sysadmins can create new roles')}
    else:
        return {'success': True}
        

        
def reader_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''
    if not user_is_sysadmin(context):
        return {'success': False, 'msg': pt._('Only sysadmins can create new roles')}
    else:
        return {'success': True}
        
        
        
def anon_editor_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''
    if not user_is_sysadmin(context):
        return {'success': False, 'msg': pt._('Only sysadmins can create new roles')}
    else:
        return {'success': True}