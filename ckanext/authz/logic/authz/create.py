# -*- coding: utf-8 -*-
from ckan.plugins import toolkit as pt
import ckan.model as model


def admin_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''
    
    return {'success': True}
    
    model = context.get('model')
    user = context.get('user')
    
    data_dict['user'] = user
    data_dict['domain_object'] = model.System()
    data_dict['roles'] = ['admin']

    try:
        pt.check_access('user_role_update', context, data_dict)
        return {'success': True}
    except pt.NotAuthorized:
        return {'success': False,
                'msg': pt._('User {0} not authorized to read harvest source {1}')
                .format(user, 'admin role')}
        

def editor_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''
    return {'success': False}
    
    model = context.get('model')
    user = context.get('user')
    
    data_dict['user'] = user
    data_dict['domain_object'] = model.System()
    data_dict['roles'] = ['editor']

    try:
        pt.check_access('user_role_update', context, data_dict)
        return {'success': True}
    except pt.NotAuthorized:
        return {'success': False,
                'msg': pt._('User {0} not authorized to read harvest source {1}')
                .format(user, 'editor role')}
        

        
def reader_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''
    return {'success': True}
    
    model = context.get('model')
    user = context.get('user')

    data_dict['user'] = user
    data_dict['domain_object'] = model.System()
    data_dict['roles'] = ['reader']

    try:
        pt.check_access('user_role_update', context, data_dict)
        return {'success': True}
    except pt.NotAuthorized:
        return {'success': False,
                'msg': pt._('User {0} not authorized to read harvest source {1}')
                .format(user, 'reader role')}
        
        
        
def anon_editor_role_create(context, data_dict):
    '''
    Authorization check for changing the details of a role
    '''
    return {'success': True}
    
    model = context.get('model')
    user = context.get('user')

    data_dict['user'] = user
    data_dict['domain_object'] = model.System()
    data_dict['roles'] = ['anon_editor']

    try:
        pt.check_access('user_role_update', context, data_dict)
        return {'success': True}
    except pt.NotAuthorized:
        return {'success': False,
                'msg': pt._('User {0} not authorized to read harvest source {1}')
                .format(user, 'anon_editor_role')}