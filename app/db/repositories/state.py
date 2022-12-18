from app.db.repositories.base import BaseRepository
from app.db.tables.state import state_table
from app.models.domain.state import State
from fastapi import HTTPException, status

class StateRepository(BaseRepository):
    table = state_table

    async def get_state(self) -> State:
        q = self.table.select()
        result = await self.session.execute(q)
        row = result.fetchone()

        if not row:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='В таблице нет записи.'
            )

        return row

    async def create_state(self, data: State) -> State:
        q = self.table.delete()
        await self.session.execute(q)

        q = (
            self.table.insert()
            .values(**data.dict())
            .returning(self.table)
        )
        result = await self.session.execute(q)
        row = result.fetchone()

        return row