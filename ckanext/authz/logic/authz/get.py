# -*- coding: utf-8 -*-

from ckan.plugins import toolkit as pt


def roles_list(context, data_dict):
    '''
    Authorization check for getting the details of the current roles
    
    '''
    return {'success': True}
    
    '''model = context.get('model')
    user = context.get('user')
    source_id = data_dict['id']

    pkg = model.Package.get(source_id)
    if not pkg:
        raise pt.ObjectNotFound(pt._('Harvest source not found'))

    context['package'] = pkg

    try:
        pt.check_access('package_show', context, data_dict)
        return {'success': True}
    except pt.NotAuthorized:
        return {'success': False,
                'msg': pt._('User {0} not authorized to read harvest source {1}')
                .format(user, source_id)}'''