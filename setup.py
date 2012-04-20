from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='toutpt.commons',
      version=version,
      description="Commons addons used in Plone projects",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['toutpt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.addthis',
          'collective.ckeditor',
          'collective.portlet.oembed',
          'collective.galleria',
          'collective.masonry',
          'collective.seo',
          'Products.PloneFormGen',
          'webcouturier.dropdownmenu',
          # -*- Extra requirements: -*-
      ],
      extras_require = dict(
          tests=['plone.app.testing'],
      ),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
