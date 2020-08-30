from aqt import gui_hooks
from subprocess import run
from shlex import split

def run_simple_setup(card):
    note = card.note()

    if not 'Setup' in note: return

    setup = note['Setup']

    if not setup: return

    print('Run setup for pneq:', setup)

    run(split(setup))

gui_hooks.reviewer_did_show_question.append(run_simple_setup)
