from fabric.api import local


def run_manage(command):
    local('/home/vagrant/.virtualenvs/le-code-test/bin/python /vagrant/testsite/manage.py %s' % command)

def flush():
    run_manage('flush')

def reload_sample_fixtures():
    run_manage('flush')
    run_manage('loaddata sample1')

def test():
    run_manage('test')

def web():
    run_manage('runserver 0.0.0.0:8888')

def migrate():
    run_manage('migrate')

def make_migrations():
    run_manage('makemigrations')

def requirements():
    local('/home/vagrant/.virtualenvs/le-code-test/bin/pip install -r requirements.txt ')