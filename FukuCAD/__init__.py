import bpy
import tool_test as tool
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "FukuCAD",
    "author": "Tokushi-2000",
    "description": "",
    "blender": (3, 0, 1),
    "version": (0, 0, 1),
    "location": "3D View",
    "warning": "",
    "suport": "TESTING",
    "category": "Generic",
    "doc_url": "https://github.com/TOKUSHI-2000/FukuCAD/tree/main",
}


class AddSketchOperator(bpy.types.Operator):
    bl_idname = "object.addsketch"
    bl_label = "AddSketch"
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0  # type: ignore

        # Lets Blender know the operator finished successfully.
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(AddSketchOperator.bl_idname)


def register():
    bpy.utils.register_class(AddSketchOperator)
    # Adds the new operator to an existing menu.
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(AddSketchOperator)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
    tool.register()
