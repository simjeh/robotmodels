from math import sqrt
from math import sin
from math import cos
from math import acos
from math import asin
import numpy as np
import os

class jd_off:
    """urdf generation parameter creation for multiple list.
    """
    def __init__(self) -> None:
        """initiallize variable with 9*3 array
        """
        self.CY_x=0.0
        self.CY_y=0.0
        self.CY_z=0.0
        self.SP_x=0.0
        self.SP_y=0.0
        self.SP_z=0.0
        self.SR_x=0.0
        self.SR_y=0.0
        self.SR_z=0.0
        self.UP_x=0.0
        self.UP_y=0.0
        self.UP_z=0.0
        self.ER_x=0.0
        self.ER_y=0.0
        self.ER_z=0.0
        self.LP_x=0.0
        self.LP_y=0.0
        self.LP_z=0.0
        self.WR_x=0.0
        self.WR_y=0.0
        self.WR_z=0.0
        self.WY_x=0.0
        self.WY_y=0.0
        self.WY_z=0.0
        self.EE_x=0.0
        self.EE_y=0.0
        self.EE_z=0.0
        self.jd=np.zeros((9,3))
    def set(self):
        """set parameter with its member variable. Could we erase this function?
        """
        self.jd[0]=[self.CY_x,self.CY_y,self.CY_z]
        self.jd[1]=[self.SP_x,self.SP_y,self.SP_z]
        self.jd[2]=[self.SR_x,self.SR_y,self.SR_z]
        self.jd[3]=[self.UP_x,self.UP_y,self.UP_z]
        self.jd[4]=[self.ER_x,self.ER_y,self.ER_z]
        self.jd[5]=[self.LP_x,self.LP_y,self.LP_z]
        self.jd[6]=[self.WR_x,self.WR_y,self.WR_z]
        self.jd[7]=[self.WY_x,self.WY_y,self.WY_z]
        self.jd[8]=[self.EE_x,self.EE_y,self.EE_z]


jd_off_default= jd_off().jd 


def generate_humanoid(dir,jd_off=jd_off_default):
    """urdf generation based on TOCABI config.

    Args:
        dir (path): saving path for urdf ex)"c://repos/resource/urdf"
        jd_off (optional): joint config parameter list. Defaults is np.zeros((9,3)) 
                        ex)[[pos_x,pos_y,pos_z],...] 
                            [[0.0,0.0,0.1],...]
    """
    file_name = os.path.join(dir, 'test.urdf')  # the name of urdf file
    f=open(file_name, mode='w')
    #linkname , link size, link offset from link origin
   # parent, child, type, axis x, axis y, axis z, joint position from link origin
    jd=[['world','P','fixed',0.0,0.0,0.0,0.11,0.0,0.0],
    ['P','B1','revolute',0.0,0.0,1.0,0.0,0.0,0.1979],['B1','B2','revolute',0.0,-1.0,0.0,0.0,0.0,0.0],['B2','B3','revolute',1.0,0.0,0.0,0.0,0.0,0.0],
    # ['P','B1','fixed',0.0,0.0,1.0,0.0,0.0,0.1979],['B1','B2','fixed',0.0,-1.0,0.0,0.0,0.0,0.0],['B2','B3','fixed',1.0,0.0,0.0,0.0,0.0,0.0],
    
    ['B3','LA1','revolute',0.0,0.0,1.0,0.023,0.154,0.2925],['LA1','LA2','revolute',0.0,-1.0,0.0,0.0,0.1491,0.0],['LA2','LA3','revolute',1.0,0.0,0.0,0.0,0.0,0.0],
    ['LA3','LA4','revolute',0.0,-1.0,0.0,0.0,0.0,0.0],['LA4','LA5','revolute',-1.0,0.0,0.0,0.0,0.3351,-0.0325],['LA5','LA6','revolute',0.0,-1.0,0.0,0.0,0.2688,0.0325],
    ['LA6','LA7','revolute',1.0,0.0,0.0,0.0,0.0,0.0],['LA7','LA8','revolute',0.0,0.0,-1.0,0.0,0.048,0.0],['LA8','LAE','fixed',0.0,0.0,0.0,0.0,0.0375,0.0],
    
    ['B3','RA1','revolute',0.0,0.0,1.0,0.023,-0.154,0.2925],['RA1','RA2','revolute',0.0,-1.0,0.0,0.0,-0.1491,0.0],['RA2','RA3','revolute',1.0,0.0,0.0,0.0,0.0,0.0],
    ['RA3','RA4','revolute',0.0,1.0,0.0,0.0,0.0,0.0],['RA4','RA5','revolute',1.0,0.0,0.0,0.0,-0.3351,-0.0325],['RA5','RA6','revolute',0.0,1.0,0.0,0.0,-0.2688,0.0325],
    ['RA6','RA7','revolute',1.0,0.0,0.0,0.0,0.0,0.0],['RA7','RA8','revolute',0.0,0.0,1.0,0.0,-0.048,0.0],['RA8','RAE','fixed',0.0,0.0,0.0,0.0,-0.0375,0.0],
    
    ['B3','T1','revolute',0.0,0.0,1.0,-0.036,0.0,0.407],['T1','T2','revolute',0.0,-1.0,0.0,0.0,0.0,0.0],
    ['P','LL1','revolute',0.0,0.0,1.0,0.11,0.1025,-0.01],['LL1','LL2','revolute',1.0,0.0,0.0,0.0,0.0,-0.0924],['LL2','LL3','revolute',0.0,-1.0,0.0,0.0,0.0,0.0],['LL3','LL4','revolute',0.0,-1.0,0.0,0.0,0.0,-0.35],['LL4','LL5','revolute',0.0,-1.0,0.0,0.0,0.0,-0.35],['LL5','LLE','revolute',1.0,0.0,0.0,0.0,0.0,0.0],
    ['P','RL1','revolute',0.0,0.0,1.0,0.11,-0.1025,-0.01],['RL1','RL2','revolute',1.0,0.0,0.0,0.0,0.0,-0.0924],['RL2','RL3','revolute',0.0,-1.0,0.0,0.0,0.0,0.0],['RL3','RL4','revolute',0.0,-1.0,0.0,0.0,0.0,-0.35],['RL4','RL5','revolute',0.0,-1.0,0.0,0.0,0.0,-0.35],['RL5','RLE','revolute',1.0,0.0,0.0,0.0,0.0,0.0]
    ]

    rd=[['world',0.0,0.0,0.0,0.0,0.0,0.0],
    ['P',0.11,0.0,0.0,0.0,0.0,0.0],['B1',0.0,0.0,-0.1979,0.0,0.0,0.0],['B2',0.0,0.0,0.0,0.0,0.0,0.0],['B3',0.023,0.0,0.2925,0.0,0.0,0.0],
    ['LA1',0.0,0.1,0.0,0.0,-0.05,0.0],['LA2',0.0,-0.1491,0.0,0.0,0.0,0.0],['LA3',jd[7][6]+jd_off[3][0],jd[7][7]+jd_off[3][1],jd[7][8]+jd_off[3][2],0.0,0.06,0.0],['LA4',jd[8][6]+jd_off[4][0],jd[8][7]+jd_off[4][1],jd[8][8]+jd_off[4][2],0.0,0.0,0.0],['LA5',jd[9][6]+jd_off[5][0],jd[9][7]+jd_off[5][1],jd[9][8]+jd_off[5][2],0.0,0.0,0.0],['LA6',0.0,0.01,0.0,0.0,0.0,0.0],['LA7',jd[11][6]+jd_off[7][0],jd[11][7]+jd_off[7][1],jd[11][8]+jd_off[7][2],0.0,0.0,0.0],['LA8',0.0,0.0375,0.0,0.0,0.0,0.0],['LAE',0.0,0.1,0.0,0.0,0.0,0.0],
    ['RA1',0.0,-0.1,0.0,0.0,0.05,0.0],['RA2',0.0,0.1491,0.0,0.0,0.0,0.0],['RA3',jd[16][6]+jd_off[3][0],jd[16][7]-jd_off[3][1],jd[16][8]+jd_off[3][2],0.0,-0.06,0.0],['RA4',jd[17][6]+jd_off[4][0],jd[17][7]-jd_off[4][1],jd[17][8]+jd_off[4][2],0.0,0.0,0.0],['RA5',jd[18][6]+jd_off[5][0],jd[18][7]-jd_off[5][1],jd[18][8]+jd_off[5][2],0.0,0.0,0.0],['RA6',0.0,-0.01,0.0,0.0,0.0,0.0],['RA7',jd[20][6]+jd_off[7][0],jd[20][7]-jd_off[7][1],jd[20][8]+jd_off[7][2],0.0,0.0,0.0],['RA8',0.0,-0.0375,0.0,0.0,0.0,0.0],['RAE',0.0,-0.1,0.0,0.0,0.0,0.0],
    ['T1',0.0,0.0,-0.2,0.0,0.0,0.0],['T2',0.1,0.0,0.0,0.0,0.0,0.1],
    ['LL1',0.0,0.0,-0.0924,0.0,0.0,0.0],['LL2',0.0,0.0,-0.01,0.0,0.0,0.0],['LL3',0.0,0.0,-0.35,0.0,0.0,0.0],['LL4',0.0,0.0,-0.35,0.0,0.0,0.0],['LL5',0.0,0.0,-0.01,0.0,0.0,0.0],['LLE',0.2,0.0,0.0,0.0,0.0,0.0],
    ['RL1',0.0,0.0,-0.0924,0.0,0.0,0.0],['RL2',0.0,0.0,-0.01,0.0,0.0,0.0],['RL3',0.0,0.0,-0.35,0.0,0.0,0.0],['RL4',0.0,0.0,-0.35,0.0,0.0,0.0],['RL5',0.0,0.0,-0.01,0.0,0.0,0.0],['RLE',0.2,0.0,0.0,0.0,0.0,0.0]
    ]

    #joint offset !!! change this variable for deform tocabi
    # parent, axis offset, joint position offset.

    f.write('<?xml version="1.0" ?>\n')
    f.write('<robot name="test_robot">\n\n')
    f.write('<material name="silver">\n')
    f.write('  <color rgba="0.700 0.700 0.700 1.000"/>\n')
    f.write('</material>\n\n')

    for i in range(0,37): 
        #print(rd[i][0])
        f.write(f'<link name="{rd[i][0]}">\n')
        f.write('  <inertial>\n')
        f.write('    <origin rpy="0 0 0" xyz="0 0 0"/>\n')
        f.write('    <mass value="0.1"/>\n')
        f.write('    <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/>\n')
        f.write('  </inertial>\n')
        f.write('  <visual>\n')

        tl=sqrt(rd[i][1]*rd[i][1]+rd[i][2]*rd[i][2]+rd[i][3]*rd[i][3])+0.00001
        temp2=asin(rd[i][1]/tl)
        temp1=asin(-rd[i][2]/tl)
        if rd[i][3]<0: temp1=-temp1
        
        f.write(f'    <origin rpy="{temp1} {temp2} {0}" xyz="{rd[i][1]/2.0+rd[i][4]} {rd[i][2]/2.0+rd[i][5]} {rd[i][3]/2.0+rd[i][6]}"/>\n')
        f.write('    <geometry>\n')
        f.write(f'      <cylinder length="{tl}" radius="0.05"/>\n')
        f.write('    </geometry>\n')
        # f.write('    <material name="silver"/>\n')
        f.write('  </visual>\n')
        f.write('</link>\n\n')
    for i in range(0,4): 
        f.write(f'<joint name="J{jd[i][1]}" type="{jd[i][2]}">\n')
        f.write(f'  <origin rpy="0 0 0" xyz="{jd[i][6]} {jd[i][7]} {jd[i][8]}"/>\n')
        
        f.write(f'  <parent link="{jd[i][0]}"/>\n')
        f.write(f'  <child link="{jd[i][1]}"/>\n')
        f.write(f'  <axis xyz="{jd[i][3]} {jd[i][4]} {jd[i][5]}"/>\n')

        f.write(f'  <limit effort="100" lower= "-3.14" upper="3.14" velocity="100"/>\n')
        # f.write(f'  <limit effort="100" lower= "-0.01" upper="0.01" velocity="100"/>\n')
        f.write('</joint>\n\n')   
    for i in range(4,13): 
        f.write(f'<joint name="J{jd[i][1]}" type="{jd[i][2]}">\n')
        f.write(f'  <origin rpy="0 0 0" xyz="{jd[i][6]+jd_off[i-4][0]} {jd[i][7]+jd_off[i-4][1]} {jd[i][8]+jd_off[i-4][2]}"/>\n')
        
        f.write(f'  <parent link="{jd[i][0]}"/>\n')
        f.write(f'  <child link="{jd[i][1]}"/>\n')
        f.write(f'  <axis xyz="{jd[i][3]} {jd[i][4]} {jd[i][5]}"/>\n')

        f.write(f'  <limit effort="100" lower= "-6.14" upper="6.14" velocity="100"/>\n')
        f.write('</joint>\n\n') 
    for i in range(13,22): 
        f.write(f'<joint name="J{jd[i][1]}" type="{jd[i][2]}">\n')
        f.write(f'  <origin rpy="0 0 0" xyz="{jd[i][6]+jd_off[i-13][0]} {jd[i][7]-jd_off[i-13][1]} {jd[i][8]+jd_off[i-13][2]}"/>\n')
        
        f.write(f'  <parent link="{jd[i][0]}"/>\n')
        f.write(f'  <child link="{jd[i][1]}"/>\n')
        f.write(f'  <axis xyz="{jd[i][3]} {jd[i][4]} {jd[i][5]}"/>\n')

        f.write(f'  <limit effort="100" lower= "-6.14" upper="6.14" velocity="100"/>\n')
        f.write('</joint>\n\n') 
    for i in range(22,36): 
        f.write(f'<joint name="J{jd[i][1]}" type="{jd[i][2]}">\n')
        f.write(f'  <origin rpy="0 0 0" xyz="{jd[i][6]} {jd[i][7]} {jd[i][8]}"/>\n')
        
        f.write(f'  <parent link="{jd[i][0]}"/>\n')
        f.write(f'  <child link="{jd[i][1]}"/>\n')
        f.write(f'  <axis xyz="{jd[i][3]} {jd[i][4]} {jd[i][5]}"/>\n')

        f.write(f'  <limit effort="100" lower= "-3.14" upper="3.14" velocity="100"/>\n')
        f.write('</joint>\n\n') 
    f.write('</robot>\n')
    return os.path.basename(file_name)

