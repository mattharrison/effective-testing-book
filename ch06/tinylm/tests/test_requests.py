import pytest

@pytest.fixture(params=['value'], ids=['demo'])
def demo_fixture(request):
    print(f'{request=}')
    print(f'{request.node=}')
    for attr in ['name', 'cls', 'module']:
        print(f' {attr}={getattr(request.node, attr)}')
    print(f'{request.function=}')
    print(f'{request.cls=}')
    print(f'{request.module=}')
    print(f'{request.fspath=}')
    print(f'{request.scope=}')
    print(f'{request.param=}')

def test_requests_example(demo_fixture, request):
    assert request.node.name == 'test_requests_example[demo]'
