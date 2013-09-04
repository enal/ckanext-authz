import logging
from sqlalchemy import or_
from ckan.model import User

from ckan import logic
from ckan.plugins import PluginImplementations

import ckan.plugins as p
from ckan.logic import NotFound, check_access, side_effect_free



log = logging.getLogger(__name__)

@side_effect_free
def roles_list(context,data_dict):
    '''
    Returns the any current roles
    
    :returns: roles
    :rtype: dictionary
    '''

    return 'deprecated' 