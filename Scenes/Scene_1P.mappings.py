import bpy
import math

mappings = [
    (18, 'Snail Turn', 'bpy.data.objects["RIG-snail.001"].pose.bones["root"].rotation_euler[2]', 180, -180),
    (26, 'Ladybug Turn', 'bpy.data.objects["RIG-ladybug"].pose.bones["root"].rotation_euler[2]', 180, -180),
    (48, 'Butterfly Turn', 'bpy.data.objects["RIG-butterfly"].pose.bones["root"].rotation_euler[2]', 180, -180),
    (56, 'Spider Turn', 'bpy.data.objects["RIG-spider"].pose.bones["root"].rotation_euler[2]', 180, -180),
]

for cc, name, data_path, min_deg, max_deg in mappings:

    m = bpy.context.scene.midi_mappings.add()
    m.name = name
    m.midi_cc = cc
    m.use_note = False
    m.use_absolute = False
    m.smooth_speed = 1.0
    m.easing_mode = 'LINEAR'

    t = m.targets.add()
    t.data_path = ( data_path )
    t.min_value = math.radians(min_deg)
    t.max_value = math.radians(max_deg)
    t.drive_mode = 'SET'
    t.expression = ''

