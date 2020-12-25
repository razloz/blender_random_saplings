import bpy
from random import uniform as rFloat
from random import randint as rInt

rMode = ('original', 'rotate', 'random')

geometry = {
    'bevel': True,
    'bevelRes': 1,
    'resU': 1,
    'handleType': '0',
    'shape': str(rInt(1, 10)),
    'shapeS': str(rInt(1, 9)),
    'customShape': (rFloat(0.01, 1.0), rFloat(0.01, 1.0),
                    rFloat(0.01, 1.0), rFloat(0.01, 1.0)),
    'branchDist': rFloat(0.1, 10.0),
    'nrings': rInt(0, 34),
    'seed': rInt(-5000, 5000),
    'scale': rInt(1, 20),
    'scaleV': rInt(1, 5),
    'do_update': True,
    'chooseSet': '3'
    }

branch_radius = {
    'ratio': rFloat(0.001, 0.05),
    'scale0': rFloat(0.25, 1.25),
    'scaleV0': rFloat(0.1, 1.0),
    'ratioPower': rFloat(1.0, 2.0),
    'minRadius': 0.001,
    'closeTip': False,
    'rootFlare': rInt(1, 5),
    'autoTaper': True,
    'taper': (rFloat(0, 1), rFloat(0, 1), rFloat(0, 1), rFloat(0, 1)),
    'radiusTweak': (rFloat(0, 1), rFloat(0, 1), rFloat(0, 1), rFloat(0, 1))
    }

branch_splitting = {
    'levels': rInt(1, 5),
    'baseSplits': rInt(1, 10),
    'baseSize': rFloat(0, 1),
    'baseSize_s': rFloat(0, 1),
    'splitHeight': rFloat(0, 1),
    'splitBias': rFloat(-2, 2),
    'splitByLen': True,
    'branches': (rInt(1, 34), rInt(1, 34), rInt(1, 34), rInt(1, 34)),
    'segSplits': (rFloat(0, 1), rFloat(0, 1), rFloat(0, 1), rFloat(0, 1)),
    'splitAngle': (rFloat(0, 15), rFloat(0, 15), rFloat(0, 15), rFloat(0, 15)),
    'splitAngleV': (rFloat(0, 15), rFloat(0, 15), rFloat(0, 15), rFloat(0, 15)),
    'rotate': (rFloat(0, 15), rFloat(0, 15), rFloat(0, 15), rFloat(0, 15)),
    'rotateV': (rFloat(0, 15), rFloat(0, 15), rFloat(0, 15), rFloat(0, 15)),
    'attractOut': (rFloat(0, 1), rFloat(0, 1), rFloat(0, 1), rFloat(0, 1)),
    'rMode': rMode[rInt(0, 2)],
    'curveRes': (rInt(1, 16), rInt(1, 8), rInt(1, 4), rInt(1, 2))
    }

branch_growth = {
    'taperCrown': rFloat(0, 1),
    'length': (rFloat(0, 5), rFloat(0, 5), rFloat(0, 5), rFloat(0, 5)),
    'lengthV': (rFloat(0, 1), rFloat(0, 1), rFloat(0, 1), rFloat(0, 1)),
    'downAngle': (rFloat(0, 45), rFloat(0, 45), rFloat(0, 45), rFloat(0, 45)),
    'downAngleV': (rFloat(0, 90), rFloat(0, 90), rFloat(0, 90), rFloat(0, 90)),
    'curve': (rFloat(-30, 30), rFloat(-30, 30), rFloat(-30, 30), rFloat(-30, 30)),
    'curveV': (rFloat(0, 90), rFloat(0, 90), rFloat(0, 90), rFloat(0, 90)),
    'curveBack': (rFloat(-30, 30), rFloat(-30, 30), rFloat(-30, 30), rFloat(-30, 30)),
    'attractUp': (rFloat(-1, 2), rFloat(-1, 2), rFloat(-1, 2), rFloat(-1, 2)),
    'useOldDownAngle': True,
    'useParentAngle': True
    }

pruning = {
    'prune': True if rInt(0, 1) == 1 else False,
    'pruneRatio': rFloat(0, 1),
    'pruneWidth': rFloat(0.1, 1),
    'pruneBase': rFloat(0.1, 1),
    'pruneWidthPeak': rFloat(0.1, 1),
    'prunePowerHigh': rFloat(0.1, 1),
    'prunePowerLow': rFloat(0.001, 0.1)
    }

leaves = {
    'showLeaves': True,
    'leafShape': 'hex',
    'leaves': rInt(0, 500),
    'leafDist': str(rInt(1, 9)),
    'leafDownAngle': rFloat(-360, 360),
    'leafDownAngleV': rFloat(-360, 360),
    'leafRotate': rFloat(-360, 360),
    'leafRotateV': rFloat(-360, 360),
    'leafScale': rFloat(0.1, 1),
    'leafScaleX': rFloat(0.1, 1),
    'leafScaleT': rFloat(0.1, 1),
    'leafScaleV': rFloat(0.1, 1),
    'horzLeaves': True,
    'leafangle': rFloat(-360, 360)
    }

armature = {
    'useArm': False,
    'makeMesh': False,
    'armLevels': 2,
    'boneStep': (1, 1, 1, 1)
    }

animation = {
    'armAnim': False,
    'leafAnim': False,
    'previewArm': False,
    'frameRate': 1,
    'loopFrames': 0,
    'wind': 1,
    'gust': 1,
    'gustF': 0.075,
    'af1': 1,
    'af2': 1,
    'af3': 4
    }

bpy.ops.curve.tree_add(
    **geometry,
    **branch_radius,
    **branch_splitting,
    **branch_growth,
    **pruning,
    **leaves,
    **armature,
    **animation
    )
