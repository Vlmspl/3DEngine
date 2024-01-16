from numba import njit
import numpy as np
import glm
import math

#  resolution
windowResolution = glm.vec2(1000, 600)

BG_COLOR = glm.vec3(0.1, 0.16, 0.25)

# camera
ASPECT_RATIO = windowResolution.x / windowResolution.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.01
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENSITIVITY = 0.002
