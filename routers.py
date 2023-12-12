from fastapi import APIRouter
from fastapi import Response, Request, HTTPException
from fastapi import jsonable_encoder
from schemas import Todo, TodoBody
from database import create_todo_table
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

router = APIRouter()


@router.poste("/api/todo", response_model=Todo)
async def create_todo(request: Request, response: Response, data: TodoBody):
    todo = jsonable_encoder(data)
    res = await create_todo_table(todo)
    response.status_code = HTTP_201_CREATED
    if res:
        return res
    return HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail="Create task failed",
    )
