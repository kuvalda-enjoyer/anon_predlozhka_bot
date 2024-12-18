from aiogram.fsm.state import StatesGroup, State

class SendingPost(StatesGroup):
    GET_POST = State()
    GET_CONFIRM = State()
    SEND_MEDIA_GROUP = State()
    WAITING = State()