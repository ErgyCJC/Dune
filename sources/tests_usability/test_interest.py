from dune import *
from datetime import datetime


def test_check_play_time():
    size = 16
    game = DuneGame(size)

    start_time = datetime.now()
    game.mainloop()

    estimated_time = (datetime.now() - start_time).total_seconds()

    assert(estimated_time >= 10)