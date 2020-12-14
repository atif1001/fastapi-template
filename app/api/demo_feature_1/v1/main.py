from fastapi import APIRouter

router = APIRouter()

data = [
    {
        'id': 0,
        'name': 'abc'
    },
    {
        'id': 1,
        'name': 'def'
    }
]


@router.get('/demo-feature-1')
async def list():
    return data


@router.post('/demo-feature-1')
async def create():
    return data


@router.get('/demo-feature-1/{id}')
async def read():
    return data


@router.put('/demo-feature-1/{id}')
async def update():
    return data


@router.delete('/demo-feature-1/{id}')
async def delete():
    return data
