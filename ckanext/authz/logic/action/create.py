import logging

from ckan import logic
import ckan.model as model
import ckan.model.authz as authz


log = logging.getLogger(__name__)

def admin_role_create(context,data_dict):
    '''
    Creates a new admin role for the given user
    
    :param user_name: the name of the user who gets editor role 
    
    :returns: on success True otherwise False
    :rtype: string
    '''
    user_name = data_dict.get('user_name')
    log.info('Creating admin role for user: %r', user_name)
    try:
        user = model.User.get(user_name)
        authz.add_user_to_role(user,u'admin',model.System())
        model.Session.commit()
        return {'success': True}
    except:
        return{'success' : False}
        
    return None


def editor_role_create(context,data_dict):
    '''
    Creates a new editor role for the given user
    
    :param user_name: the name of the user who gets editor role 
    
    :returns: on success True otherwise False
    :rtype: string
    '''
    user_name = data_dict.get('user_name')
    log.info('Creating editor role for user: %r', user_name)
    try:
        user = model.User.get(user_name)
        authz.add_user_to_role(user,u'editor',model.System())
        model.Session.commit()
        return {'success': True}
    except:
        return{'success' : False}
        
    return None

def reader_role_create(context,data_dict):
    '''
    Creates a new reader role for the given user
    
    :param user_name: the name of the user who gets editor role 
    
    :returns: on success True otherwise False
    :rtype: string
    '''
    user_name = data_dict.get('user_name')
    log.info('Creating reader role for user: %r', user_name)
    try:
        user = model.User.get(user_name)
        authz.add_user_to_role(user,u'reader',model.System())
        model.Session.commit()
        return {'success': True}
    except:
        return{'success' : False}
        
    return None
        
def anon_editor_role_create(context,data_dict):
    '''
    Creates a new reader role for the given user
    
    :param user_name: the name of the user who gets editor role 
    
    :returns: on success True otherwise False
    :rtype: string
    '''
    user_name = data_dict.get('user_name')
    log.info('Creating reader role for user: %r', user_name)
    try:
        user = model.User.get(user_name)
        authz.add_user_to_role(user,u'anon_editor',model.System())
        model.Session.commit()
        return {'success': True}
    except:
        return{'success' : False}
        
    return None


