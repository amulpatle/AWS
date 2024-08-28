from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "prints hello world"
    
    def handle(self,*args,**kwargs):
        #we write the logic here
        self.stdout.write('Hello wordl')