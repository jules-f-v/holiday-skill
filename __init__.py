from mycroft import MycroftSkill, intent_file_handler


class Holiday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('holiday.intent')
    def handle_holiday(self, message):
        self.speak_dialog('holiday')


def create_skill():
    return Holiday()

