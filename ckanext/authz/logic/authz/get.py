# -*- coding: utf-8 -*-

from ckan.plugins import toolkit as pt
from ckanext.harvest.logic.auth import user_is_sysadmin

def roles_list(context, data_dict):
    '''
    Authorization check for getting the details of the current roles
    
    '''
    if not user_is_sysadmin(context):
        return {'success': False, 'msg': pt._('Only sysadmins can view current roles')}
    else:
        return {'success': True}