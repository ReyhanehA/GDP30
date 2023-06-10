#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_stats(steps,t_diff,dm):

  print 'steps:',steps,
  print 'time:', '{:.5f}'.format(t_diff),
  print 'vnum:', dm.get_vnum(),
  print 'enum:', dm.get_enum(),
  print 'tnum:', dm.get_tnum(),
  print 'snum:', dm.get_snum()

  return

def print_debug(dm):
  print
  print 'edges',dm.get_edges()
  print 'edges vertices',dm.get_edges_vertices()
  print 'surface edges',dm.get_surface_edges()
  print 'triangles',dm.get_triangles()
  print 'triangles edges',dm.get_triangles_edges()
  print

  return

