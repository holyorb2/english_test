#!/usr/bin/env python3
import random
import os
from gi.repository import Gtk

class MyWindow(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="Hello World")
    self.set_border_width(10)

    self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    self.add(self.box)

    self.l_stats = Gtk.Label("")
    self.box.pack_start(self.l_stats, True, True, 0)

    self.l_result = Gtk.Label("")
    self.box.pack_start(self.l_result, True, True, 0)

    self.l_quest = Gtk.Label("")
    self.box.pack_start(self.l_quest, True, True, 0)

    hbox_answer = Gtk.Box(spacing=10)

    self.entry = Gtk.Entry()
    self.entry.set_text("")
    hbox_answer.pack_start(self.entry, True, True, 0)

    self.send = Gtk.Button(label="Send")
    self.send.connect("clicked", self.on_send_clicked)
    hbox_answer.pack_start(self.send, True, True, 0)

    self.box.pack_start(hbox_answer, True, True, 0)

    # data variables
    self.i_right = 0
    self.i_err = 0
    self.curr_question = 0
    self.answer = ''
    self.dic = []
    for str in open(os.path.dirname(__file__) + '/db/dic.txt'):
      line = str.split('#')
      if len(line) == 2:
        self.dic.append([line[0].strip(), line[1].strip()])
    self.count_dic = len(self.dic)

  def on_send_clicked(self, widget):
    self.answer = self.entry.get_text()
    self.entry.set_text('')
    self.update_status()
    
  def update_status(self):
    all_answer = self.i_right + self.i_err
    if all_answer == 0 and self.answer == '':
      status = ''
      last = ''
    else:
      last = self.dic[self.curr_question][0]
      if self.answer.lower() == self.dic[self.curr_question][1].lower():
        self.i_right += 1
        status = 'OK'
      else:
        self.i_err += 1
        status = self.dic[self.curr_question][1]

    self.l_result.set_text('Last:\n{0} ({5})\n{1}\n\nAll answer - {2}\nError - {3}\nRight - {4}'.format(last, status, all_answer, self.i_err, self.i_right, self.curr_question))

    self.curr_question = random.randint(0, self.count_dic)
    self.l_quest.set_text('{0}'.format(self.dic[self.curr_question][0]))


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

win.l_stats.set_text('Top result: 20.06.2015 - 0/0\n\nCount of questions: {0}\n'.format(win.count_dic))
win.update_status()

Gtk.main()
