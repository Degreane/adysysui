from sanic import Sanic, response, static
from sanic_session import Session
from sanic.log import logger
import jinja2 as j2
import os
import sys
from pprint import pprint as pp
import asyncio
empty_html_template = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="author" content="Faysal Al-Banna" />
        <meta name="description" content="AdySys Web UI HTML Builder" />
        <link rel="stylesheet" type="text/css" href="/css/adysys.css?{{range(1,100)|random}}">
        <link rel="stylesheet" type="text/css" href="/aloha/src/css/aloha.css">
        <script src="/aloha/src/lib/require.js?{{range(1,1000)|random}}" ></script>
        <script src="/aloha/src/lib/aloha.js?{{range(1,1000)|random}}"
        data-aloha-plugins="common/format,common/table,common/list,common/link,common/highlighteditables,common/block,common/undo,common/contenthandler,common/paste,common/commands,common/abbr,common/image,extra/browser,extra/linkbrowser"></script>
        <title>Build1</title>
    </head>
    <body id='content_body'>
        <div id='content'>
        </div>
    <script defer>
        Aloha.ready( function() {
            Aloha.jQuery('#content').aloha();
        });
    </script>
    </body>
</html>
'''

accesslog_file = open('../accesslog_file.log', 'a')


CUSTOM_LOGIN_CONFIG = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        "root": {
            "level": "INFO",
            "handlers": ["console"]
        },
        "sanic.error": {
            "level": "INFO",
            "handlers": ["error_console"],
            "propagate": True,
            "qualname": "sanic.error"
        },

        "sanic.access": {
            "level": "INFO",
            "handlers": ["access_console"],
            "propagate": True,
            "qualname": "sanic.access"
        }
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": accesslog_file
        },
    },
    formatters={
        "generic": {
            "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: " +
                      "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
    }
)
app = Sanic('AdySysSanicServer', log_config=CUSTOM_LOGIN_CONFIG)
Session(app)


@app.route('/favicon.ico')
async def favicon(request):
    project_path = os.path.join(os.getcwd(), 'src', 'css', 'web-icons', 'graph.png')
    return await response.file_stream(project_path)


@app.route('/build/html/<path>', methods=['GET', ], name="getNewPageBuild")
async def getBuildPage(request, path):
    if not request['session'].get('path'):
        return response.json({'SessionError': path})
    else:
        # page_path = os.path.join(request['session'].get('path'), 'adysys', 'build', 'html', path)
        return response.html('{0}'.format(empty_html_template))
        # with open(page_path) as fd:


@app.route('/build/html', methods=['POST', ], name="setNewPageBuild")
async def pageRequest(request):
    pp(request.body)
    # pp(request.parsed_args)
    pp(request.form)
    if not request['session'].get('path'):
        # pp(dir(request))
        return response.json({'pageCreation': 'Fail'})
    else:
        '''
        here we print the request header and then we return json success
        1- get project path from the session
        2- add to it 'adysys'
        3- add to it the build,html
        '''
        project_path = os.path.join(request['session'].get('path'), 'adysys', 'build', 'html')
        os.makedirs(project_path, exist_ok=True)
        with open(os.path.join(project_path, request.form['newPage'][0]), 'w') as fd:
            fd.write(empty_html_template)
        return response.json({'pageCreation': 'Success'})


@app.route('/')
async def home(request):
    pp(request['session'])
    if not request['session'].get('path'):
        with open(os.path.join(os.getcwd(), 'src', 'tpl', 'invalid_access.html')) as fd:
            html_tpl = fd.read()
        return response.html(html_tpl)
    else:
        env = j2.Environment(
            loader=j2.FileSystemLoader(os.path.join(request['session']['path'], 'adysys', 'src', 'tpl')),
            auto_reload=True
        )

        # page_tpl_path=os.path.join(request['session']['path'],'adysys','src','tpl','adysys.html')
        # with open (page_tpl_path,'r') as fd:
        #     page_tpl=fd.read()
        response_tpl = env.get_template(name='designer.html')
        # j2.Template(page_tpl)
        title = os.path.split(request['session']['path'])[-1]
        response_html = response_tpl.render({'title': title})
        return response.html(response_html, headers={
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        })


@app.route('/project')
async def setProject(request):
    # app.read_config(request)
    # response.redirect('/')

    if 'js' not in app.router.routes_static_files:
        app.static('/js', os.path.join(request.raw_args['path'], 'adysys', 'src', 'js'), name="js")
    if 'css' not in app.router.routes_static_files:
        app.static('/css', os.path.join(request.raw_args['path'], 'adysys', 'src', 'css'), name="css")
    if 'images' not in app.router.routes_static_files:
        app.static('/img', os.path.join(request.raw_args['path'], 'adysys', 'src', 'images'), name="images")
    if 'videos' not in app.router.routes_static_files:
        app.static('/vid', os.path.join(request.raw_args['path'], 'adysys', 'src', 'videos'), name="videos")
    if 'aloha' not in app.router.routes_static_files:
        app.static('/aloha', os.path.join(request.raw_args['path'], 'adysys', 'src', 'aloha'), name='aloha')
    request['session']['path'] = request.raw_args['path']
    # print(request['session'])
    print(app.router.routes_static_files)
    return response.redirect('/')

if __name__ == '__main__':
    app.go_fast(host='0.0.0.0', port=6910, debug=True, access_log=True)
    # log_config=LOGGING
