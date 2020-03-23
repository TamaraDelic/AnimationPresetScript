import maya.cmds as mc

##### GLOBAL VARIABLES #####

#GLOBAL WINDOW VARIABLES#
actionAnim = 2
fpsDesired = 24
fromFrameNum = 0
toFrameNum = 23
stepNum = 4
stepCheck = False
fpsALL = {'game' : 15, 'film' : 24, 'pal' : 25, 'ntsc' : 30, 'show' : 48, 'palf' : 50, 'ntscf' : 60}
IDLEposing = True

#GLOBAL RIG VARIABLES#
spineCount = 3
ikLegs = True  
fkLegs = True
ikArms = True
fkArms = True
thumb = True
iFace = True
includeHair = True
fingerCount = 5


#GLOBAL ANIMATION VARIABLES
loopADD = False

#GLOBAL BODY VARIABLES#
pelvis = ''
spine = ''
neck1 = ''
neck2 = ''
head = ''
hair = ''
shoulder = ''
upArm = ''
lowArm = ''
wrist = ''
thigh = ''
knee = ''
foot = ''
toes = ''
ikHand = ''
ikElbow = ''
ikFoot = ''
ikKnee = ''
thumbF = ''
finger = ''
lowEyeLid = ''
upEyeLid = ''
    

#SETING GLOBAL NAMES#
def Names():
    global fkArms, fkLegs, ikArms, ikLegs, iFace, includeHair, fingerCount
    global pelvis, spine, neck1, neck2, head, hair, shoulder, upArm, lowArm, wrist, thigh, knee, foot, toes, ikHand, ikElbow, ikFoot, ikKnee, thumbF, finger, lowEyeLid, upEyeLid
    pelvis = 'CTRL_Pelvis'
    
    #spine + num, num < spineCount
    spine = 'CTRL_Spine_'
    
    neck1 = 'CTRL_Neck_A'
    neck2 = 'CTRL_Neck_B'
    head = 'CTRL_Head'
    
    #includeHair
    #hair + '_' + num, num < hairBone
    if(includeHair):
        hair = 'CTRL_Hair'
    
    #'CTRL_' + side + shoulder
    shoulder = '_Shoulder'
    
    #FK - fkLegs, fkArms
    #'CTRL_FK_'+ side + fkPart
    if(fkArms):
        upArm = '_UpperArm'
        lowArm = '_LowerArm'
        wrist = '_Wrist'
    if(fkLegs):
        thigh = '_Thigh'
        knee = '_Knee'##mozda ne treba
        foot = '_Foot'##mozda ne treba
        toes = '_Toes'##mozda ne treba
    
    #IK - ikLegs, ikArms
    #'CTRL_' + side + ikPart
    if(ikArms):
        ikHand = '_IK_Hand'##mozda ne treba
        ikElbow = '_IK_Elbow_Twist'##mozda ne treba
    if(ikLegs):
        ikFoot = '_IK_Foot'
        ikKnee = '_IK_Knee_Twist'
    
    #thumb
    #'CTRL_' + side + thumbF + 1,2,3
    if(thumb):
        thumbF = '_Finger_Thumb_'
    
    #fingerCount (- 1 if thumb) - A, B, C, D ...
    #'CTRL_' + side + finger + A,B,C,D... + '_' + 1,2,3
    if not(thumb and (fingerCount == 1)):
        finger = '_Finger_'
    
    #'CTRL_F_' + side + lid
    if(iFace):
        lowEyeLid = '_LowerEyeLid'
        upEyeLid = '_UpperEyeLid'
    


#IDLE START POSE SETTING#    
def IDLEpose():
    global pelvis, spine, neck1, neck2, head, hair, shoulder, upArm, lowArm, wrist, thigh, knee, foot, toes, ikHand, ikElbow, ikFoot, ikKnee, thumbF, finger, lowEyeLid, upEyeLid
    global spineCount, ikLegs, fkLegs, ikArms, fkArms, thumb, iFace
    
    LEGbase = 0.607
    #new LEG
    mc.spaceLocator(n = 'p')
    mc.spaceLocator(n = 'f')
    mc.matchTransform('p', 'BN_Pelvis', position = True)
    mc.matchTransform('f', 'BN_R_Ankle', position = True)
    LEGnew = (mc.getAttr('p.translateY')) - (mc.getAttr('f.translateY'))
    mc.delete('p', 'f')
    
    #constant which allow different characters
    LEGconst = LEGnew / LEGbase
    
    
    pelvisT = [-0.006,-0.021,0]
    pelvisR = [0.862,10.618,14.491]
    mc.move(pelvisT[0]*LEGconst, pelvisT[1]*LEGconst, pelvisT[2]*LEGconst, pelvis, wd = True)
    mc.rotate(pelvisR[0],pelvisR[1],pelvisR[2], pelvis)
    
    
    spineHALF = math.floor(spineCount/2)+1
    spineHALF = str(spineHALF)
    spineHALF = spineHALF.split('.')[0]
    
    spineR = [[0,3.089,-14.044], [-0.297,-4.667,-0.347], [0,-4.56,-3.254]]
    
    mc.rotate(spineR[0][0],spineR[0][1],spineR[0][2], spine + '1')
    mc.rotate(spineR[1][0],spineR[1][1],spineR[1][2], spine + spineHALF)
    mc.rotate(spineR[2][0],spineR[2][1],spineR[2][2], spine + str(spineCount))
    
    neckR = [0.149,3.313,2.577]
    headR = [5.587,7.937,2.589]
    mc.rotate(neckR[0],neckR[1],neckR[2], neck1)
    mc.rotate(neckR[0],neckR[1],neckR[2], neck2)
    mc.rotate(headR[0],headR[1],headR[2], head)
    
    
    sides = ['L', 'R']
    
    if(ikLegs):
        if(fkLegs):
            mc.setAttr('CTRL_R_LegSwitch.R_IK', 1)
            mc.setAttr('CTRL_L_LegSwitch.L_IK', 1)
        ikFootT = [[-0.051,0,-0.005], [-0.077,0,0.069]]
        ikFootR = [[0,8.609,0], [0,0,0]]
        ikKneeT = [[0.091,0,0.044], [-0.11,0,0.103]]
        for k, side in enumerate(sides):
            mc.move(ikFootT[k][0]*LEGconst, ikFootT[k][1]*LEGconst, ikFootT[k][2]*LEGconst, 'CTRL_' + side + ikFoot, wd = True)
            mc.rotate(ikFootR[k][0],ikFootR[k][1],ikFootR[k][2], 'CTRL_' + side + ikFoot)
            mc.move(ikKneeT[k][0]*LEGconst, ikKneeT[k][1]*LEGconst, ikKneeT[k][2]*LEGconst, 'CTRL_' + side + ikKnee)
    else:
        print 'postaviti za FK noge idle pozu'
    
    shoulderR = [[0,0,-20.988],[-0.151,-0.069,8.229]]
    mc.rotate(shoulderR[k][0],shoulderR[k][1],shoulderR[k][2], 'CTRL_' + side + shoulder)
    
    if(fkArms):
        if(ikArms):
            mc.setAttr('CTRL_R_ArmSwitch.R_IK', 0)
            mc.setAttr('CTRL_L_ArmSwitch.L_IK', 0)
        upArmR = [[0,-7.371,-77.057], [-5.46,0.228,67.417]]
        lowArmR = [[17.739,-6.89,-16.601], [35.176,12.024,15.135]]
        wristR = [[6.75,3.337,1.234], [12.858,-6.904,5.545]]
        for k, side in enumerate(sides):
            mc.rotate(upArmR[k][0],upArmR[k][1],upArmR[k][2], 'CTRL_FK_'+ side + upArm)
            mc.rotate(lowArmR[k][0],lowArmR[k][1],lowArmR[k][2], 'CTRL_FK_'+ side + lowArm)
            mc.rotate(wristR[k][0],wristR[k][1],wristR[k][2], 'CTRL_FK_'+ side + wrist)
    else:
        print 'postaviti za IK ruke idle pozu'
        ############################### ------------> do not allow preset animations if there is no IK, or add IK system if there is no <---------##############################################
    
    if(thumb):
        thumbR = [[[27.875,9.928,27.85],[4.502,15.413,16.003],[-29.88,17.255,-9.496]], [[3.999,-26.379,-8.897],[3.741,-16.734,-8.196],[-9.229,-26.379,-8.897]]]
        for k, side in enumerate(sides):
            for i in range(3):
                mc.rotate(thumbR[k][i][0], thumbR[k][i][1], thumbR[k][i][2], 'CTRL_' + side + thumbF + str(i+1))
    
    
    if(iFace):
        upEyeLidT = [[0,-0.091,0], [0,-0.103,0]]
        lowEyeLidT = [[0,0.076,0], [0,0.103,0]]
        for k, side in enumerate(sides):
            mc.move(upEyeLidT[k][0], upEyeLidT[k][1], upEyeLidT[k][2], 'CTRL_F_' + side + upEyeLid)
            mc.move(lowEyeLidT[k][0], lowEyeLidT[k][1], lowEyeLidT[k][2], 'CTRL_F_' + side + lowEyeLid)
    
    print 'IDLE POSING'

#IDLE ANIMATION KEYFRAMES SETTING#
def IdleAnimation():
    if(IDLEposing):
        IDLEpose()
    global fromFrameNum, toFrameNum, loopADD
    
    HipsTtX = [0.0, 13.5, 27.0, 82.5, 110.25, 138.0, 144.0, 156.0, 168.0, 180.0, 192.0, 209.25, 217.875, 226.5, 243.75, 261.0, 288.0, 315.0, 321.0, 349.5, 363.75, 370.875, 378.0, 477.0, 500.0]
    HipsTtY = [0.0, 33.0, 48.0, 72.0, 114.0, 123.0, 177.0, 264.0, 279.0, 294.0, 318.0, 375.0, 393.0, 396.0, 453.0, 500.0]
    HipsTtZ = [0.0, 43.5, 65.25, 76.125, 87.0, 102.0, 124.5, 135.75, 147.0, 158.25, 169.5, 180.75, 192.0, 211.5, 221.25, 231.0, 252.0, 264.0, 298.5, 333.0, 339.0, 348.0, 357.0, 387.75, 403.125, 410.8125, 418.5, 433.875, 449.25, 464.625, 480.0, 490.0, 500.0]

    HipsTvX = [0.17779485881328583, 0.18752059530466797, 0.2009551344376344, -0.0735133182831529, -0.22100100769524234, -0.3282756494652284, -0.3224179744720459, -0.37428250908851624, -0.4851997196674347, -0.6094918251037598, -0.6346231698989868, -0.514301427640021, -0.4467938421003054, -0.3645054157823324, -0.2612109170295297, -0.23870888352394104, -0.355541721713962, -0.39751530008972, -0.3985836661553808, -0.43591747228390515, -0.5022106756587338, -0.5285275414912446, -0.5376094683580722, 0.3587857484817505, 0.17779485881328583]
    HipsTvY = [98.2432861328125, 98.25767124720981, 98.25446319580078, 98.26216704757125, 98.23657386504937, 98.23868560791016, 98.18712615966797, 98.29048873163418, 98.26807403564453, 98.26515831266131, 98.27314211527505, 98.18214632707156, 98.19028112825262, 98.19105529785156, 98.26376342773438, 98.2432861328125]
    HipsTvZ = [-0.4100062847137451, -0.24446356572406283, -0.023791488840410425, 0.062385208092899526, 0.06793052840914164, 0.05239826440811157, 0.14909910410642624, 0.18939124466851356, 0.21213829517364502, 0.23913892824202784, 0.323179729282856, 0.43452210584655415, 0.4574851393699646, 0.301368131759268, 0.24785943173766306, 0.24008075649641, 0.2732388474323132, 0.27188771963119507, 0.4058982297447148, 0.5125252216983912, 0.5113953351974487, 0.5283292531967163, 0.528292179107666, 0.3083632541820405, 0.0311279170564377, -0.09514799168209695, -0.21084582246839956, -0.40345653597614733, -0.51361380610615, -0.5914320640149527, -0.6361932754516602, -0.550125777721405, -0.4100062847137451]


    Rtx = [0.0, 28.5, 42.75, 49.875, 57.0, 68.25, 79.5, 90.75, 102.0, 108.0, 129.0, 139.5, 144.75, 150.0, 155.25, 160.5, 171.0, 181.5, 192.0, 231.0, 234.75, 238.5, 246.0, 263.25, 271.875, 280.5, 289.125, 297.75, 306.375, 315.0, 337.5, 343.125, 348.75, 354.375, 360.0, 400.5, 410.625, 420.75, 430.875, 441.0, 468.0, 472.0, 476.0, 484.0, 500.0]
    Rty = [0.0, 3.0, 7.875, 12.75, 22.5, 32.25, 42.0, 48.0, 52.5, 57.0, 61.5, 66.0, 69.0, 73.5, 78.0, 82.5, 87.0, 96.0, 105.0, 121.5, 138.0, 142.875, 147.75, 152.625, 155.0625, 157.5, 162.375, 167.25, 177.0, 198.75, 209.625, 220.5, 231.375, 242.25, 264.0, 270.0, 301.5, 333.0, 369.0, 375.0, 381.0, 387.0, 393.0, 399.0, 444.0, 466.5, 477.75, 489.0, 500.0]
    Rtz = [0.0, 3.0, 6.0, 15.0, 33.0, 51.0, 61.5, 72.0, 93.0, 135.0, 156.0, 177.75, 199.5, 221.25, 243.0, 271.5, 300.0, 321.0, 342.0, 363.0, 387.0, 415.25, 443.5, 471.75, 478.8125, 485.875, 500.0]
    
    Rvx = [-3.459852933883667, -3.3072674870491032, -3.176591850817203, -3.0825127395801246, -3.07987642288208, -3.22169135697186, -3.3993495255708694, -3.5094699412584305, -3.5606977939605713, -3.559291362762451, -3.692271232604981, -3.8295076936483383, -3.9137303754687323, -4.017697811126709, -4.0973897092044345, -4.128383785486221, -4.197817325592041, -4.2483763694763175, -4.316548824310303, -3.942728281021118, -3.9687414783984427, -3.9942632317543025, -3.9991328716278076, -3.926121961325408, -3.9024378501344463, -3.802559673786164, -3.720135221956298, -3.6284290980547667, -3.5285610260907556, -3.5282745361328125, -3.7624221891164775, -3.890642332611606, -4.048165224492551, -4.1375120636075735, -4.147119522094727, -3.9508220106363305, -3.8748749443329875, -3.762465771287679, -3.582578553818166, -3.5687813758850098, -3.8114373683929443, -3.749022960662842, -3.6738564968109126, -3.5961985588073726, -3.459852933883667]
    Rvy = [-5.428574085235596, -5.429776191711426, -5.464799016037511, -5.55895686494974, -5.76318071230855, -5.900301446019517, -5.919962774965807, -5.9206414222717285, -5.93696716427803, -5.921253681182861, -5.9002445936203, -5.902807235717773, -5.888182163238525, -5.8291606307029715, -5.711162567138672, -5.551192641258239, -5.371066093444824, -5.142420291900635, -5.088422775268555, -5.278287128282444, -5.358760306604535, -5.285179398731328, -5.192776870766908, -5.060915844826717, -4.985991182575158, -4.9078199565410605, -4.79939656531452, -4.7610757600463645, -4.720608084550551, -4.861498888220405, -4.939804805868713, -5.029376111924648, -5.14065934223968, -5.205549111566794, -5.209500152623212, -5.201642036437988, -5.485459406337823, -5.567963123321533, -5.215297222137451, -5.228514229129843, -5.243098384471413, -5.254955123984125, -5.243727177576302, -5.262018954740371, -5.627600338527134, -5.46442405575305, -5.368713822153452, -5.34763541845469, -5.428574085235596]
    Rvz = [-2.9911160469055176, -2.9928882122039795, -2.9908785820007324, -2.989689588546753, -3.0356638431549072, -3.068981409072876, -3.002770761332297, -2.9430974031992263, -2.763348609776853, -2.6338381805708484, -2.673411821239788, -2.584677147679032, -2.450161037634943, -2.3980438846629113, -2.362424612045288, -2.461025772027432, -2.534801226124125, -2.505805730819702, -2.6102686353303763, -2.6427693367004395, -2.5919349193573, -2.7329156929069756, -2.8143385203904536, -2.8868817113264407, -2.9342009524940953, -2.9602950462468645, -2.9911160469055176]

    ArmsRtx = [0.0, 3.0, 11.25, 19.5, 36.0, 43.5, 47.25, 51.0, 54.0, 58.5, 63.0, 75.0, 84.0, 88.5, 93.0, 102.0, 111.0, 144.0, 151.5, 155.25, 159.0, 163.5, 168.0, 171.0, 179.25, 183.375, 187.5, 191.625, 195.75, 199.875, 204.0, 220.5, 237.0, 240.0, 252.0, 269.625, 287.25, 296.0625, 304.875, 309.28125, 313.6875, 322.5, 331.3125, 335.71875, 337.921875, 340.125, 344.53125, 348.9375, 353.34375, 357.75, 393.0, 396.375, 399.75, 406.5, 413.25, 416.625, 420.0, 426.75, 433.5, 447.0, 473.5, 486.75, 500.0]
    ArmsRty = [0.0, 30.0, 55.5, 81.0, 108.0, 120.0, 141.0, 183.0, 210.0, 270.0, 348.0, 426.0, 463.0, 500.0]
    ArmsRtz = [0.0, 24.0, 42.0, 46.5, 51.0, 55.5, 60.0, 63.0, 72.0, 81.0, 94.5, 101.25, 108.0, 113.25, 118.5, 129.0, 138.0, 142.5, 147.0, 150.0, 252.0, 255.0, 264.0, 280.875, 297.75, 314.625, 323.0625, 331.5, 339.9375, 344.15625, 348.375, 356.8125, 361.03125, 365.25, 369.46875, 373.6875, 382.125, 399.0, 408.375, 417.75, 436.5, 455.25, 474.0, 500.0]
    
    ArmsRvx = [14.696393966674805, 14.683956146240234, 14.589741982519627, 14.539034843444822, 14.508481025695799, 14.573204278945921, 14.589449927210808, 14.567172050476074, 14.573321342468263, 14.613119781017305, 14.612019538879396, 14.580472946166994, 14.755029069900512, 14.90908973264694, 15.013168248176573, 15.102417178153996, 15.107366561889648, 14.980143547058105, 15.04130208492279, 15.064428016543387, 15.050728797912596, 15.01063358783722, 15.00830078125, 15.000904083251951, 14.887253042538324, 14.792230348605065, 14.64637211422682, 14.466676157440226, 14.362500167665285, 14.279128948680162, 14.181788893019707, 13.912285493060484, 13.887174606323242, 13.877899169921875, 13.866764444580067, 13.99433328050395, 14.119301445224893, 14.168557734797973, 14.275942387520162, 14.355731188232825, 14.410879196153525, 14.482654170163034, 14.63298543533977, 14.724944110488774, 14.785129346152559, 14.874119049950117, 15.02308235241596, 15.06902795045495, 15.074395629087238, 15.101098716850576, 15.285305629373527, 15.21556884337512, 15.159940492560024, 15.025511155998947, 14.836986242022569, 14.748274388239864, 14.664523022281793, 14.540925806567216, 14.506900751218026, 14.491443634033203, 14.603954076766964, 14.668143555521963, 14.696393966674805]
    ArmsRvy = [6.138768672943115, 6.160321235656738, 6.124497828423046, 6.112393379211426, 6.126261855390939, 6.121921566225887, 6.128090589804135, 6.116992473602295, 6.128780841827393, 6.09617280960083, 6.133551972930342, 6.187722664722027, 6.146836555180271, 6.138768672943115]
    ArmsRvz = [14.900257110595705, 14.989876456930611, 14.898343368557619, 14.840866263258503, 14.757704198310002, 14.709761652553368, 14.71494197845459, 14.697582244873047, 14.64612928181681, 14.663432207695275, 14.957966160545293, 15.020994551827302, 15.008961615882127, 14.973911670493544, 14.968881726264952, 14.9664312776903, 14.970444679260254, 14.943714380264284, 14.957403182983398, 14.955492019653319, 14.151723861694336, 14.146367073059082, 14.146729221427957, 14.275032481557885, 14.353107295630942, 14.49930505229019, 14.591430860072094, 14.717206958907704, 14.930823182979315, 15.029528533958906, 15.083471822860004, 15.13192010909238, 15.193725110862673, 15.28104424762414, 15.371352550050576, 15.422538384838996, 15.466372599124623, 15.509959384570992, 15.458869024417957, 15.32128171250963, 15.01405720655155, 14.893473285597622, 14.875975984025917, 14.900257110595705]

    
    allTimeLists = [HipsTtX, HipsTtY, HipsTtZ, Rtx, Rty, Rtz, ArmsRtx, ArmsRty, ArmsRtz]
    
    if(fromFrameNum != 0):
        print 'treba podesiti da krene kasnije'
        for j in range(9):
            for m, element in enumerate(allTimeLists[j]):
                allTimeLists[j][m] = element + fromFrameNum
    else:
        print 'ne treba nista na pocetku'
    
    if(toFrameNum < 500):
        print 'treba podesiti da se zavrsi ranije'
        for j in range(9):
            endTMP = 0
            for num in allTimeLists[j]:
                if(num < toFrameNum):
                    endTMP = endTMP + 1
                elif(num >= toFrameNum):
                    endTMP = endTMP + 1
                    break
            
            end = len(allTimeLists[j])
            if(end > endTMP):
                for h in range(end - endTMP):
                    allTimeLists[j].pop()
                        
    elif(toFrameNum > 500):
        print 'treba loop unapred'
        loopADD = True
    else:
        print 'ne treba nista na kraju'
    
    global pelvis, spine, neck1, neck2, head, hair, shoulder, upArm, lowArm, wrist, thigh, knee, foot, toes, ikHand, ikElbow, ikFoot, ikKnee, thumbF, finger, lowEyeLid, upEyeLid
    global spineCount, ikLegs, fkLegs, ikArms, fkArms, thumb

    mc.currentUnit(t = 'ntscf')
    ###########################################################################-------------> KAKO CE DA UTICE PROMENA FPS <----------------###############################################################
    
    
    hipsTt = [HipsTtX, HipsTtY, HipsTtZ]
    print hipsTt
    hipsTv = [HipsTvX, HipsTvY, HipsTvZ]
    axis = ['x', 'y', 'z']
    
    for i, a in enumerate(axis):
        mc.currentTime(0)
        tav = mc.getAttr(pelvis + '.t' + a)
        if(tav == 0):
            tav = 0.01
        
        difference = tav/hipsTv[i][0]
        
        for k, t in enumerate(hipsTt[i]):
            mc.currentTime(t)
            mc.setKeyframe(pelvis, attribute = 't' + a, v = hipsTv[i][k]*difference)
        
        
        
    bodyParts = [pelvis, neck1, head]
    pRt = [Rtx, Rty, Rtz]
    pRv = [Rvx, Rvy, Rvz]
    
    #pelvis, neck, head
    for p in bodyParts:
        for i, a in enumerate(axis):
            mc.currentTime(0)
            rav = mc.getAttr(p + '.r' + a)
            if(rav == 0):
                rav = 0.01
            
            difference = rav/pRv[i][0]
            
            for k, t in enumerate(pRt[i]):
                mc.currentTime(t)
                mc.setKeyframe(p, attribute = 'r' + a, v = pRv[i][k]*difference)
    #spine
    for bn in range(spineCount):
        for i, a in enumerate(axis):
            mc.currentTime(0)
            rav = mc.getAttr(spine + str(bn+1) + '.r' + a)
            if(rav == 0):
                rav = 0.01
            
            difference = rav/pRv[i][0]
            
            for k, t in enumerate(pRt[i]):
                mc.currentTime(t)
                mc.setKeyframe(spine + str(bn+1), attribute = 'r' + a, v = pRv[i][k]*difference)
    
    #Arms
    bodyParts = [shoulder, upArm, lowArm, wrist]
    ApRt = [ArmsRtx, ArmsRty, ArmsRtz]
    ApRv = [ArmsRvx, ArmsRvy, ArmsRvz]    
    axis = ['x', 'y', 'z']
    sides = ['L', 'R']
    pTMP = ''
    for side in sides:
        for p in bodyParts:
            for i, a in enumerate(axis):
                if(p == shoulder):
                    mc.currentTime(0)
                    rav = mc.getAttr('CTRL_'+ side + p + '.r' + a)
                    if(rav == 0):
                        rav = 0.01
                
                    difference = rav/ApRv[i][0]
                    for k, t in enumerate(ApRt[i]):
                        mc.currentTime(t)
                        mc.setKeyframe('CTRL_'+ side + p, attribute = 'r' + a, v = ApRv[i][k]*difference)
                else:
                    mc.currentTime(0)
                    rav = mc.getAttr('CTRL_FK_'+ side + p + '.r' + a)
                    if(rav == 0):
                        rav = 0.01
                
                    difference = rav/ApRv[i][0]
                    for k, t in enumerate(ApRt[i]):
                        mc.currentTime(t)
                        mc.setKeyframe('CTRL_FK_'+ side + p, attribute = 'r' + a, v = ApRv[i][k]*difference)
                
    

    
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

#LOOP IF NEEDED and BAKE animation#
def Bake():
    #########################################################################-------------> setting loop but not for legs <------------------#########################################################################
    
    global spineCount, fromFrameNum, toFrameNum, loopADD
    global pelvis, spine, neck1, neck2, head, shoulder, upArm, lowArm, wrist
    mc.select(pelvis, neck1, neck2, head, 'CTRL_L'+shoulder, 'CTRL_FK_L'+upArm, 'CTRL_FK_L'+lowArm, 'CTRL_FK_L'+wrist, 'CTRL_R'+shoulder, 'CTRL_FK_R'+upArm, 'CTRL_FK_R'+lowArm, 'CTRL_FK_R'+wrist)
    for i in range(spineCount):
        mc.select(spine + str(i+1), add = True)
    
    if(loopADD):
        mc.setInfinity(poi = 'cycle')
    
    mc.bakeResults(simulation = True, t = (fromFrameNum,toFrameNum), attribute = 'rotate', disableImplicitControl = True, preserveOutsideKeys = True, removeBakedAttributeFromLayer = False, removeBakedAnimFromLayer = False, bakeOnOverrideLayer = False, minimizeRotation = True)
    
    mc.select(deselect = True)
    mc.select(pelvis)
    mc.bakeResults(simulation = True, t = (fromFrameNum,toFrameNum), attribute = 'translate', disableImplicitControl = True, preserveOutsideKeys = True, removeBakedAttributeFromLayer = False, removeBakedAnimFromLayer = False, bakeOnOverrideLayer = False, minimizeRotation = True)
    
    mc.confirmDialog(title = 'Done!', message = 'Animation successfully generated!')

#GLOBAL#
def Animation():
    Names()
    global actionAnim, fpsDesired, fromFrameNum, toFrameNum, stepCheck, stepNum, fpsALL
    
    ########################################################################### ---------------> proracunati duzinu koraka i pocetne poze <------------------ ##########################################################
    
    if(actionAnim == 1):
        IdleAnimation()
    elif(actionAnim == 2):
        WalkAnimation()
    else:
        RunAnimation()
    
    Bake()
    
    mc.currentTime(fromFrameNum)

###WINDOW FUNCTIONS### SETTING PARAMETERS ###
def ApplyButton():
    global actionAnim, fpsDesired, fromFrameNum, toFrameNum, stepCheck, stepNum, fpsALL, IDLEposing
    
    selACTION = mc.radioCollection('actionCol', q = True, sl = True)
    actionALL = {'idleRadio' : 1, 'walkRadio' : 2, 'runRadio' : 3}
    actionAnim = actionALL.get(selACTION)
    
    selFPS = mc.radioCollection('fpsCol', q = True, sl = True)
    fpsDesired = fpsALL.get(selFPS)
    
    fromFrameNum = mc.intField('fromField', q = True, v = True)
    
    IDLEposing = mc.checkBox('SetStartPose', q = True, value = True)
    
    if(actionAnim == 1):
        toFrameNum = mc.intField('toField', q = True, v = True)
    else:
        stepCheck = mc.checkBox('NumberOfSteps', q = True, value = True)
        if not(stepCheck):
            toFrameNum = mc.intField('toField', q = True, v = True)
        else:
            stepNum = mc.intField('stepField', q = True, v = True)
    
    Animation()



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
    mc.checkBox('NumberOfSteps', e = True, enable = False)
    mc.intField('stepField', e = True, enable = False)
    mc.intField('toField', e = True, enable = True)
    mc.checkBox('SetStartPose', e = True, enable = True)

def WalkON():
    mc.checkBox('NumberOfSteps', e = True, enable = True)
    a = mc.checkBox('NumberOfSteps', q = True, value = True)
    if(a):
        mc.intField('stepField', e = True, enable = True)
        mc.intField('toField', e = True, enable = False)
    else:
        mc.intField('stepField', e = True, enable = False)
        mc.intField('toField', e = True, enable = True)
    mc.checkBox('SetStartPose', e = True, enable = False)

def RunON():
    mc.checkBox('NumberOfSteps', e = True, enable = True)
    a = mc.checkBox('NumberOfSteps', q = True, value = True)
    if(a):
        mc.intField('stepField', e = True, enable = True)
        mc.intField('toField', e = True, enable = False)
    else:
        mc.intField('stepField', e = True, enable = False)
        mc.intField('toField', e = True, enable = True)
    mc.checkBox('SetStartPose', e = True, enable = False)

def checkStepsON():
    mc.intField('stepField', e = True, enable = True)
    mc.intField('toField', e = True, enable = False)  

def checkStepsOFF():
    mc.intField('stepField', e = True, enable = False)
    mc.intField('toField', e = True, enable = True)

def startPoseON():
    print 'startposeON'

def startPoseOFF():
    print 'startposeOFF'

###WINDOW###
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

mc.rowColumnLayout(p = glavni, nc=4, cw = ([1,100], [2,95], [3, 104]))
mc.separator(style = 'none', h = 20)
mc.checkBox('SetStartPose', onCommand = 'startPoseON()', offCommand = 'startPoseOFF()', enable = False, value = True)
mc.checkBox('NumberOfSteps', onCommand = 'checkStepsON()', offCommand = 'checkStepsOFF()')
mc.intField('stepField', w = 25, value = 4, min = 1, enable = False)

mc.separator(p = glavni, style = 'double', h = 20)

mc.rowColumnLayout(p = glavni, nc=3, cw = ([1,115], [2, 120]))
mc.separator(style = 'none', h = 20)
mc.button(l = 'Apply', c = 'ApplyButton()')
mc.separator(style = 'none')

mc.separator(p = glavni, style = 'none', h = 10)

mc.showWindow('AnimationPreset')