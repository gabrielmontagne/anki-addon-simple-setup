from aqt import gui_hooks
from subprocess import Popen

def run_simple_setup(card):
    note = card.note()

    if not 'Setup' in note: return

    setup = note['Setup']

    if not setup: return

    print('Run setup for card:', setup)

    pid = Popen(setup.split()).pid

    print('Setup pid', pid)

gui_hooks.reviewer_did_show_question.append(run_simple_setup)
