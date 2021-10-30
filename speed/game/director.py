from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.answer import Answer


class Director:

    def __init__(self, input_service, output_service):


        self._word = Word()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._answer = Answer()

    def start_game(self):

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):

        letter = self._input_service.get_letter()
        self._answer.update_text(letter)


        

    def _do_updates(self):
        self._word.move_words()

        if self._input_service.get_letter() == self._word.list:
            self._word.get_points()

    def _do_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._word)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()