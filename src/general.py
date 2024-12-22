from enum import Enum
import pygame

TILE_WIDTH = 68                   # map tile width
TILE_HEIGHT = 56                  # map tile height
SUBTILE_WIDTH = TILE_WIDTH / 2    # map subtile (corners) width
SUBTILE_HEIGHT = TILE_HEIGHT / 2  # map subtile (corners) height

RESOURCE_PATH = "../resources"

RACE_HUMAN = 0

GENDER_MALE = 20
GENDER_FEMALE = 21

ANIMATION_IDLE_UP    = 100
ANIMATION_IDLE_RIGHT = 101
ANIMATION_IDLE_DOWN  = 102
ANIMATION_IDLE_LEFT  = 103

def saturate(value, minimum, maximum):
  if value < minimum:
    return minimum
  elif value > maximum:
    return maximum
  else:
    return value

def begins_with(what,prefix):
  return what[:len(prefix)] == prefix
