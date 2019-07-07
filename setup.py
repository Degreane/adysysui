from setuptools import setup

setup(
        name="AdySysPageBuilder",
        version="0.1",
        url="https://github.com/Degreane/AdySysPageBuilder",
        author="Faysal Al-Banna",
        author_email="degreane@gmail.com",
        description="WebSafe PageBuilder Supporting Old Browsers",
        requires=['sanic','sanic_session','lxml','pyquery'],
        provides=['adysys'],
        zip_safe=False,
)