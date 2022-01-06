import bpy
from bpy import context
import mathutils
from mathutils import Vector
import numpy

f=open('/Users/blackhole/Desktop/LEGOCODES.txt','r')
k=f.read()
l=k.split('\n')

codes=list(dict.fromkeys(l))

for number in range(len(l)):

    s=str(codes[number])

    s_object='00000_'+str(s)+'.dat'
    filepath__='/Users/blackhole/Downloads/ldraw/parts/'+str(s)+'.dat'

    bpy.ops.import_scene.importldraw(filepath=filepath__)



    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['LegoGroundPlane'].select_set(True)
    bpy.ops.object.delete() 

    bpy.ops.object.camera_add(enter_editmode=True, align='VIEW', location=(0, 0, 0), rotation=(0.991345, 1.24775e-06, -1.45211))
    bpy.context.scene.camera = bpy.data.objects['Camera']

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[s_object].select_set(True)
    bpy.data.objects['Camera'].rotation_euler[0] = 0
    bpy.data.objects['Camera'].rotation_euler[1] = 0
    bpy.data.objects['Camera'].rotation_euler[2] = 0


    bpy.ops.view3d.camera_to_view_selected()

    bpy.data.objects["Camera"].location = bpy.data.objects['Camera'].location + Vector((0,0,3))


#cube = bpy.data.objects["Camera"]
## one blender unit in x-direction
#vec = mathutils.Vector((0.0, 0.0, 3.0))
#inv = cube.matrix_world.copy()
#inv.invert()
## vec aligned to local axis
#vec_rot = (vec @ inv)
#cube.location = cube.location + vec_rot
    bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0))
    bpy.data.objects['Camera'].select_set(True)
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)



    k=0.3141592654
    piece_index=0
    for j in range(18):
        bpy.data.objects['Empty'].rotation_euler[1] = (j*k)
        for i in range(18):
            bpy.data.objects['Empty'].rotation_euler[0] = (i*k)
            bpy.context.scene.render.filepath = ('/Users/blackhole/Desktop/LegoImages/piece'+s+'_'+str(piece_index)+'.png')
            bpy.ops.render.render(write_still = True)
            piece_index=piece_index+1
            
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete() 

#bpy.data.objects[s_object].rotation_euler[0] = 0
#for i in range(36):
#    bpy.data.objects[s_object].rotation_euler[1] = (i*k)
#    bpy.context.scene.render.filepath = ('/Users/blackhole/Desktop/LegoImages/piece'+str(piece_index)+'.png')
#    bpy.ops.render.render(write_still = True)
#    piece_index=piece_index+1
#    
#bpy.data.objects[s_object].rotation_euler[1] = 0
#    
#    
#for i in range(36):
#    bpy.data.objects[s_object].rotation_euler[2] = (i*k)
#    bpy.context.scene.render.filepath = ('/Users/blackhole/Desktop/LegoImages/piece'+str(piece_index)+'.png')
#    bpy.ops.render.render(write_still = True)
#    piece_index=piece_index+1
#    
#bpy.data.objects[s_object].rotation_euler[2] = 0
