import bpy
import math

#mappings = [
#    (18, 'Snail Turn', 'bpy.data.objects["RIG-snail.001"].pose.bones["root"].rotation_euler[2]', 3.14, -3.14),
#    (26, 'Ladybug Turn', 'bpy.data.objects["RIG-ladybug"].pose.bones["root"].rotation_euler[2]', 3.14, -3.14),
#    (48, 'Butterfly Turn', 'bpy.data.objects["RIG-butterfly"].pose.bones["root"].rotation_euler[2]', 3.14, -3.14),
#    (56, 'Spider Turn', 'bpy.data.objects["RIG-spider"].pose.bones["root"].rotation_euler[2]', 3.14, -3.14),
#    
#    (19, 'Snail Walk', 'bpy.data.objects["RIG-snail.001"].pose.bones["root"].location[1]', -0.1, 0.1),
#    (27, 'Ladybug Walk', 'bpy.data.objects["RIG-ladybug"].pose.bones["root"].location[1]', -0.1, 0.1),
#    (49, 'Butterfly Walk', 'bpy.data.objects["RIG-butterfly"].pose.bones["root"].location[1]', -0.1, 0.1),
#    (57, 'Spider Walk', 'bpy.data.objects["RIG-spider"].pose.bones["root"].location[1]', -0.1, 0.1),
#]

#for cc, name, data_path, min, max in mappings:

#    m = bpy.context.scene.midi_mappings.add()
#    m.name = name
#    m.midi_cc = cc
#    m.use_note = False
#    m.use_absolute = False
#    m.smooth_speed = 1.0
#    m.easing_mode = 'LINEAR'

#    t = m.targets.add()
#    t.data_path = ( data_path )
#    t.min_value = min
#    t.max_value = max
#    t.drive_mode = 'SET'
#    t.expression = ''



#snail_wiggle_mappings = [
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg5.L"].location[1]', 'sin(time * 5) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg4.L"].location[1]', 'sin(time * 5 + 1) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg3.L"].location[1]', 'sin(time * 5 + 2) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg2.L"].location[1]', 'sin(time * 5 + 3) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg1.L"].location[1]', 'sin(time * 5 + 4) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg5.R"].location[1]', 'sin(time * 5) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg4.R"].location[1]', 'sin(time * 5 + 1) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg3.R"].location[1]', 'sin(time * 5 + 2) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg2.R"].location[1]', 'sin(time * 5 + 3) * x * .01'),
#    ('bpy.data.objects["RIG-snail.001"].pose.bones["Leg1.R"].location[1]', 'sin(time * 5 + 4) * x * .01'),
#]

#m = bpy.context.scene.midi_mappings.add()
#m.name = 'Snail Wiggle'
#m.midi_cc = 23
#m.use_note = False
#m.use_absolute = False
#m.smooth_speed = 1.0
#m.easing_mode = 'LINEAR'

#for data_path, expression in snail_wiggle_mappings:

#    t = m.targets.add()
#    t.data_path = ( data_path )
#    t.drive_mode = 'SET'
#    t.expression = expression


ladybug_wiggle_mappings = [
    ('bpy.data.objects["RIG-ladybug"].pose.bones["STR-TIP-Leg1.L"].location[1]', 'sin(time * 2) * x * .01'),
    ('bpy.data.objects["RIG-ladybug"].pose.bones["STR-TIP-Leg2.L"].location[1]', 'sin(time * 2 + 1) * x * .01'),
    ('bpy.data.objects["RIG-ladybug"].pose.bones["STR-TIP-Leg3.L"].location[1]', 'sin(time * 2 + 2) * x * .01'),

    ('bpy.data.objects["RIG-ladybug"].pose.bones["STR-TIP-Leg1.R"].location[1]', 'sin(time * 2 + 3) * x * .01'),
    ('bpy.data.objects["RIG-ladybug"].pose.bones["STR-TIP-Leg2.R"].location[1]', 'sin(time * 2 + 4) * x * .01'),
    ('bpy.data.objects["RIG-ladybug"].pose.bones["STR-TIP-Leg3.R"].location[1]', 'sin(time * 2 + 5) * x * .01'),
]

m = bpy.context.scene.midi_mappings.add()
m.name = 'Ladybug Wiggle'
m.midi_cc = 31
m.use_note = False
m.use_absolute = False
m.smooth_speed = 1.0
m.easing_mode = 'LINEAR'

for data_path, expression in ladybug_wiggle_mappings:

    t = m.targets.add()
    t.data_path = ( data_path )
    t.drive_mode = 'SET'
    t.expression = expression
