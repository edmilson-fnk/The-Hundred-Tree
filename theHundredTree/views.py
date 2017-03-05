from pyramid.view import view_config
from theHundredTree.app import builder
from theHundredTree.app import node

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'theHundredTree'}


@view_config(route_name='tree', renderer='templates/mytemplate.jinja2')
def tree_view(request):
    min = int(request.POST['min'])
    max = int(request.POST['max'])
    sum = int(request.POST['sum'])
    
    errors = builder.validate(min, max, sum)
    if (not errors):
        root = builder.buildTemplate(min, max)
        root.getPossibilities(sum, ['',' - ',' + '])
        return {'list': root.expressions, 'sum': sum}
    else:
        return {'errors': errors}
    