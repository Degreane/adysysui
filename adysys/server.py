from sanic import Sanic, response, static
from sanic_session import Session
import jinja2 as j2
import os

app = Sanic('AdySysSanicServer')
Session(app)


@app.route('/')
async def home(request):
    print(request['session'])
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
        response_tpl = env.get_template(name='toolbox_ppael.html')
        # j2.Template(page_tpl)
        title = os.path.split(request['session']['path'])[-1]
        response_html = response_tpl.render({'title': title})
        return response.html(response_html)


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
    request['session']['path'] = request.raw_args['path']
    print(request['session'])
    print(app.router.routes_static_files)
    return response.redirect('/')

if __name__ == '__main__':
    app.go_fast(host='0.0.0.0', port=6910)
