# -*- coding: utf-8 -*-
import sys
from pprint import pprint

from ckan import model
from ckan.logic import get_action, ValidationError

from ckan.lib.cli import CkanCommand

class Authentication(CkanCommand):
    '''Changes remotely authentication configurations

    Usage:
    
      authz add-admin {name}
        - Gives admin rights to the given user. This means the user can perform any action including: edit, read, delete, update-permissions on any object.
        
      authz add-editor {name}
        - Gives editor rights to the given user. This means the user can edit, read and create new objects.
        
      authz add-reader {name}
        - Gives reader rights to the given user. This means the user can perform any action on any object.
        
      authz add-anon_editor {name}
        - Gives editor rights to anonymous (i.e. not logged in) users. This means the user can edit and read any object
    
      
      authz rm-admin {name}
        - Removes admin rights from the given user.
        
      authz rm-editor {name}
        - Removes editor rights from the given user. 
        
      authz rm-reader {name}
        - Removes reader rights from the given user. 
        
      authz rm-anon_editor {name}
        - Removes editor rights from anonymous (i.e. not logged in) users.
    
    
    authz roles-user {name}
        - Displays current roles of the given user.   
      authz roles
        - Displays any current roles.

    The commands should be run from the ckanext-authz directory and expect
    a development.ini/production.ini file to be present. Most of the time you will
    specify the config explicitly though::

        paster authz roles --config=../ckan/development.ini

    '''

    summary = __doc__.split('\n')[0]
    max_args = 2
    min_args = 0

    def __init__(self,name):

        super(Authentication,self).__init__(name)


    def command(self):
        self._load_config()

        # We'll need a sysadmin user to perform most of the actions
        # We will use the sysadmin site user (named as the site_id)
        context = {'model':model,'session':model.Session,'ignore_auth':True}
        self.admin_user = get_action('get_site_user')(context,{})


        print ''

        if len(self.args) == 0:
            self.parser.print_usage()
            sys.exit(1)
        cmd = self.args[0]
        if cmd == 'roles':
            self.list_all_roles()
        if cmd == 'roles-user':
            self.list_user_roles()
        elif cmd == "add-admin":
            self.add_admin()
        elif cmd == 'add-editor':
            self.add_editor()
        elif cmd == 'add-reader':
            self.add_reader()
        elif cmd == 'add-anon_editor':
            self.add_anon_editor          
        elif cmd == "rm-admin":
            self.remove_admin()
        elif cmd == 'rm-editor':
            self.remove_editor()
        elif cmd == 'rm-reader':
            self.remove_reader()
        elif cmd == 'rm-anon_editor':
            self.remove_anon_editor
        else:
            print 'Command %s not recognized' % cmd

    def _load_config(self):
        super(Authentication, self)._load_config()
        
    def list_user_roles(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)
        
        context = {
            'model':model,
            'session':model.Session,
            'user': self.admin_user['name'],
            'ignore_auth': True,
        }
        source = get_action('roles_user_list')(context,{'user_name':user_name})
        
        if(source['success'] == True):
            roles = source['result']
            self.print_roles(roles)
        else:
            print 'An error occurred: ' + str(source['msg'])


    def list_all_roles(self):
        context = {
            'model':model,
            'session':model.Session,
            'user': self.admin_user['name'],
            'ignore_auth': True,
        }
        source = get_action('roles_all_list')(context,{})
        
        if(source['success'] == True):
            user_roles = source['result']
            for user_role in user_roles:
                print 'User: %s' % user_role['name']
                self.print_roles(user_role['roles'])
                print '\n'
        else:
            print 'An error occurred: ' + str(source['msg'])
        

    def print_roles(self,roles):
            print 'System: %s' % roles['System'] 
            print 'Group: %s' % roles['Group'] 
            print 'Package: %s' % roles['Package']
            


    def add_admin(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('admin_role_create')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role admin is successfully created for user %s' % user_name
        else:
            print 'An error occurred: ' + str(result['msg'])
    
    def add_editor(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('editor_role_create')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role editor is successfully created for user %s' % user_name
        else:
            print 'An error occurred: ' +  str(result['msg'])

     
    def add_reader(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('reader_role_create')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role reader is successfully created for user %s' % user_name
        else:
            print 'An error occurred: ' +  str(result['msg'])
            
            
    def add_anony_editor(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('anon_editor_role_create')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role anon_editor is successfully created for user %s' % user_name
        else:
            print 'An error occurred: ' + str(result['msg'])


    def remove_admin(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('admin_role_delete')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role admin is successfully deleted for user %s' % user_name
        else:
            print 'An error occurred: ' + str(result['msg'])
    
    def remove_editor(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('editor_role_delete')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role editor is successfully deleted for user %s' % user_name
        else:
            print 'An error occurred: ' + str(result['msg'])

     
    def remove_reader(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('reader_role_delete')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role reader is successfully deleted for user %s' % user_name
        else:
            print 'An error occurred: ' + str(result['msg'])
            
            
    def remove_anony_editor(self):
        if len(self.args) >= 2:
            user_name = unicode(self.args[1])
        else:
            print 'Please provide a name'
            sys.exit(1)

        context = {'model': model,'session':model.Session, 'user': self.admin_user['name']}
        result = get_action('anon_editor_role_delete')(context,{'user_name':user_name})

        if result['success'] == True:
            print 'role anon_editor is successfully deleted for user %s' % user_name
        else:
            print 'An error occurred: ' + str(result['msg'])


    

