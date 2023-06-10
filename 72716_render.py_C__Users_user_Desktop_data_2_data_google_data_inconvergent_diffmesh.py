#!/usr/bin/python
# -*- coding: utf-8 -*-

import cairo
from numpy import pi, sqrt, linspace, arctan2, cos, sin

import gtk, gobject

TWOPI = pi*2

#gtk.main()


class Render(object):

  def __init__(self,n, back, front):

    self.n = n
    self.front = front
    self.back = back

    self.__init_cairo()

    self.num_img = 0

  def clear_canvas(self):

    self.ctx.set_source_rgba(*self.back)
    self.ctx.rectangle(0,0,1,1)
    self.ctx.fill()

  def __init_cairo(self):

    sur = cairo.ImageSurface(cairo.FORMAT_ARGB32,self.n,self.n)
    ctx = cairo.Context(sur)
    ctx.scale(self.n,self.n)
    ctx.set_source_rgba(*self.back)
    ctx.rectangle(0,0,1,1)
    ctx.fill()

    self.sur = sur
    self.ctx = ctx

  def line(self,x1,y1,x2,y2):

    self.ctx.set_source_rgba(*self.front)
    self.ctx.move_to(x1,y1)
    self.ctx.line_to(x2,y2)
    self.ctx.stroke()

  def edge(self,x1,y1,x2,y2):

    ctx = self.ctx
    ctx.move_to(x1,y1)
    ctx.line_to(x2,y2)
    ctx.stroke()

  def triangle(self,x1,y1,x2,y2,x3,y3,fill=False):

    ctx = self.ctx
    ctx.move_to(x1,y1)
    ctx.line_to(x2,y2)
    ctx.line_to(x3,y3)
    ctx.close_path()

    if fill:
      ctx.fill()
    else:
      ctx.stroke()

  def circle(self,x,y,r,fill=False):

    self.ctx.arc(x,y,r,0,pi*2.)
    if fill:
      self.ctx.fill()
    else:
      self.ctx.stroke()

class Animate(Render):

  def __init__(self,n,front,back,steps_itt, step):

    Render.__init__(self, n,front,back)

    window = gtk.Window()
    window.resize(self.n, self.n)

    self.steps_itt = steps_itt
    self.step = step

    window.connect("destroy", self.__destroy)
    darea = gtk.DrawingArea()
    darea.connect("expose-event", self.expose)
    window.add(darea)
    window.show_all()

    self.darea = darea

    self.steps = 0
    gobject.idle_add(self.step_wrap)

  def __destroy(self,*args):

    gtk.main_quit(*args)

  def expose(self,*args):

    cr = self.darea.window.cairo_create()
    cr.set_source_surface(self.sur,0,0)
    cr.paint()

  def step_wrap(self):

    res = self.step(self.steps_itt,self)
    self.steps += 1
    self.expose()

    return res

