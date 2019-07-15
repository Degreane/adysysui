import os
import sys
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from pymitter import EventEmitter
from threading import Thread
import subprocess
import asyncio
import sysrsync


class project():
    def __init__(self, args):
        self.__args = args

        self.___populate_project_tree()

        self.___start_sanic()
        self.___start_gui()

    def ___populate_project_tree(self):
        '''
        - read the project directory provided self.__args.project
        - create project_path directory tree as needed
        - read self.project_tree and populate
        :return:
        '''
        project_path = self.__args.project
        path = ""
        for dir in os.path.split(project_path):
            path = os.path.join(path, dir)
            if not os.path.exists(path):
                try:
                    os.mkdir(path)
                except Exception as ex:
                    print("Couldn't Create Directory {0}".format(path))
                    print(ex)
                    sys.exit()
        if not os.path.exists(os.path.join(project_path, 'adysys')):
            os.mkdir(os.path.join(project_path, 'adysys'))
        self.___copy_project_tree_files()

    def ___copy_project_tree_files(self):
        '''
        - read self.project_tree and populate directories as needed
        :return:
        '''
        # def ig(src,name):
        #     return ["pyqt"]
        # project_path=os.path.join(self.__args.project,'adysys')
        # try:
        #     shutil.copytree(os.path.join(os.getcwd(),'adysys','src'),os.path.join(project_path,'src'),ignore=ig)
        # except FileExistsError:
        #     print("Err")
        #     pass
        # Instead of using copytree i am going to use rsync implementation
        sysrsync.run(source=os.path.join(os.getcwd(), 'adysys', 'src'), destination=os.path.join(self.__args.project, 'adysys', 'src'), verbose=True, options=['-c', '-v', '-r', '-u'])

    def ___start_sanic(self):
        # import adysys.server
        # sanic_server=server.webworker(self.__args.project,self.__ee)
        # Sanic is deployed and be used with gunicorn server
        if os.path.exists('sserver.pid'):
            with open('sserver.pid', 'r') as fd:
                pid = int(fd.read())
                try:
                    os.kill(pid, 9)
                    os.remove('sserver.pid')
                except Exception as Ex:
                    if Ex.args[0] == 3:
                        print(Ex.args)
                    else:
                        print(Ex)
                        sys.exit()
        cwd = os.getcwd()
        os.chdir(os.path.join(cwd, 'adysys'))
        subprocess.run(['gunicorn', 'server:app', '-D', '--error-logfile', '../sserver_err.log', '--disable-redirect-access-to-syslog', '--access-logfile', '../sserver_access.log', '--bind', '0.0.0.0:6910', '--worker-class', 'sanic.worker.GunicornWorker', '--reload', '-p', '../sserver.pid'])
        # subprocess.run(['gunicorn', 'server:app', '--error-logfile', '../sserver_err.log', '--disable-redirect-access-to-syslog', '--access-logfile', '../sserver_access.log', '--bind', '0.0.0.0:6910', '--worker-class', 'sanic.worker.GunicornWorker', '--reload', '-p', '../sserver.pid'])

        os.chdir(cwd)

    def ___start_gui(self):
        from adysys.projectwindow import start_gui
        start_gui(self.__args.project)
