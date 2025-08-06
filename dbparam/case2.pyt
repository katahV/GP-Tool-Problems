import json
import os

import arcpy


class Toolbox(object):

    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "Test with absolute paths"

        # List of tool classes associated with this toolbox
        self.tools = [ToolA]


class ToolA(object):
    DEFAULT_CONFIG = {
        "db-sde": "C:\\PRJ\\GP-Tool-Problems\\data\\sql-cases.sde",
        "db-gdb": "C:\\PRJ\\GP-Tool-Problems\\data\\cases.gdb"
    }

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Case 2"
        self.description = "Test with absolute paths"
        self.canRunInBackground = False

        config = self._read_configfile()
        self.config = dict(self.DEFAULT_CONFIG)
        self.config.update(config)  # does not work with arcmap

    @staticmethod
    def _read_configfile():
        try:
            configfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'case2.json')
            with open(configfile, 'r') as f:
                return json.loads(f.read())
        except Exception as e:
            arcpy.AddError('Failed reading config file. {0}'.format(e))
            return e

    def getParameterInfo(self):
        """Define parameter definitions
        handles the parameters from the Toolboxwindow

        :keyword: https://desktop.arcgis.com/en/arcmap/10.7/analyze/creating-tools/defining-parameters-in-a-python-toolbox.htm

        """
        params = []
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        arcpy.AddMessage(f"Workspace: {arcpy.env.workspace}")
        arcpy.AddMessage(f"packageWorkspace: {arcpy.env.packageWorkspace}")

        arcpy.AddMessage("Path as it is")

        try:
            arcpy.env.workspace = self.config['db-sde']
            arcpy.AddMessage(arcpy.env.workspace)
        except Exception as e:
            arcpy.AddError(e)
        try:
            arcpy.env.workspace = self.config['db-gdb']
            arcpy.AddMessage(arcpy.env.workspace)
        except Exception as e:
            arcpy.AddError(e)

        arcpy.AddMessage("Relative path converted to absolute path")
        try:
            arcpy.env.workspace = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.config['db-sde']))
            arcpy.AddMessage(arcpy.env.workspace)
        except Exception as e:
            arcpy.AddError(e)
        try:
            arcpy.env.workspace = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.config['db-gdb']))
            arcpy.AddMessage(arcpy.env.workspace)
        except Exception as e:
            arcpy.AddError(e)
        return


if __name__ == '__main__':
    tb = Toolbox()
    a = ToolA()
    a.execute(None, None)
