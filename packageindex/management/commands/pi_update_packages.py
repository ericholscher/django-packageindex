"""
Management command for loading all the known packages from the official
pypi.
"""

from django.core.management.base import BaseCommand
from packageindex.models import Package
from packageindex.operations.packages import update_package

class Command(BaseCommand):
    args = '<package_name package_name ...>'
    help = """Update the package index (packages only. no releases.)"""
    def handle(self, *args, **options):
        if not args:
            # update all packages! using iterator() because querysets get cahced
            # and we access files in the loop. they use a lot of ram.
            for package in Package.objects.all().iterator():
                print "updating <%s>" % package.name
                update_package(package=package, update_releases=True, 
                   update_distributions=True, mirror_distributions=False)
        for package_name in args:
            try:
                package = Package.objects.get(name=package_name)
                print "updating <%s>" % package.name
                update_package(package=package, update_releases=True, 
                   update_distributions=True, mirror_distributions=False)
            except Package.DoesNotExist:
                print "package <%s> does not exist in local database" % package_name
