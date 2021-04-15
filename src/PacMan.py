import pygame
import time
import random
import numpy as np                  

pygame.init()             
mult = 20
height = 31
width = 28
x = int(width*mult)
y = int(height*mult)
#screen = pygame.display.set_mode([x,y])
#screen = None
#font = pygame.font.Font(pygame.font.get_default_font(), mult)
counter = 0
mode = 0
modeCt = 0
hidden = False
speed = 1 #make this higher to control game speed
running = True
reset = False
score = 0
highScore = 0
wins = 0     
steps = 0
moveSync = 0
deaths = 0           
reflex_agent = False
nn_agent = False

#================================
def SETUP_PACMAN_AI(Setting):

    global reflex_agent
    global nn_agent
    if Setting == True:
        #reflex_agent = True
        nn_agent = True
    else:
        reflex_agent = False
        nn_agent = False
#================================

board = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,6,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,7,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,2,2,1,1,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,1,1,2,2,3,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,9,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

nodes = [1*width+1,1*width+6,1*width+12,1*width+15,1*width+21,1*width+26,
    5*width+1,5*width+6,5*width+9,5*width+12,5*width+15,5*width+18,5*width+21,5*width+26,
    8*width+1,8*width+6,8*width+9,8*width+12,8*width+15,8*width+18,8*width+21,8*width+26,
    11*width+9,11*width+12,11*width+15,11*width+18,
    14*width+6,14*width+9,14*width+18,14*width+21,
    17*width+9,17*width+18,
    20*width+1,20*width+6,20*width+9,20*width+12,20*width+15,20*width+18,20*width+21,20*width+26,
    23*width+1,23*width+3,23*width+6,23*width+9,23*width+12,23*width+15,23*width+18,23*width+21,23*width+24,23*width+26,
    26*width+1,26*width+3,26*width+6,26*width+9,26*width+12,26*width+15,26*width+18,26*width+21,26*width+24,26*width+26,
    29*width+1,29*width+12,29*width+15,29*width+26]

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    ds = s*(1-s)
    return ds

class NN:
    def __init__(self):
        self.IHWeights = np.array([[-37.643349210479464, -545.9610134040859, -24.132871617585117, -659.6795062925476, -26.589494004406735, -285.2503509175077, -374.12267151731635, -91.78463226555448, -22.02650703887688, 2.7121049810113447, -394.36672267914406, -32.31105894345988, -677.9639122410746, -208.9374774698837, -661.977128982264, -47.95419550735306, -218.5596415348124, -372.08044374560825, -24.086185087474806, -26.428658036027493],
[31.578981397350955, 28.416981327090486, 34.28113314560732, 24.226910473210953, 32.45479289549773, 34.16041559599162, 32.70977340806874, 32.92197855746428, 32.757631699912274, 35.1243433975635, 34.06965591701402, 33.43825104842917, 23.869990820779005, 33.12109715546986, 23.71836391845261, 32.56806821368766, 36.600027684134844, 34.25524649231916, 33.730029647783, 32.715712398290506],
[-36.58917706266116, -534.7126888478251, -44.988833170673104, -645.1046204201803, -35.995480076931685, -286.7929815205219, -370.5785881465467, -90.49422501983021, -39.95498043077309, -16.23461042749503, -392.8460964693813, -36.77020846288939, -663.5921835828777, -204.35203706921374, -649.3990074665808, -50.91174959818051, -222.60735750196253, -371.1250217910758, -43.57831274611513, -36.617531678697894],
[36.00665996603628, 36.78597709844814, 36.934128306578586, 34.81658179364088, 37.00781907934176, 37.25744320791995, 36.38372998916242, 36.68602284708787, 37.28900293110885, 37.96567625036182, 37.63801964447837, 36.61952988725377, 36.274135113522384, 37.6548158047686, 36.089282536153725, 36.65317270529368, 37.14181490715313, 36.27211222745393, 36.92067835087993, 36.43153606974236],
[-35.236924730193074, -527.517275723211, -31.138329121864153, -641.7429319314615, -39.89082688851362, -269.21619607823436, -357.5798010903125, -88.11067112865564, -28.162683867241324, -4.806394622133979, -378.3609534939415, -33.88621502416834, -660.3769474364107, -195.32694128130595, -644.9286525388526, -45.22156873068828, -205.64309768225982, -355.0454962165105, -31.347257016603606, -36.2537140230868],
[24.382012933568195, -17.10458459718778, 22.73752337145519, -48.24162692913809, 27.14752884344176, 12.687632694104684, 10.261219603836812, 23.15644567902442, 23.649334264602277, 33.097133148603035, 7.099432253710987, 24.566819522322536, -54.32723784670527, 19.3334687522904, -48.810161300800665, 23.16620708846553, 15.6397680003583, 8.43145886499246, 24.582910375189897, 25.381454138214185],
[28.125940116324482, 13.890121169167303, 32.15137487990144, -7.4610903982107395, 29.697906535097957, 29.062538230475724, 23.668859571395384, 28.4376635431035, 31.485378587876546, 38.63624019061835, 28.322731396919117, 30.6794161413516, -11.826691921042485, 26.56094172174207, -8.169768887604206, 29.277762563535557, 31.189160856959433, 28.367310105925487, 32.17538774714587, 28.78488804884758],
[7.67203243184383, -410.48896127510756, 14.468421677893891, -501.8645542063001, 11.192878003194219, -209.69002962161358, -277.0073622130168, -63.9805896685197, 18.575450857314394, 37.97622708888586, -293.1305320942204, 8.729945175356324, -516.8699486309113, -154.86639481470192, -504.8063640028319, -15.284629381151507, -161.79316804623704, -273.8974303833195, 15.093288405593007, 12.710047605230075],
[-40.43184583654733, -524.8104348023116, -44.1386636562282, -634.1848900325135, -39.80948374073426, -278.8254926752439, -361.44630103846254, -88.7442180543516, -47.26502588885743, -22.32144545186123, -382.4846126233803, -39.999358951165526, -652.3309450842904, -200.64545697571634, -639.0133729158877, -52.450822438476656, -215.78770464685093, -361.0891162737003, -48.191694228207965, -41.24822246717898],
[-42.39614320255246, -524.5735568145138, -47.230168137550294, -635.1333231629364, -42.24881062485576, -280.20821796385286, -361.0847262494295, -90.3121519524881, -46.088439270307376, -29.187555079160376, -383.2107623936732, -42.05371589062242, -652.5991617356018, -200.844106388083, -638.8123740271917, -53.80167401506649, -218.38091601084247, -362.9460009332385, -51.39033550562917, -42.65418909083702],
[28.55663892527563, 18.12861035211076, 28.55347817794657, 0.9484703042981971, 26.688187745886243, 27.360284049330318, 27.308053972827935, 25.591009706863304, 28.207438030360265, 33.75473542964481, 22.662309372271647, 26.644065338485206, -2.2954099795537726, 28.087690425575957, 0.5990043226678458, 27.812838356937288, 28.891790261745793, 25.660273145974347, 29.043276312637374, 28.41773483134813],
[-33.09984644442659, -543.501007754527, -25.01326579347718, -658.060728147804, -28.88525671484273, -285.6916028604622, -373.2606092211952, -93.39559913433058, -21.54317168910486, 2.8754860069031887, -397.2356010822975, -37.56011397757095, -675.8745108634222, -209.43820457901037, -660.6254617378927, -50.0207629109976, -219.76958642450413, -372.39862428813274, -24.196091559646394, -27.414911369884294],
[37.83087765126713, 37.78994113703953, 39.067111852244494, 36.953812882969096, 38.5086686270359, 38.17561998321592, 37.32162619304155, 38.15154266188482, 38.959652813301915, 39.71600253232834, 39.17722864019976, 38.827054018354865, 35.99917281528215, 37.81066200686955, 37.31149100170499, 38.08348883589701, 37.47115971721367, 38.3873688902966, 39.323439911047565, 37.564893788382484],
[25.826972411294676, -89.60229737590117, 29.132481092951654, -137.66301696616222, 27.737676349698575, -11.774329919451468, -33.22796820081671, 16.235992954566456, 31.431322640170304, 44.07139873235223, -38.009532896952294, 26.634409875754915, -146.649638336402, -3.8958068410363245, -138.7963642204305, 22.76505520255325, 1.247188891668903, -31.09149653680768, 31.380395136747545, 28.046363733844615],
[35.173897399465915, 33.69044464907333, 35.20899274131894, 34.324586965188075, 35.45258207097735, 35.845700336514355, 35.50133551860864, 35.901569124716836, 35.01317613071956, 35.23323192343291, 35.645683373554476, 35.311998544448855, 35.70632587647021, 36.25867867444478, 32.9230134401248, 35.28319839809094, 36.91220004138707, 35.73170176348647, 34.37847391611007, 35.362120479387734],
[-14.0344669316874, -465.52883309583314, -7.162163412497874, -568.0023269774895, -8.75619717852995, -240.18454546512945, -317.11503859390984, -74.23764905973785, -4.347706411520438, 19.152099387985626, -335.21237179965385, -14.855288841719716, -584.9378918576116, -175.15332796733523, -570.034981161709, -44.17615312554049, -183.60225381766006, -314.7167510608847, -6.974707930570991, -9.681790545154021],
[23.865207477822317, -66.21310473053812, 18.336329114096277, -107.56280279007602, 25.18865714269603, -6.810073548833751, -21.192152229185133, 17.481976248307685, 21.805059432067274, 30.422998961038754, -26.408726705712162, 22.88683088734062, -116.13109104971416, 4.899391342097207, -108.82932319467415, 19.711033728192156, -2.868384930344467, -22.081080656202566, 19.406443931317206, 24.23884497869193],
[26.25496818017095, 14.440383452398295, 25.23450167883727, -4.810421478036956, 27.148347557367003, 22.52892283119806, 24.831069975123267, 25.830248127121344, 24.743785106353318, 31.223216131350433, 23.110614380998424, 26.29255870666183, -8.303304382055817, 26.583254618311955, -5.6835206510300935, 25.58777628902958, 24.016975165104324, 20.886965031075817, 25.9239729532615, 26.314027294815094],
[-38.81686829634851, -529.9898991337798, -47.45441244712862, -638.4824804441923, -38.58252934289083, -283.65628896937807, -365.3957287760799, -89.187395534258, -45.583047511213934, -23.942178563572227, -388.25305558436224, -39.4933955761145, -655.8654877303833, -202.71665456308438, -642.9630149962431, -51.40135507899354, -220.6424659575754, -367.9102842718392, -51.08964218423465, -39.519147619820664],
[-35.26182930702813, -523.2638058635159, -30.917094674204485, -638.6743825375736, -37.182829990080926, -268.4943155941406, -357.0293009118661, -86.14833963545104, -29.437168045553907, -4.911271349184949, -374.9573635238772, -33.24929304816067, -656.1651340277296, -196.54942629150264, -640.455784476433, -46.67059563410434, -204.51511692212156, -352.88462905755796, -31.048895766800527, -39.34651343074162]])
        self.HOWeights = np.array([[-2.0028735553327155, 1.1295060095092428, -0.07290034486853925, 0.8305474531677579],
[34.347545361482744, 33.444847812572306, 34.021925414749035, 33.95928962101176],
[1.360707103845948, -1.3603741461702175, -0.11227256060931445, 0.31793483202690115],
[36.870980176256495, 36.92023288371638, 37.5576265186376, 37.568725775745826],
[-0.38747272614685724, 0.01973777546361416, 1.0692116347656646, 0.20311099213215422],
[24.257243254532163, 24.771409749058233, 25.51221846531245, 24.59899040744869],
[27.905870786564755, 28.722747422752974, 28.124963862932788, 28.78853092829208],
[6.8582918355783224, 6.941779572966296, 6.408295813687589, 8.225311824705301],
[-0.002810515551417647, -0.47442779923106215, 1.669206651594941, -0.27391140426906335],
[-1.1214269175355567, -0.9787600423082576, 0.8272144795763491, -1.1286449690541605],
[28.713253641898877, 29.549390485423196, 28.32082981631105, 29.997428718460192],
[-1.2123150216401077, 0.9951869737914784, -0.2603113856801893, 0.3951368392506511],
[37.15585554375075, 37.733800361091625, 38.04433252761249, 38.013495266149256],
[20.84870127116369, 20.140664952806947, 20.15216017438548, 20.480052917319362],
[36.638590891277715, 37.63697811120926, 37.65225617228433, 37.326215592265605],
[2.3173024336070296, 2.9272955576599857, 4.2896619744221915, 4.075334306855501],
[21.08491204300703, 21.905472095987037, 20.339128171478723, 22.08482137147231],
[28.4736325519689, 27.737794366893567, 28.321753339976443, 28.754334697364946],
[-0.06749470429755411, 0.6876496758114339, 1.055900980832472, -0.8069320314802418],
[-0.29265095197355356, 0.10582635627071618, 1.0151283275119156, 0.46264605900149036]])
        #self.IHWeights = np.random.rand(20,20)
        #self.HOWeights = np.random.rand(20,4)
        self.output = np.zeros(4)

    def feedForward(self, x):
        self.hiddenLayer = sigmoid(np.dot(x,self.IHWeights))
        self.output = sigmoid(np.dot(self.hiddenLayer, self.HOWeights))

    def backPropagate(self, y):
        d_HOWeights = np.dot(self.hiddenLayer.T, (2*(y - self.output) * sigmoid_derivative(self.output)))+0.01
        d_IHWeights = np.dot(self.hiddenLayer.T, (np.dot(2*(y - self.output) * sigmoid_derivative(self.output), self.HOWeights.T) * sigmoid_derivative(self.hiddenLayer)))+0.01

        self.HOWeights += d_HOWeights
        self.IHWeights += d_IHWeights

nn = NN()

dotX = 0
dotY = 0

def findDot(p5x,p5y):
    global dotX
    global dotY
    itX = random.randint(0,1)
    if itX == 0:
        itX = -1
    itY = random.randint(0,1)
    if itY == 0:
        itY = -1
    xy = random.randint(0,1)
    if xy == 0:
        for i in range(len(board[0])):
            if board[p5y][(i+p5x)%28] == 2:
                dotX = (i+p5x)%28
                dotY = p5y
                return
        for i in range(len(board)):
            if board[(i+p5y)%31][p5x] == 2:
                dotX = p5x
                dotY = (i+p5y)%31
                return
    else:
        for i in range(len(board)):
            if board[(i+p5y)%31][p5x] == 2:
                dotX = p5x
                dotY = (i+p5y)%31
                return
        for i in range(len(board[0])):
            if board[p5y][(i+p5x)%28] == 2:
                dotX = (i+p5x)%28
                dotY = p5y
                return
    jt = random.randint(0,len(board)-1)
    it = random.randint(0,len(board[jt])-1)
    cnt = 0
    while True:
        if board[jt%31][it%28] == 2:
            dotX = it%28
            dotY = it%31
            return
        it = it + 1
        jt = jt + 1
        if cnt == 28*31:
            dotY = random.randint(0,len(board)-1)
            dotX = random.randint(0,len(board[dotY]-1))
            return
class Pacman:
    def __init__(self,ch):
        self.type = ch
        if self.type == 5:
            self.pacX = 13*mult + int(mult/2)
            self.pacY = 23*mult + int(mult/2)
            self.color = (255,255,0)
            self.old = 0
            self.point = [23,13]
        elif self.type == 6:
            self.pacX = 1*mult + int(mult/2)
            self.pacY = 1*mult + int(mult/2)
            self.color = (0,255,255)
            self.old = 2
            self.point = [1,1]
        elif self.type == 7:
            self.pacX = 26*mult + int(mult/2)
            self.pacY = 1*mult + int(mult/2)
            self.color = (255,0,0)
            self.old = 2
            self.point = [1,26]
        elif self.type == 8:
            self.pacX = 1*mult + int(mult/2)
            self.pacY = 29*mult + int(mult/2)
            self.color = (255,184,255)
            self.old = 2
            self.point = [29,1]
        elif self.type == 9:
            self.pacX = 26*mult + int(mult/2)
            self.pacY = 29*mult + int(mult/2)
            self.color = (255,184,82)
            self.old = 2
            self.point = [29,26]
        self.dirX = 0
        self.dirY = 0
        self.bufX = 0
        self.bufY = 0
        self.alive = True
        self.timer = 0

    def move(self,ch):
        if ch == 0:
            self.bufX = 0
            self.bufY = -1
        elif ch == 1:
            self.bufX = -1
            self.bufY = 0
        elif ch == 2:
            self.bufX = 0
            self.bufY = 1
        elif ch == 3:
            self.bufX = 1
            self.bufY = 0

    def calcMove(self,px,py):
        x = self.pacX - px
        y = self.pacY - py
        p = random.randint(0,20)
        if p < 5:
            if x > 0:
                ch = 1
            else:
                ch = 3
        elif p < 10:
            if y > 0:
                ch = 0
            else:
                ch = 2
        else:
            ch = random.randint(0,3)
        if mode == 1:
            ch = ch + 2
            if ch > 3:
                ch = ch - 4
        self.move(ch)

    def updatePos(self, screen):
        global mode
        global modeCt
        global height
        global width
        global reset
        global score
        global wins
        global highScore  
        global nn
        global dotX
        global dotY
        global steps
        global moveSync
        global deaths
        global nn_agent
        found = False
        for i in range(0,x,mult):
            for j in range(0,y,mult):
                p = board[int(j/mult)][int(i/mult)]
                if p == self.type and not found:
                    if self.type == 5 and self.pacX % mult == int(mult/2) and self.pacY % mult == int(mult/2) and moveSync == 0:
                        p5x = -1
                        p5y = -1
                        p6x = -1
                        p6y = -1
                        p7x = -1
                        p7y = -1
                        p8x = -1
                        p8y = -1
                        p9x = -1
                        p9y = -1
                        for it in range(len(board)):
                            for jt in range(len(board[it])):
                                if board[it][jt] == 5:
                                    p5x = jt
                                    p5y = it
                                elif board[it][jt] == 6:
                                    p6x = jt
                                    p6y = it
                                elif board[it][jt] == 7:
                                    p7x = jt
                                    p7y = it
                                elif board[it][jt] == 8:
                                    p8x = jt
                                    p8y = it
                                elif board[it][jt] == 9:
                                    p9x = jt
                                    p9y = it
                        ap6x = abs(p6x-p5x)
                        ap6y = abs(p6y-p5y)
                        ap7x = abs(p7x-p5x)
                        ap7y = abs(p7y-p5y)
                        ap8x = abs(p8x-p5x)
                        ap8y = abs(p8y-p5y)
                        ap9x = abs(p9x-p5x)
                        ap9y = abs(p9y-p5y)
                        steps = steps + 1
                        if board[dotY][dotX] != 2 and board[dotY][dotX] != 3:
                            findDot(p5x,p5y)
                        arr = np.array([[board[p5y-1][p5x],board[p5y][p5x-1],board[p5y+1][p5x],board[p5y][p5x+1],p5x,p5y,p6x,p6y,p7x,p7y,p8x,p8y,p9x,p9y,dotX,dotY,score,score-0.1*steps,mode,mode==0 or modeCt>=900]])
                        for it in range(4):
                            if arr[0][it] == 1:
                                arr[0][it] = -0.5
                            elif arr[0][it] > 5:
                                arr[0][it] = -10
                                if mode == 1 and modeCt < 900:
                                    arr[0][it] = 10
                            elif arr[0][it] == 2:
                                arr[0][it] = 2
                            elif arr[0][it] == 3:
                                arr[0][it] = 5
                            else:
                                arr[0][it] = -0.2
                        nn.feedForward(arr)
                        highest = max(nn.output[0])
                        ch = -1
                        for it in range(4):
                            if nn.output[0][it] == highest:
                                ch = it
                        eps = random.random()
                        if nn_agent:
                            if eps < 0.98:
                                self.move(ch)
                            else:
                                self.move(random.randint(0,3))
                        back = np.array([[0,0,0,0]])
                        temp = np.array([[arr[0][0],arr[0][1],arr[0][2],arr[0][3]]])
                        prop = False
                        for it in range(4):
                            if temp[0][it] == max(temp[0]):
                                back[0][it] = 1
                        kt = random.randint(0,3)
                        while (sum(back[0])) > 1:
                            back[0][kt%4] = 0
                            kt = kt + 1
                        if back[0][ch] != 1:
                            nn.backPropagate(back)
                            
                    if (int(i/mult+self.bufX) < 28 and int(i/mult+self.bufX) > 0 and
                        board[int(j/mult+self.bufY)][int(i/mult+self.bufX)] != 1 and
                        self.pacX % mult == int(mult/2) and
                        self.pacY % mult == int(mult/2) and moveSync == 0):
                        if self.type == 5 or int(j/mult)*width+int(i/mult) in nodes:
                            self.dirX = self.bufX
                            self.dirY = self.bufY
                    if board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] != 1:
                        self.pacX = self.pacX + self.dirX
                        self.pacY = self.pacY + self.dirY
                        if (self.pacX % mult == int(mult/2) and
                            self.pacY % mult == int(mult/2)):
                            if self.type == 5:
                                board[int(j/mult)][int(i/mult)] = 0
                            else:
                                board[int(j/mult)][int(i/mult)] = self.old
                            self.old = board[int(j/mult+self.dirY)][int(i/mult+self.dirX)]
                            if self.old == 5 and mode == 1:
                                board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = 5
                                self.old = 0
                                self.alive = False
                            else:
                                board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = self.type
                            self.point[0] = self.point[0] + self.dirY
                            self.point[1] = self.point[1] + self.dirX
                            if self.point[1] >= 27:
                                self.point[1] = self.point[1] - 26
                            elif self.point[1] <= 0:
                                self.point[1] = self.point[1] + 26
                            if int(i/mult+self.dirX) == 27:
                                if self.type == 5:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = 0
                                else:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = self.old
                                self.old = board[int(j/mult+self.dirY)][1]
                                board[int(j/mult+self.dirY)][1] = self.type
                                self.pacX = self.pacX - 26*mult
                            elif int(i/mult+self.dirX) == 0:
                                if self.type == 5:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = 0
                                else:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = self.old
                                self.old = board[int(j/mult+self.dirY)][26]
                                board[int(j/mult+self.dirY)][26] = self.type
                                self.pacX = self.pacX + 26*mult
                    pygame.draw.circle(screen,self.color,(self.pacX,self.pacY),8)
                    if (((self.old > 4 and self.type == 5) or
                        (self.old == 5 and self.type > 4))
                        and mode == 0):
                        deaths = deaths + 1
                        arr2 = np.array([[1,1,1,1]])
                        for it in range(4):
                            if nn.output[0][it] == max(nn.output[0]):
                                arr2[0][it] = 0
                        nn.backPropagate(arr2)    
                        reset = True
                        if score > highScore:
                            highScore = score
                        score = 0
                        wins = 0
                        steps = 0                        
                        return                        
                    if not any(2 in x for x in board):
                        if reset == False:
                            wins = wins + 1
                        reset = True
                        steps = 0      
                        return
                    if self.type == 5 and self.old == 3:
                        self.old = 0
                        mode = 1
                        modeCt = 0
                        self.color = (255,255,255)
                    found = True

def updateBoard(screen):
    screen.fill((0,0,0))
    for i in range(0,x,mult):
        for j in range(0,y,mult):
            p = board[int(j/mult)][int(i/mult)]
            if p == 0:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
            elif p == 1:
                pygame.draw.rect(screen,(33,33,222),(i,j,mult-1,mult-1))
            elif p == 2:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,255),
                                   (i+int(mult/2),j+int(mult/2)),2)
            elif p == 3:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,0),
                                   (i+int(mult/2),j+int(mult/2)),4)
            elif p == 4:
                pygame.draw.rect(screen,(255,255,255),(i,j,mult-1,mult-1))

def resetBoard():
    global board
    board = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,6,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,7,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,2,2,1,1,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,1,1,2,2,3,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,9,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def countScore():
    global board
    s = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2 or board[i][j] == 3:
                s = s + 1
    return 241 - s
    
def pacmanAgent(pac,g1,g2,g3,g4):
    px = pac.point[0]
    py = pac.point[1]
    gh = [g1.pacX,g1.pacY,g2.pacX,g2.pacY,g3.pacX,g3.pacY,g4.pacX,g4.pacY]
    gp = [g1.point[0],g1.point[1],g2.point[0],g2.point[1],g3.point[0],g3.point[1],g4.point[0],g4.point[1]]
    ch = []
    if py == 0 or py == 27:
        return random.randint(0,3)
    if board[px+1][py] != 1:
        ch.append([px+1,py,2])
    if board[px-1][py] != 1:
        ch.append([px-1,py,0])
    if board[px][py+1] != 1:
        ch.append([px,py+1,3])
    if board[px][py-1] != 1:
        ch.append([px,py-1,1])
    max2 = [-1,-1]
    for i in range(len(ch)):
        min1 = 9999
        for j in range(4):
            temp = abs(ch[i][0]-gp[2*j])+abs(ch[i][1]-gp[2*j+1])
            if temp < min1:
                min1 = temp
        if min1 > max2[0] and mode == 0:
            max2[0] = min1
            max2[1] = i
    if max2[0] <= 5 and mode == 0 or modeCt > 900:
        return ch[max2[1]][2]
    ch2 = []
    if board[px+1][py] != 1 and board[px+1][py] < 4 and (board[px+1][py] == 3 or board[px+1][py] == 2):
        ch2.append([px+1,py,2])
    if board[px-1][py] != 1 and board[px-1][py] < 4 and (board[px-1][py] == 3 or board[px-1][py] == 2):
        ch2.append([px-1,py,0])
    if board[px][py+1] != 1 and board[px][py+1] < 4 and (board[px][py+1] == 3 or board[px][py+1] == 2):
        ch2.append([px,py+1,3])
    if board[px][py-1] != 1 and board[px][py-1] < 4 and (board[px][py-1] == 3 or board[px][py-1] == 2):
        ch2.append([px,py-1,1])
    if len(ch2) == 0:
        pxy = px*width+py
        if pxy in nodes:
            return random.randint(0,3)
        if pac.bufX == 1 or pac.bufY == 1:
            if pac.bufX == 1:
                return 3
            else:
                return 2
        else:
            if pac.bufX == -1:
                return 1
            else:
                return 0
    ch = random.randint(0,len(ch2)-1)
    return ch2[ch][2]
    
def PacMan_Main():

    pygame.init()
    
    global x
    global y
    global mult
    screen = pygame.display.set_mode([x,y+mult])

    updateBoard(screen)

    pacman = Pacman(5)
    inky = Pacman(6)
    blinky = Pacman(7)
    pinky = Pacman(8)
    clyde = Pacman(9)

    global running
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and reflex_agent == False:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    pacman.move(0)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pacman.move(1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pacman.move(2)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pacman.move(3)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYDOWN and reflex_agent == True:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
        #screen.fill((255,255,255))
        global counter
        counter = counter + 1
        if counter % speed == 0:
            if reflex_agent == True:
                res = pacmanAgent(pacman,inky,blinky,pinky,clyde)
                pacman.move(res)
            updateBoard(screen)
            pacman.updatePos(screen)
            inky.calcMove(pacman.pacX,pacman.pacY)
            inky.updatePos(screen)
            blinky.calcMove(pacman.pacX,pacman.pacY)
            blinky.updatePos(screen)
            pinky.calcMove(pacman.pacX,pacman.pacY)
            pinky.updatePos(screen)
            clyde.calcMove(pacman.pacX,pacman.pacY)
            clyde.updatePos(screen)
            global mode
            global modeCt
            if mode == 1:
                if modeCt == 0:
                    inky.color = (25,25,166)
                    blinky.color = (25,25,166)
                    pinky.color = (25,25,166)
                    clyde.color = (25,25,166)
                modeCt = modeCt + 1
                if modeCt > 1000:
                    mode = 0
                    modeCt = 0
                    pacman.color = (255,255,0)
                    inky.color = (0,255,255)
                    blinky.color = (255,0,0)
                    pinky.color = (255,184,255)
                    clyde.color = (255,184,82)
            global score
            global wins
            global highScore
            old = score
            score = (wins * 241) + countScore()
            if score < old:
                score = old
            outScore = "Score: " + str(score) + "     Highscore: " + str(highScore)
            font = pygame.font.SysFont('aerial', mult)
            text = font.render(outScore,True,(255,255,255))
            textRect = text.get_rect()
            textRect.center = (x/2,y+(mult/2))
            screen.blit(text,textRect)
        
            global reset
            if reset == True:
                score = 0
                reset = False
                pacman = Pacman(5)
                inky = Pacman(6)
                blinky = Pacman(7)
                pinky = Pacman(8)
                clyde = Pacman(9)
                resetBoard()
                updateBoard(screen)
        if counter > 999999999:
            counter = 0
        pygame.display.flip()

    pygame.quit()
