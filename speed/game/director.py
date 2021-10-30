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

        for i in range(0, len(self._word.get_all())):
            self._word.move_words(i, 1, 1)


        

    def _do_updates(self):
        
        self.enter10()

    def _do_outputs(self):
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._answer)
        self._output_service.draw_actors(self._word.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def enter10(self):
        word = self._answer.get_word()
        
        if '*' in word:
            new_word = word[:-1]
            #points = 5
            points = self._word.word_check(new_word)
            self._score.add_points(points)
            self._answer.reset()
            self._word._reset()