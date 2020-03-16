import maya.cmds as mc

actionAnim = 2
fpsDesired = 24
fromFrameNum = 0
toFrameNum = 23
stepNum = 4
stepCheck = False
fpsALL = {'game' : 15, 'film' : 24, 'pal' : 25, 'ntsc' : 30, 'show' : 48, 'palf' : 50, 'ntscf' : 60}

def IdleAnimation():
    print 'idling'
    #pelvis keyframes
    
    #foot
    
    #toes
    
    #spine
    
    #head
    
    #shoulders
    
    #upperArm
    
    #lowerArm
    
    #hands
    
    #fingers
    
def WalkAnimation():
    print 'walking'
    #pelvis keyframes
    
    #foot
    
    #toes
    
    #spine
    
    #head
    
    #shoulders
    
    #upperArm
    
    #lowerArm
    
    #hands
    
    #fingers

def RunAnimation():
    print 'running'
    #pelvis keyframes
    
    #foot
    
    #toes
    
    #spine
    
    #head
    
    #shoulders
    
    #upperArm
    
    #lowerArm
    
    #hands
    
    #fingers

def Animation():
    mc.select('lopta')
    global actionAnim, fpsDesired, fromFrameNum, toFrameNum, stepCheck, stepNum, fpsALL
    
    mc.currentTime(fromFrameNum)
    
    #proracunati duzinu koraka
    
    if(actionAnim == 1):
        IdleAnimation()
    elif(actionAnim == 2):
        WalkAnimation()
    else:
        RunAnimation()


def ApplyButton():
    global actionAnim, fpsDesired, fromFrameNum, toFrameNum, stepCheck, stepNum, fpsALL
    
    selACTION = mc.radioCollection('actionCol', q = True, sl = True)
    actionALL = {'idle' : 1, 'walk' : 2, 'run' : 3}
    actionAnim = actionALL.get(selACTION)
    
    selFPS = mc.radioCollection('fpsCol', q = True, sl = True)
    fpsDesired = fpsALL.get(selFPS)
    
    fromFrameNum = mc.intField('fromField', q = True, v = True)
    
    if(actionAnim == 1):
        toFrameNum = mc.intField('toField', q = True, v = True)
    else:
        stepCheck = mc.checkBox('Number', q = True, value = True)
        if not(stepCheck):
            toFrameNum = mc.intField('toField', q = True, v = True)
        else:
            stepNum = mc.intField('stepField', q = True, v = True)
    
    Animation()

#provera
    print actionAnim
    print fpsDesired
    print fromFrameNum
    print toFrameNum
    print stepCheck
    print stepNum

def intFieldCommand():
    global fpsALL
    intFPS = mc.intField('fpsField', q = True, value = True)
    noFPS = True
    
    for f in fpsALL.keys():
        if(fpsALL.get(f) == intFPS):
            print fpsALL.get(f)
            mc.radioCollection('fpsCol', e = True, sl = f)
            noFPS = False
        
    if(noFPS):
        print 'usao'
        mc.confirmDialog(title =  'Error', message = 'You entered unavaliable FPS rate', icon = 'error')
        mc.intField('fpsField', e = True, value = 24)
        
def RadioFPSCommand(fps):
    global fpsALL
    selFPS = mc.radioCollection('fpsCol', q = True, sl = True)
    mc.intField('fpsField', e = True, value = fpsALL.get(selFPS))

def IdleON():
    mc.checkBox('Number', e = True, enable = False)
    mc.intField('stepField', e = True, enable = False)
    mc.intField('toField', e = True, enable = True)

def WalkON():
    mc.checkBox('Number', e = True, enable = True)
    a = mc.checkBox('Number', q = True, value = True)
    if(a):
        mc.intField('stepField', e = True, enable = True)
        mc.intField('toField', e = True, enable = False)
    else:
        mc.intField('stepField', e = True, enable = False)
        mc.intField('toField', e = True, enable = True)

def RunON():
    mc.checkBox('Number', e = True, enable = True)
    a = mc.checkBox('Number', q = True, value = True)
    if(a):
        mc.intField('stepField', e = True, enable = True)
        mc.intField('toField', e = True, enable = False)
    else:
        mc.intField('stepField', e = True, enable = False)
        mc.intField('toField', e = True, enable = True)

def checkStepsON():
    mc.intField('stepField', e = True, enable = True)
    mc.intField('toField', e = True, enable = False)  

def checkStepsOFF():
    mc.intField('stepField', e = True, enable = False)
    mc.intField('toField', e = True, enable = True)



if(mc.window('AnimationPreset', q = True, exists = True)):
    mc.deleteUI('AnimationPreset')
mc.window('AnimationPreset', h = 250, w = 350, s = False)

glavni = mc.rowColumnLayout(nc=1, cw = [1,350])

mc.separator(p = glavni, style = 'none', h = 10)
mc.text(l = 'ANIMATION PRESET', h = 40)

mc.separator(p = glavni, style = 'double', h = 20)

mc.rowColumnLayout(p = glavni, nc=5, cw = ([1,55], [2, 20], [3, 100], [4,100]))
mc.text(l = 'ACTION', h = 20)
mc.separator(style = 'none', w = 10)
mc.radioCollection('actionCol')
mc.radioButton('idleRadio', label = 'Idle', onCommand = 'IdleON()')
mc.radioButton('walkRadio', label= 'Walk', onCommand = 'WalkON()', sl = True)
mc.radioButton('runRadio', label= 'Run', onCommand = 'RunON()')

mc.separator(p = glavni, style = 'double', h = 20)

mc.rowColumnLayout(p = glavni, nc=4, cw = ([1,110], [2, 40], [3,50]))
mc.separator(style = 'none')
mc.text(l = 'FPS')
mc.intField('fpsField', w = 15, v = 24, min = 15, max = 60, cc = 'intFieldCommand()')
mc.separator(style = 'none')

mc.rowColumnLayout(p = glavni, nc=5, cw = ([1,20], [2, 80], [3,80], [4,80]))
mc.radioCollection('fpsCol')
mc.separator(style = 'none')
mc.radioButton('game', l = 'Game: 15', onCommand = 'RadioFPSCommand("game")')
mc.radioButton('film', l = 'Film: 24', sl = True, onCommand = 'RadioFPSCommand("film")')
mc.radioButton('pal', l = 'Pal: 25', onCommand = 'RadioFPSCommand("pal")')
mc.radioButton('ntsc', l = 'Ntsc: 30', onCommand = 'RadioFPSCommand("ntsc")')

mc.rowColumnLayout(p = glavni, nc=5, cw = ([1,40], [2, 80], [3,80], [4,80]))
mc.separator(style = 'none')
mc.radioButton('show', l = 'Show: 48', onCommand = 'RadioFPSCommand("show")')
mc.radioButton('palf', l = 'Palf: 50', onCommand = 'RadioFPSCommand("palf")')
mc.radioButton('ntscf', l = 'Ntscf: 60', onCommand = 'RadioFPSCommand("ntscf")')
mc.separator(style = 'none')

mc.separator(style = 'none', p = glavni, h = 20)
mc.rowColumnLayout(p = glavni, nc=6, cw = ([1,70], [2, 80], [3,40], [4,20], [5, 60]))
mc.text(l = 'DURATION', h = 20)
mc.text(l = 'From Frame:')
mc.intField('fromField', value = 0)
mc.separator(style = 'none')
mc.text(l = 'To Frame:')
mc.intField('toField', value = 0, w = 40)

mc.separator(p = glavni, style = 'none', h = 10)

mc.rowColumnLayout(p = glavni, nc=4, cw = ([1,195], [2, 66], [3, 55]))
mc.separator(style = 'none', h = 20)
mc.checkBox('Number', onCommand = 'checkStepsON()', offCommand = 'checkStepsOFF()')
mc.text(l = 'of steps:')
mc.intField('stepField', w = 25, value = 4, min = 1, enable = False)

mc.separator(p = glavni, style = 'double', h = 20)

mc.rowColumnLayout(p = glavni, nc=3, cw = ([1,115], [2, 120]))
mc.separator(style = 'none', h = 20)
mc.button(l = 'Apply', c = 'ApplyButton()')
mc.separator(style = 'none')

mc.separator(p = glavni, style = 'none', h = 10)

mc.showWindow('AnimationPreset')